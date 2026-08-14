from __future__ import annotations

import json
from collections import Counter
from pathlib import Path
from typing import Annotated

import typer
from rich.table import Table

from oracle_eval.commands.options import (
    AllowDriftOption,
    LimitOption,
    ManifestOption,
    PredictionsOption,
    RepoOption,
    SpendTestSplitOption,
    SplitOption,
    TsmorphOption,
)
from oracle_eval.console import console
from oracle_eval.loading import corpus_for, oracle_for, require_sources
from oracle_eval.oracle.tsmorph import MODULE_SCOPE
from oracle_eval.paths import (
    DEFAULT_MANIFEST,
    DEFAULT_REPO,
    DEFAULT_TSMORPH,
    PREDICTIONS_ROOT,
    RESULTS_ROOT,
)

from .arms import arm_app


@arm_app.command("treesitter")
def arm_treesitter(
    split: SplitOption = "dev",
    limit: LimitOption = 0,
    arm: Annotated[str, typer.Option("--arm")] = "treesitter",
    manifest_path: ManifestOption = DEFAULT_MANIFEST,
    tsmorph_path: TsmorphOption = DEFAULT_TSMORPH,
    repo_root: RepoOption = DEFAULT_REPO,
    root: PredictionsOption = PREDICTIONS_ROOT,
    probe_out: Annotated[Path, typer.Option("--probe")] = RESULTS_ROOT / "recall-probe.jsonl",
    allow_drift: AllowDriftOption = False,
    spend_test_split: SpendTestSplitOption = False,
) -> None:
    """Run the naive syntactic baseline over a split.

    Also writes the invocation sites it deliberately did not claim.
    """
    from oracle_eval.arms.treesitter import Bucket, predict_file
    from oracle_eval.score.match import OracleCut, key_of
    from oracle_eval.score.run import write_predictions

    require_sources(repo_root)
    files = corpus_for(manifest_path, split, limit, repo_root, allow_drift, spend_test_split)
    oracle, _ = oracle_for(tsmorph_path)

    answers: dict[str, dict[str, object]] = {}
    candidates: list[dict[str, object]] = []
    buckets: Counter[str] = Counter()
    dropped: Counter[str] = Counter()
    calls = errors = 0

    for corpus_file in files:
        answer, result = predict_file(repo_root / corpus_file.path, corpus_file.path)
        answers[corpus_file.path] = answer
        calls += len(result.calls)
        errors += result.parse_errors

        truth, excluded = OracleCut.FULL.partition_edges(oracle.get(corpus_file.path, []))
        known = truth.keys() | excluded

        for skipped in result.skipped:
            buckets[skipped.bucket.value] += 1
            if skipped.bucket is Bucket.RESIDUE:
                dropped["residue (not a recall gap)"] += 1
                continue
            if skipped.callee_text is None:
                dropped["unnameable"] += 1
                continue
            if skipped.caller == MODULE_SCOPE:
                dropped["module scope (the primary metric is function callers only)"] += 1
                continue
            if key_of(corpus_file.path, skipped.caller, skipped.callee_text) in known:
                dropped["oracle already holds this edge"] += 1
                continue
            candidates.append(
                {
                    "file": corpus_file.path,
                    "line": skipped.line,
                    "bucket": skipped.bucket.value,
                    "caller": skipped.caller,
                    "callee_text": skipped.callee_text,
                    "source_line": skipped.source_line,
                }
            )

    written = write_predictions(root, arm, answers)
    probe_out.parent.mkdir(parents=True, exist_ok=True)
    probe_out.write_text("".join(json.dumps(row) + "\n" for row in candidates), encoding="utf8")

    console.print(
        f"\n[bold]{arm}[/bold]  ·  {written} files  ·  {calls:,} call sites"
        f"  ·  {errors} parse errors\n"
    )
    if errors:
        console.print(
            f"[red]{errors} nodes failed to parse.[/red] Every number from this run is "
            "suspect until that is zero.\n"
        )

    table = Table("not claimed", "sites", title="Invocation sites the arm did not emit")
    for name, count in sorted(buckets.items()) or [("(none)", 0)]:
        table.add_row(name, f"{count:,}")
    console.print(table)

    if dropped:
        filtered = Table("filtered from the recall probe", "sites")
        for name, count in dropped.most_common():
            filtered.add_row(name, f"{count:,}")
        console.print(filtered)

    console.print(
        f"\n[bold]{len(candidates)}[/bold] oracle-recall candidates -> {probe_out}"
        "   [dim](hand-check these; the oracle's recall is otherwise unmeasured)[/dim]\n"
    )
