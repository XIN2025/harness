from __future__ import annotations

import json
from pathlib import Path
from typing import Annotated

import typer

from oracle_eval.arms.prompts import load_prompts
from oracle_eval.commands.options import (
    AllowDriftOption,
    CutOption,
    LimitOption,
    ManifestOption,
    PredictionsOption,
    RepoOption,
    SpendTestSplitOption,
    SplitOption,
    TsmorphOption,
)
from oracle_eval.console import console
from oracle_eval.export.catalogue import (
    BASELINES,
    CURVE,
    EXPLORER_BASE,
    EXPLORER_MODELS,
    HEADROOM,
    HYBRID,
    HYBRID_PANEL,
    MODELS,
    NOT_CLAIMED,
    OVERLAPS,
    UNSCOREABLE,
)
from oracle_eval.export.demo import (
    DEFAULT_OUT,
    file_panels,
    headroom_rows,
    manifest_summary,
    summary_rows,
)
from oracle_eval.loading import corpus_for, oracle_for
from oracle_eval.paths import (
    DEFAULT_MANIFEST,
    DEFAULT_REPO,
    DEFAULT_TSMORPH,
    PREDICTIONS_ROOT,
    RESULTS_ROOT,
)
from oracle_eval.predict.parse import ParseResult
from oracle_eval.score.match import OracleCut
from oracle_eval.score.run import load_predictions

export_app = typer.Typer(help="Export measured results for downstream readers.")


@export_app.callback()
def _export_group() -> None:
    """Keep 'demo' an explicit subcommand rather than collapsing into the root."""


@export_app.command("demo")
def export_demo(
    out: Annotated[Path, typer.Option("--out", help="JSON file to write")] = DEFAULT_OUT,
    split: SplitOption = "dev",
    cut: CutOption = "full",
    limit: LimitOption = 0,
    manifest_path: ManifestOption = DEFAULT_MANIFEST,
    tsmorph_path: TsmorphOption = DEFAULT_TSMORPH,
    root: PredictionsOption = PREDICTIONS_ROOT,
    results: Annotated[Path, typer.Option("--results")] = RESULTS_ROOT,
    repo_root: RepoOption = DEFAULT_REPO,
    allow_drift: AllowDriftOption = False,
    spend_test_split: SpendTestSplitOption = False,
) -> None:
    """Write every measured number the demo shows to one JSON file. No model calls.

    The inherited drift check matters: a stale explorer page misleads too.
    """
    oracle_cut = OracleCut(cut)
    files = corpus_for(manifest_path, split, limit, repo_root, allow_drift, spend_test_split)
    oracle, aliases = oracle_for(tsmorph_path)

    predictions: dict[str, dict[str, ParseResult]] = {}
    for arm in (EXPLORER_BASE, *EXPLORER_MODELS):
        loaded = load_predictions(root, arm, files)
        if not loaded:
            console.print(f"[red]no responses on disk for[/red] {root / arm}")
            raise typer.Exit(1)
        predictions[arm] = loaded

    payload = {
        "meta": {
            "project": "oracle-eval",
            "split": split,
            "explorer_cut": oracle_cut.value,
            "corpus": {
                "repo": "remeda",
                "files": len(files),
                "oracle_edges": sum(
                    len(oracle_cut.partition_edges(oracle.get(f.path, []))[0]) for f in files
                ),
                "manifest": manifest_summary(manifest_path),
            },
            "models": list(MODELS),
            "prompts": len(load_prompts()),
            "not_claimed": list(NOT_CLAIMED),
            "explorer_panels": [EXPLORER_BASE, *EXPLORER_MODELS, HYBRID_PANEL],
        },
        "curve": summary_rows(CURVE, results, expect_files=len(files)),
        "baselines": summary_rows(BASELINES, results),
        "hybrid": summary_rows(HYBRID, results, expect_files=len(files)),
        "overlap": summary_rows(OVERLAPS, results),
        "headroom": {
            "scored": headroom_rows(HEADROOM, results),
            "unscoreable": list(UNSCOREABLE),
        },
        "files": [file_panels(f, oracle, aliases, predictions, oracle_cut) for f in files],
    }

    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(payload, indent=1) + "\n", encoding="utf8")
    size = out.stat().st_size
    console.print(
        f"\nwrote [bold]{out}[/bold]  ({size / 1024:.0f} KB)\n"
        f"  {len(payload['curve'])} curve rows · {len(payload['hybrid'])} hybrid rows · "
        f"{len(HEADROOM)} headroom rows · {len(files)} files\n"
    )
