from __future__ import annotations

from collections.abc import Container
from typing import Annotated

import typer

from oracle_eval.commands.options import (
    AllowDriftOption,
    CutOption,
    LimitOption,
    ManifestOption,
    OutOption,
    PredictionsOption,
    RepoOption,
    SpendTestSplitOption,
    SplitOption,
    TsmorphOption,
)
from oracle_eval.console import console
from oracle_eval.loading import corpus_for, oracle_for
from oracle_eval.oracle.build import Edge
from oracle_eval.oracle.tsmorph import MODULE_SCOPE
from oracle_eval.paths import (
    DEFAULT_MANIFEST,
    DEFAULT_REPO,
    DEFAULT_TSMORPH,
    PREDICTIONS_ROOT,
    RESULTS_ROOT,
)
from oracle_eval.results import write_result

score_app = typer.Typer(help="Score arms against the oracle, from disk.")


@score_app.command("selfcheck")
def score_selfcheck(
    drop: Annotated[float, typer.Option("--drop", help="Fraction of true edges to withhold")] = 0.0,
    noise: Annotated[float, typer.Option("--noise", help="Invented edges, as a fraction")] = 0.0,
    misattribute: Annotated[
        bool, typer.Option("--misattribute", help="Blame a function that does not contain the call")
    ] = False,
    swap_fields: Annotated[
        bool, typer.Option("--swap-fields", help="Answer in `callable_refs` instead of `calls`")
    ] = False,
    excluded_only: Annotated[
        bool, typer.Option("--excluded-only", help="Predict only what this cut excludes")
    ] = False,
    split: SplitOption = "dev",
    cut: CutOption = "calls_only",
    limit: LimitOption = 0,
    manifest_path: ManifestOption = DEFAULT_MANIFEST,
    tsmorph_path: TsmorphOption = DEFAULT_TSMORPH,
    repo_root: RepoOption = DEFAULT_REPO,
    allow_drift: AllowDriftOption = False,
    spend_test_split: SpendTestSplitOption = False,
) -> None:
    """Score the oracle against itself, damaged by a known amount.

    Calibration, not a result: an undamaged run must report exactly 1.000.
    """
    import random

    from oracle_eval.oracle.tsmorph import FunctionScope, load_tsmorph
    from oracle_eval.predict.parse import ParseResult
    from oracle_eval.predict.schema import PredictedCall, Prediction
    from oracle_eval.score.match import EdgeKey, OracleCut, key_of, normalise
    from oracle_eval.score.run import score_arm

    oracle_cut = OracleCut(cut)
    files = corpus_for(manifest_path, split, limit, repo_root, allow_drift, spend_test_split)
    oracle, aliases = oracle_for(tsmorph_path)
    scopes = load_tsmorph(tsmorph_path).function_scopes if misattribute else {}
    rng = random.Random(20260808)

    def blame_elsewhere(
        edge: Edge, in_file: list[FunctionScope], key: EdgeKey, truth: Container[EdgeKey]
    ) -> str | None:
        file, _, callee = key
        candidates = [
            s.name
            for s in in_file
            if normalise(s.name) != normalise(edge.caller)
            and not any(s.contains(line) for line in edge.call_lines)
            and key_of(file, s.name, callee) not in truth
        ]
        return rng.choice(candidates) if candidates else None

    predictions: dict[str, ParseResult] = {}
    for corpus_file in files:
        truth, excluded = oracle_cut.partition_edges(oracle.get(corpus_file.path, []))
        pairs: list[tuple[str, str]] = []

        if excluded_only:
            pairs = [(caller, callee) for _, caller, callee in sorted(excluded)]
        else:
            in_file = scopes.get(corpus_file.path, [])
            for key, edge in truth.items():
                if rng.random() < drop:
                    continue
                caller = key[1]
                blamed = blame_elsewhere(edge, in_file, key, truth) if misattribute else caller
                if blamed is not None:
                    pairs.append((blamed, key[2]))
            callers = [key[1] for key in truth] or [MODULE_SCOPE]
            pairs += [
                (rng.choice(callers), f"__invented_{i}__") for i in range(round(len(truth) * noise))
            ]

        calls = [PredictedCall(caller=c, callee_text=t) for c, t in pairs]
        answer = (
            Prediction(calls=[], callable_refs=calls) if swap_fields else Prediction(calls=calls)
        )
        predictions[corpus_file.path] = ParseResult(True, True, True, answer)

    damage = [
        name
        for name, on in (
            (f"drop={drop:.0%}", drop),
            (f"noise={noise:.0%}", noise),
            ("misattribute", misattribute),
            ("swap-fields", swap_fields),
            ("excluded-only", excluded_only),
        )
        if on
    ]
    label = f"selfcheck({', '.join(damage) or 'undamaged'})"
    report = score_arm(
        label, files, oracle, predictions, split=split, cut=oracle_cut, aliases=aliases
    )
    console.print(f"\n{report.render()}\n")

    score = report.score
    failures = [
        message
        for condition, message in (
            (
                not damage and score.f1.point != 1.0,
                "an undamaged self-score must be exactly 1.000",
            ),
            (
                misattribute and score.tp != 0,
                f"blaming the wrong function scored {score.tp} true positives, "
                "the caller rule is accepting a function that contains no call site",
            ),
            (
                swap_fields and oracle_cut is OracleCut.CALLS_ONLY and score.tp != 0,
                "the primary cut must not read `callable_refs`",
            ),
            (
                swap_fields and oracle_cut is OracleCut.FULL and score.f1.point != 1.0,
                "the full cut must read `callable_refs`",
            ),
            (
                excluded_only and (score.tp, score.fp) != (0, 0),
                f"predicting only excluded edges scored tp {score.tp} / fp {score.fp}, "
                "a cut must charge them to neither side",
            ),
        )
        if condition
    ]
    for message in failures:
        console.print(f"[red]FAILED: {message}[/red]")
    if failures:
        raise typer.Exit(1)


