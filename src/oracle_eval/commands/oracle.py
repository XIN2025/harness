from __future__ import annotations

from collections import Counter
from pathlib import Path
from typing import Annotated

import typer
from rich.table import Table

from oracle_eval.commands.options import (
    IndexOption,
    TsmorphOption,
)
from oracle_eval.console import console
from oracle_eval.oracle.projection import CallEdge, project_index
from oracle_eval.paths import (
    DEFAULT_INDEX,
    DEFAULT_TSMORPH,
)
from oracle_eval.scip.load import load_index
from oracle_eval.scip.symbols import short_name

oracle_app = typer.Typer(help="Build and inspect the oracle.")


def _load_edges(index_path: Path, package: str) -> tuple[list[CallEdge], int]:
    index = load_index(index_path)
    edges = project_index(index, package)
    return edges, len(index.documents)


@oracle_app.command("stats")
def stats(
    index_path: IndexOption = DEFAULT_INDEX,
    package: Annotated[str, typer.Option("--package")] = "remeda",
) -> None:
    """Project the index and report what the oracle actually contains."""
    edges, doc_count = _load_edges(index_path, package)

    primary = [e for e in edges if e.counts_toward_primary]
    by_caller_kind = Counter(e.caller_kind.value for e in edges)
    by_package = Counter(e.callee_package for e in edges)

    console.print(f"\n[bold]{index_path}[/bold]  ·  {doc_count} documents\n")

    in_repo = sum(1 for e in edges if e.in_repo)
    in_repo_src = sum(1 for e in edges if e.in_repo and not e.is_test_file)

    table = Table("cut", "edges", title="From all occurrences down to the primary metric")
    table.add_row("all callable-reference edges", f"{len(edges):,}")
    table.add_row("  in-repo callee", f"{in_repo:,}")
    table.add_row("  in-repo, non-test", f"{in_repo_src:,}")
    table.add_row("[bold]  PRIMARY: function -> function[/bold]", f"[bold]{len(primary):,}[/bold]")
    console.print(table)

    kinds = Table("caller kind", "edges", title="Caller scope (module = imports and re-exports)")
    for kind, count in by_caller_kind.most_common():
        kinds.add_row(kind, f"{count:,}")
    console.print(kinds)

    pkgs = Table("callee package", "edges", title="Where callees live")
    for pkg, count in by_package.most_common(8):
        pkgs.add_row(pkg, f"{count:,}")
    console.print(pkgs)

    files = Counter(e.file for e in primary)
    console.print(
        f"\nfiles with >=1 primary edge: [bold]{len(files):,}[/bold]"
        f"   ·  median edges/file: {sorted(files.values())[len(files) // 2] if files else 0}"
    )
    console.print(f"unique callers: {len({e.caller for e in primary}):,}")
    console.print(f"unique callees: {len({e.callee for e in primary}):,}\n")


@oracle_app.command("show")
def show(
    file: Annotated[str, typer.Argument(help="Path fragment, e.g. src/funnel.ts")],
    index_path: IndexOption = DEFAULT_INDEX,
    package: Annotated[str, typer.Option("--package")] = "remeda",
    all_edges: Annotated[bool, typer.Option("--all", help="Include non-primary")] = False,
) -> None:
    """Print the oracle's edges for one file, for hand spot-checking."""
    edges, _ = _load_edges(index_path, package)
    wanted = file.replace("\\", "/")
    subset = [e for e in edges if wanted in e.file.replace("\\", "/")]
    if not subset:
        console.print(f"[red]no edges found for[/red] {file}")
        raise typer.Exit(1)

    if not all_edges:
        subset = [e for e in subset if e.counts_toward_primary]

    subset.sort(key=lambda e: (e.line, e.callee))
    path = subset[0].file if subset else wanted
    console.print(f"\n[bold]{path}[/bold]  ·  {len(subset)} edges\n")

    table = Table("line", "caller", "callee", "kind", "pkg")
    for e in subset:
        table.add_row(
            str(e.line + 1),
            short_name(e.caller),
            short_name(e.callee),
            e.caller_kind.value,
            "" if e.in_repo else e.callee_package,
        )
    console.print(table)


