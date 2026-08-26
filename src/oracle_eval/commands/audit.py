from __future__ import annotations

import hashlib
import re
from collections import Counter
from pathlib import Path
from typing import Annotated

import typer
from rich.table import Table

from oracle_eval.commands.options import (
    ManifestOption,
    RepoOption,
    TsmorphOption,
)
from oracle_eval.console import console
from oracle_eval.corpus import load_manifest
from oracle_eval.paths import (
    DEFAULT_MANIFEST,
    DEFAULT_REPO,
    DEFAULT_TSMORPH,
)

from .oracle import oracle_app


@oracle_app.command("adjudicate")
def adjudicate(
    files: Annotated[
        str,
        typer.Option(
            "--files",
            help="comma-separated path fragments; exclusive with --sample-size",
        ),
    ] = "",
    sample_size: Annotated[
        int,
        typer.Option(
            "--sample-size",
            min=0,
            help="deterministic edge sample; frozen test files are excluded by default",
        ),
    ] = 0,
    sample_seed: Annotated[
        str,
        typer.Option("--sample-seed", help="public seed for deterministic SHA-256 ranking"),
    ] = "oracle-adjudication-v1",
    manifest_path: ManifestOption = DEFAULT_MANIFEST,
    include_test_split: Annotated[
        bool,
        typer.Option(
            "--include-test-split",
            help="allow deterministic sampling from files reserved for the one-shot test score",
        ),
    ] = False,
    repo_root: RepoOption = DEFAULT_REPO,
    tsmorph_path: TsmorphOption = DEFAULT_TSMORPH,
    out: Annotated[Path, typer.Option("--out")] = Path("data/oracle/adjudication.md"),
) -> None:
    """Emit a hand-checkable sheet: every oracle edge with its source line.

    Tool-vs-tool agreement measures difference, not correctness.
    """
    from oracle_eval.oracle.build import Edge, build_oracle
    from oracle_eval.oracle.tsmorph import load_tsmorph

    extraction = load_tsmorph(tsmorph_path)
    oracle = build_oracle(extraction)

    wanted = [f.strip().replace("\\", "/") for f in files.split(",") if f.strip()]
    if bool(wanted) == bool(sample_size):
        console.print("[red]choose exactly one of --files or --sample-size[/red]")
        raise typer.Exit(1)

    selection_lines: list[str]
    if sample_size:
        test_files = {
            corpus_file.path
            for corpus_file in load_manifest(manifest_path)
            if corpus_file.split == "test"
        }
        population = [edge for edge in oracle if include_test_split or edge.file not in test_files]
        if sample_size > len(population):
            console.print(
                f"[red]sample size {sample_size} exceeds population {len(population)}[/red]"
            )
            raise typer.Exit(1)

        def sample_rank(edge: Edge) -> str:
            identity = "\x00".join(
                (
                    sample_seed,
                    edge.file,
                    edge.caller,
                    edge.callee,
                    edge.kind.value,
                    str(edge.line),
                )
            )
            return hashlib.sha256(identity.encode("utf8")).hexdigest()

        selected = sorted(
            sorted(population, key=sample_rank)[:sample_size],
            key=lambda edge: (edge.file, edge.line, edge.caller, edge.callee),
        )
        selection_lines = [
            (
                f"Selection: the first {sample_size} edges under SHA-256 ranking of the "
                f"{len(population)} eligible oracle edges."
            ),
            f"Public seed: `{sample_seed}`.",
            (
                "Frozen test-split files were included."
                if include_test_split
                else f"Frozen test-split files excluded: {len(test_files)}."
            ),
        ]
    else:
        selected = [e for e in oracle if any(w in e.file for w in wanted)]
        selection_lines = [f"Selection: all edges in files matching `{','.join(wanted)}`."]

    if not selected:
        console.print(f"[red]no edges for[/red] {wanted or sample_size}")
        raise typer.Exit(1)

    source_cache: dict[str, list[str]] = {}

    def source_line(rel: str, line: int) -> str:
        if rel not in source_cache:
            candidate = repo_root / rel
            source_cache[rel] = (
                candidate.read_text(encoding="utf8").splitlines() if candidate.exists() else []
            )
        lines = source_cache[rel]
        return lines[line - 1].strip() if 0 < line <= len(lines) else "<source not found>"

    rows = ["# Oracle adjudication sheet", ""]
    rows.append("Mark each row `Y` (a real call or callable reference) or `N`.")
    rows.append("Check against the quoted source line; `kind` is the oracle's claim, not a hint.")
    rows.append("")
    rows.extend(selection_lines)
    rows.append("")

    for path in sorted({e.file for e in selected}):
        in_file = [e for e in selected if e.file == path]
        rows += [f"## {path}  ({len(in_file)} edges)", ""]
        rows.append("| Y/N | line | caller | callee | kind | source line |")
        rows.append("|---|---|---|---|---|---|")
        for e in in_file:
            text = source_line(e.file, e.line).replace("|", "\\|")[:80]
            rows.append(f"|  | {e.line} | `{e.caller}` | `{e.callee}` | {e.kind} | `{text}` |")
        rows.append("")

    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text("\n".join(rows) + "\n", encoding="utf8")

    console.print(f"\nwrote [bold]{len(selected)}[/bold] edges to {out}")
    console.print(f"by kind: {dict(Counter(e.kind for e in selected))}\n")