@score_app.command("run")
def score_run(
    arm: Annotated[str, typer.Argument(help="Arm name, the directory under data/predictions")],
    split: SplitOption = "dev",
    cut: CutOption = "calls_only",
    limit: LimitOption = 0,
    manifest_path: ManifestOption = DEFAULT_MANIFEST,
    tsmorph_path: TsmorphOption = DEFAULT_TSMORPH,
    root: PredictionsOption = PREDICTIONS_ROOT,
    out: OutOption = RESULTS_ROOT,
    repo_root: RepoOption = DEFAULT_REPO,
    allow_drift: AllowDriftOption = False,
    spend_test_split: SpendTestSplitOption = False,
) -> None:
    """Score one arm from cached responses on disk. Never calls a model."""
    from oracle_eval.score.match import OracleCut
    from oracle_eval.score.run import diff_report, load_predictions, score_arm

    oracle_cut = OracleCut(cut)
    files = corpus_for(manifest_path, split, limit, repo_root, allow_drift, spend_test_split)
    predictions = load_predictions(root, arm, files)
    if not predictions:
        console.print(f"[red]no responses under[/red] {root / arm}")
        raise typer.Exit(1)

    oracle, aliases = oracle_for(tsmorph_path)
    report = score_arm(
        arm, files, oracle, predictions, split=split, cut=oracle_cut, aliases=aliases
    )
    console.print(f"\n{report.render()}\n")

    if report.validity.errors:
        console.print(f"[yellow]{len(report.validity.errors)} responses unusable[/yellow]")
        for message in report.validity.errors[:5]:
            console.print(f"  [dim]{message}[/dim]")

    out.mkdir(parents=True, exist_ok=True)
    written = write_result(
        out,
        f"{arm}.{split}.{cut}",
        report.to_json(),
        diff_report(report),
        identity={"arm": arm, "split": split, "cut": cut},
    )
    console.print(f"wrote {written} and the per-edge diff beside it\n")
