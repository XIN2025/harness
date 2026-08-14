from __future__ import annotations

from pathlib import Path
from typing import Annotated

import typer

SplitOption = Annotated[
    str,
    typer.Option("--split", help="dev | test. The test split is spendable exactly once"),
]

CutOption = Annotated[
    str,
    typer.Option(
        "--cut",
        help="calls_only (the primary metric, invocations) | full (adds callable references)",
    ),
]

LimitOption = Annotated[
    int,
    typer.Option("--limit", help="Score only the first N files. 0 = the whole split"),
]

ManifestOption = Annotated[Path, typer.Option("--manifest", help="The frozen corpus manifest")]
TsmorphOption = Annotated[Path, typer.Option("--tsmorph", help="The ts-morph extraction")]
IndexOption = Annotated[Path, typer.Option("--index", help="The scip-typescript index")]
RepoOption = Annotated[Path, typer.Option("--repo", help="Checkout the corpus was frozen against")]
PredictionsOption = Annotated[
    Path, typer.Option("--predictions", help="Root of the per-arm raw responses")
]
OutOption = Annotated[Path, typer.Option("--out", help="Directory to write results into")]

SpendTestSplitOption = Annotated[
    bool,
    typer.Option(
        "--spend-test-split",
        help="Required to read --split test. It is spendable exactly once "
        "and reading it is the one irreversible act here.",
    ),
]

AllowDriftOption = Annotated[
    bool,
    typer.Option(
        "--allow-drift",
        help="Proceed even if the corpus no longer matches its frozen manifest. The oracle "
        "is rebuilt from that checkout separately, so this scores against ground truth the "
        "frozen split never saw. Say so in the writeup.",
    ),
]

__all__ = [
    "AllowDriftOption",
    "CutOption",
    "IndexOption",
    "LimitOption",
    "ManifestOption",
    "OutOption",
    "PredictionsOption",
    "RepoOption",
    "SpendTestSplitOption",
    "SplitOption",
    "TsmorphOption",
]