@oracle_app.command("adjudication-status")
def adjudication_status(
    sheet: Annotated[Path, typer.Option("--sheet")] = Path("data/oracle/adjudication.md"),
    minimum: Annotated[int, typer.Option("--minimum", min=1)] = 60,
) -> None:
    """Verify that the published manual adjudication reaches its frozen gate."""
    if not sheet.is_file():
        console.print(f"[red]adjudication sheet not found[/red]: {sheet}")
        raise typer.Exit(1)

    decisions: list[str] = []
    for line in sheet.read_text(encoding="utf8").splitlines():
        match = re.match(r"^\|\s*([^|]*)\|\s*(\d+)\s*\|", line)
        if match is not None:
            decisions.append(match.group(1).strip())

    yes = decisions.count("Y")
    no = decisions.count("N")
    incomplete = len(decisions) - yes - no
    checked = yes + no
    rule_of_three_lower = max(0.0, 1.0 - (3.0 / checked)) if checked else 0.0
    passed = checked >= minimum and no == 0 and incomplete == 0

    console.print(
        f"\nadjudication {'PASS' if passed else 'FAIL'}"
        f"  checked={checked}  Y={yes}  N={no}  incomplete={incomplete}\n"
        f"  zero-error rule-of-three lower bound: {rule_of_three_lower:.1%}\n"
    )
    if not passed:
        raise typer.Exit(1)


@oracle_app.command("blindspots")
def blindspots(
    repos_root: Annotated[Path, typer.Option("--repos")] = Path("../slm/repos"),
    only: Annotated[str, typer.Option("--only", help="comma-separated repo names")] = "",
    max_files: Annotated[int, typer.Option("--max-files", help="0 = all")] = 0,
) -> None:
    """Count, per repo, the invocations the oracle is structurally blind to.

    A blind spot empty on one corpus is not one you have ruled out.
    """
    from oracle_eval.arms.treesitter import Bucket, extract_file

    wanted = {name.strip() for name in only.split(",") if name.strip()}
    # A missing directory is the ordinary case in a fresh checkout, not an
    # exception: the corpus repos live in the sibling tree. Route it into the
    # message below rather than letting iterdir raise a traceback at a reader.
    repos = sorted(p for p in repos_root.iterdir() if p.is_dir()) if repos_root.is_dir() else []
    if wanted:
        repos = [p for p in repos if p.name in wanted]
    if not repos:
        console.print(f"[red]no repos under[/red] {repos_root}")
        raise typer.Exit(1)

    buckets = [b for b in Bucket if b is not Bucket.RESIDUE]
    table = Table("repo", "files", "calls", *[b.value for b in buckets], "errors")
    totals: Counter[str] = Counter()

    for repo in repos:
        sources = [
            path
            for path in repo.rglob("*.ts*")
            if path.suffix in (".ts", ".tsx")
            and not path.name.endswith(".d.ts")
            and "node_modules" not in path.parts
        ]
        sources = sources[:max_files] if max_files else sources
        found: Counter[str] = Counter()
        calls = errors = 0

        for path in sources:
            try:
                source = path.read_text(encoding="utf8")
            except (OSError, UnicodeDecodeError):
                continue
            result = extract_file(source, tsx=path.suffix == ".tsx")
            calls += len(result.calls)
            errors += result.parse_errors
            for skipped in result.skipped:
                found[skipped.bucket.value] += 1

        table.add_row(
            repo.name,
            f"{len(sources):,}",
            f"{calls:,}",
            *[f"{found[b.value]:,}" if found[b.value] else "·" for b in buckets],
            f"{errors:,}" if errors else "·",
        )
        totals.update(found)

    console.print("\n[bold]Constructs the oracle cannot see[/bold]\n")
    console.print(table)
    console.print(
        "\n[dim]`·` is a measured zero, not an untested one. A repo with non-zero"
        "\ncounts cannot be scored until the walk is widened or those files are"
        "\nexcluded and the excluded count published.[/dim]\n"
    )
