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
from oracle_eval.results import write_result
from oracle_eval.score.hybrid import run_hybrid
from oracle_eval.score.match import OracleCut
from oracle_eval.score.metrics import ArmScore
from oracle_eval.score.run import diff_report, load_predictions

hybrid_app = typer.Typer(help="Combine a deterministic base arm with model additions, from disk.")

_CLOBBER_NOTE = (
    "A union and an agreement hybrid over the same arms share a filename: "
    "the stem carries the arms but not --require-agreement."
)


def _delta(hybrid: ArmScore, base: ArmScore) -> str:
    def arrow(new: float, old: float) -> str:
        gap = 100 * (new - old)
        colour = "green" if gap > 0 else ("red" if gap < 0 else "dim")
        return f"[{colour}]{gap:+.1f}[/{colour}]"

    return (
        f"  delta vs base   P {arrow(hybrid.precision.point, base.precision.point)}"
        f"   R {arrow(hybrid.recall.point, base.recall.point)}"
        f"   F1 {arrow(hybrid.f1.point, base.f1.point)}"
    )


@hybrid_app.command("run")
def hybrid_run(
    base: Annotated[str, typer.Argument(help="Deterministic base arm, e.g. treesitter")],
    additions: Annotated[list[str], typer.Argument(help="Model arms that ADD to the base")],
    split: SplitOption = "dev",
    cut: CutOption = "full",
    limit: LimitOption = 0,
    manifest_path: ManifestOption = DEFAULT_MANIFEST,
    tsmorph_path: TsmorphOption = DEFAULT_TSMORPH,
    root: PredictionsOption = PREDICTIONS_ROOT,
    out: OutOption = RESULTS_ROOT,
    repo_root: RepoOption = DEFAULT_REPO,
    allow_drift: AllowDriftOption = False,
    spend_test_split: SpendTestSplitOption = False,
    require_agreement: Annotated[
        bool,
        typer.Option(
            "--require-agreement",
            help="Add only edges ALL model arms name. Needs 2+ additions; the base is "
            "always unioned in and never voted on",
        ),
    ] = False,
    force: Annotated[
        bool,
        typer.Option("--force", help="Overwrite a result a different construct produced"),
    ] = False,
) -> None:
    """Score `base UNION additions` from disk, beside the base alone. No model calls."""
    oracle_cut = OracleCut(cut)
    if oracle_cut is OracleCut.CALLS_ONLY:
        console.print(
            "[yellow]--cut calls_only: the deterministic base already recovers essentially "
            "every edge here, so additions can only add false positives. Measured, not "
            "assumed.[/yellow]"
        )
    if require_agreement and len(additions) < 2:
        console.print(
            "[red]--require-agreement needs at least two model arms[/red], with one arm "
            "there is nothing to agree with, and silently treating it as union would "
            "report a different construct under the same name."
        )
        raise typer.Exit(1)

    files = corpus_for(manifest_path, split, limit, repo_root, allow_drift, spend_test_split)
    oracle, aliases = oracle_for(tsmorph_path)

    predictions: dict[str, dict[str, ParseResult]] = {}
    for arm in (base, *additions):
        loaded = load_predictions(root, arm, files)
        if not loaded:
            console.print(f"[red]no responses on disk for[/red] {root / arm}")
            raise typer.Exit(1)
        predictions[arm] = loaded

    hybrid, base_report = run_hybrid(
        base,
        additions,
        files,
        oracle,
        predictions,
        cut=oracle_cut,
        aliases=aliases,
        split=split,
        require_agreement=require_agreement,
    )

    console.print(f"\n{base_report.render()}\n")
    console.print(f"{hybrid.render()}")
    console.print(_delta(hybrid.score, base_report.score) + "\n")

    out.mkdir(parents=True, exist_ok=True)
    stem = f"hybrid-{base}-{'-'.join(additions)}.{split}.{cut}"
    payload: dict[str, Any] = {
        **hybrid.to_json(),
        "base": base_report.to_json(),
        "additions": list(additions),
    }
    written = write_result(
        out,
        stem,
        payload,
        diff_report(hybrid),
        identity={"arm": hybrid.arm},
        force=force,
        note=_CLOBBER_NOTE,
    )
    console.print(f"wrote {written} and the per-edge diff beside it\n")