@oracle_app.command("scopes")
def scopes_cmd(
    file: Annotated[str, typer.Argument(help="Path fragment, e.g. src/funnel.ts")],
    index_path: IndexOption = DEFAULT_INDEX,
) -> None:
    """Show the caller scopes the oracle can see in one file.

    Useful for judging how much inner-function detail SCIP is losing.
    """
    from oracle_eval.oracle.projection import scopes_of

    index = load_index(index_path)
    callable_symbols = frozenset(index.callable_symbols())
    wanted = file.replace("\\", "/")
    for doc in index.documents:
        if wanted not in doc.relative_path.replace("\\", "/"):
            continue
        found = scopes_of(doc, callable_symbols)
        console.print(f"\n[bold]{doc.relative_path}[/bold]  ·  {len(found)} scopes\n")
        table = Table("lines", "kind", "symbol")
        for s in sorted(found, key=lambda s: s.range.start_line):
            table.add_row(
                f"{s.range.start_line + 1}-{s.range.end_line + 1}",
                s.kind.value,
                short_name(s.symbol),
            )
        console.print(table)
        return
    console.print(f"[red]no document matching[/red] {file}")
    raise typer.Exit(1)


@oracle_app.command("crossval")
def crossval_cmd(
    index_path: IndexOption = DEFAULT_INDEX,
    tsmorph_path: TsmorphOption = DEFAULT_TSMORPH,
    package: Annotated[str, typer.Option("--package")] = "remeda",
) -> None:
    """Measure agreement between the ts-morph extractor and scip-typescript.

    Answers the circularity objection with a number instead of an argument.
    """
    from oracle_eval.oracle.crossval import cross_validate, disagreement_profile
    from oracle_eval.oracle.tsmorph import load_tsmorph

    edges, _ = _load_edges(index_path, package)
    extraction = load_tsmorph(tsmorph_path)
    report = cross_validate(edges, extraction)

    console.print(
        f"\n[bold]cross-validation[/bold]  ·  {len(extraction.definitions):,} files"
        f"  ·  {len(extraction.calls):,} ts-morph call sites"
        f"  ·  {len(report.in_repo_names):,} in-repo definition names\n"
    )

    table = Table("comparable subset", "edges")
    table.add_row("both tools agree", f"{len(report.both):,}")
    table.add_row("SCIP only", f"{len(report.scip_only):,}")
    table.add_row("ts-morph only", f"{len(report.tsmorph_only):,}")
    console.print(table)

    scores = Table("measure", "value", "reading")
    scores.add_row(
        "agreement (Jaccard)",
        f"{report.agreement:.1%}",
        "shared share of all evidence",
    )
    scores.add_row(
        "ts-morph confirms SCIP",
        f"{report.tsmorph_recall_of_scip:.1%}",
        "low = our extractor MISSES real edges",
    )
    scores.add_row(
        "SCIP confirms ts-morph",
        f"{report.scip_recall_of_tsmorph:.1%}",
        "low = SCIP cannot express them",
    )
    console.print(scores)

    profile = disagreement_profile(report)
    for label, rows in profile.items():
        if not rows:
            continue
        t = Table("callee", "count", title=label)
        for name, count in rows:
            t.add_row(name, str(count))
        console.print(t)

    if extraction.failures:
        console.print(f"\n[red]{len(extraction.failures)} files failed extraction[/red]")


@oracle_app.command("build")
def build_cmd(
    tsmorph_path: TsmorphOption = DEFAULT_TSMORPH,
) -> None:
    """Summarise the oracle."""
    from oracle_eval.oracle.build import build_oracle, primary_edges
    from oracle_eval.oracle.tsmorph import load_tsmorph

    extraction = load_tsmorph(tsmorph_path)
    edges = build_oracle(extraction)
    primary = primary_edges(edges)

    table = Table("cut", "edges", title="Oracle (ts-morph: calls + callable refs)")
    table.add_row("all edges, non-test", f"{len(edges):,}")
    table.add_row("[bold]  PRIMARY: function caller[/bold]", f"[bold]{len(primary):,}[/bold]")
    table.add_row("  module scope (imports, top-level)", f"{len(edges) - len(primary):,}")
    console.print(table)

    kinds = Table("kind", "edges", title="How the callee was named")
    for kind, count in Counter(e.kind for e in primary).most_common():
        kinds.add_row(kind, f"{count:,}")
    console.print(kinds)

    per_file = Counter(e.file for e in primary)
    counts = sorted(per_file.values())
    console.print(
        f"files with >=1 primary edge: [bold]{len(per_file):,}[/bold]"
        f"  ·  median {counts[len(counts) // 2]}"
        f"  ·  max {counts[-1]}\n"
    )


from oracle_eval.commands import audit as _audit  # noqa: E402, F401
