from __future__ import annotations

from typing import Annotated, Any

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
from oracle_eval.paths import (
    DEFAULT_MANIFEST,
    DEFAULT_REPO,
    DEFAULT_TSMORPH,
    PREDICTIONS_ROOT,
    RESULTS_ROOT,
)
from oracle_eval.predict.parse import ParseResult
from oracle_eval.results import refuse_clobber, write_json, write_result
from oracle_eval.score.ensemble import (
    OVERLAP_FORMULA,
    OVERLAP_LIMIT,
    arm_errors,
    max_overlap,
    run_ensemble,
)
from oracle_eval.score.match import OracleCut
from oracle_eval.score.run import diff_report, load_predictions

ensemble_app = typer.Typer(
    help="The pre-registered ensemble arm: 2-of-3 majority, computed post-hoc from disk."
)

_CLOBBER_NOTE = "Both name themselves by vote count and cut, so they share a filename."


@ensemble_app.command("run")
def ensemble_run(
    arms: Annotated[
        list[str],
        typer.Argument(help="Two or more arm names, directories under data/predictions"),
    ],
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
    min_votes: Annotated[
        int, typer.Option("--min-votes", help="Votes an edge needs to enter the ensemble")
    ] = 2,
    force: Annotated[
        bool,
        typer.Option("--force", help="Overwrite a result a different set of arms produced"),
    ] = False,
) -> None:
    """Score the frozen ensemble from cached responses on disk. Never calls a model.

    Above 80% pairwise error overlap, only the overlap file is written.
    """
    if len(arms) < 2:
        console.print("[red]an ensemble needs at least two arms[/red]")
        raise typer.Exit(1)
    if len(set(arms)) != len(arms):
        console.print("[red]duplicate arm names, one model must not vote twice[/red]")
        raise typer.Exit(1)
    if not 1 <= min_votes <= len(arms):
        console.print(f"[red]--min-votes must be between 1 and {len(arms)}[/red]")
        raise typer.Exit(1)

    oracle_cut = OracleCut(cut)
    files = corpus_for(manifest_path, split, limit, repo_root, allow_drift, spend_test_split)

    predictions: dict[str, dict[str, ParseResult]] = {}
    for arm in arms:
        loaded = load_predictions(root, arm, files)
        if not loaded:
            console.print(f"[red]no responses under[/red] {root / arm}")
            raise typer.Exit(1)
        predictions[arm] = loaded

    oracle, aliases = oracle_for(tsmorph_path)
    report, per_arm, overlaps = run_ensemble(
        arms,
        files,
        oracle,
        predictions,
        cut=oracle_cut,
        aliases=aliases,
        split=split,
        min_votes=min_votes,
    )

    errors_by_arm = {arm: arm_errors(scores) for arm, scores in per_arm.items()}
    worst = max_overlap(overlaps)
    dropped = worst > OVERLAP_LIMIT

    console.print("\n[bold]error-overlap check[/bold]  ·  containment over error sets")
    for arm_a, arm_b, value in overlaps:
        console.print(
            f"  {arm_a} ({len(errors_by_arm[arm_a])} errors)"
            f"  &  {arm_b} ({len(errors_by_arm[arm_b])} errors)"
            f"  ->  {value:.1%}"
        )
    console.print(f"  max {worst:.1%}  ·  drop above {OVERLAP_LIMIT:.0%}\n")

    out.mkdir(parents=True, exist_ok=True)
    stem = f"{report.arm}.{split}.{cut}"
    overlap_path = out / f"{stem}.overlap.json"
    identity = {"arms": list(arms)}
    refuse_clobber(overlap_path, identity, force=force, note=_CLOBBER_NOTE)
    refuse_clobber(out / f"{stem}.json", identity, force=force, note=_CLOBBER_NOTE)

    overlap_payload: dict[str, Any] = {
        "arms": list(arms),
        "split": split,
        "cut": cut,
        "min_votes": min_votes,
        "formula": OVERLAP_FORMULA,
        "limit": OVERLAP_LIMIT,
        "max": worst,
        "pairs": [{"arm_a": a, "arm_b": b, "overlap": v} for a, b, v in overlaps],
        "errors_by_arm": {arm: len(keys) for arm, keys in errors_by_arm.items()},
        "ensemble_dropped": dropped,
    }
    write_json(overlap_path, overlap_payload)

    if dropped:
        console.print(
            f"[red]ensemble dropped:[/red] pairwise error overlap"
            f" {worst:.1%} exceeds the pre-committed {OVERLAP_LIMIT:.0%} limit."
            f" The overlap number is the published result; no ensemble score is written."
        )
        console.print(f"wrote {overlap_path}\n")
        return

    console.print(f"{report.render()}\n")
    if report.validity.errors:
        console.print(f"[yellow]{len(report.validity.errors)} files below quorum[/yellow]")
        for message in report.validity.errors[:5]:
            console.print(f"  [dim]{message}[/dim]")

    payload = report.to_json()
    payload["arms"] = list(arms)
    payload["overlap"] = overlap_payload
    written = write_result(out, stem, payload, diff_report(report), identity=identity, force=force)
    console.print(f"wrote {written}, the per-edge diff, and {overlap_path.name}\n")
