from __future__ import annotations

import json
from pathlib import Path
from typing import Annotated, cast

import typer
from rich.table import Table

from oracle_eval.commands.options import (
    LimitOption,
    ManifestOption,
    RepoOption,
    TsmorphOption,
)
from oracle_eval.console import console
from oracle_eval.corpus import (
    SPLITS,
    SRC_PREFIX,
    CorpusFile,
    Manifest,
    digest_of,
    load_manifest,
    select_corpus,
    split_of,
    to_manifest,
    write_manifest,
)
from oracle_eval.paths import (
    DEFAULT_MANIFEST,
    DEFAULT_REPO,
    DEFAULT_TSMORPH,
)

corpus_app = typer.Typer(help="Select, split and freeze the corpus.")


def _select(tsmorph_path: Path, repo_root: Path, prefix: str) -> list[CorpusFile]:
    from oracle_eval.oracle.build import build_oracle, primary_edges
    from oracle_eval.oracle.tsmorph import load_tsmorph

    extraction = load_tsmorph(tsmorph_path)
    edges = primary_edges(build_oracle(extraction))
    return select_corpus(edges, extraction.line_counts, repo_root, prefix)


def _report(files: list[CorpusFile]) -> None:
    table = Table("split", "files", "edges", "lines: min / median / max")
    for split in SPLITS:
        rows = split_of(files, split)
        if not rows:
            continue
        lines = sorted(f.lines for f in rows)
        table.add_row(
            split,
            f"{len(rows):,}",
            f"{sum(f.edges for f in rows):,}",
            f"{lines[0]} / {lines[len(lines) // 2]} / {lines[-1]}",
        )
    console.print(table)


@corpus_app.command("select")
def corpus_select(
    tsmorph_path: TsmorphOption = DEFAULT_TSMORPH,
    repo_root: RepoOption = DEFAULT_REPO,
    prefix: Annotated[str, typer.Option("--src-prefix")] = SRC_PREFIX,
) -> None:
    """Apply the selection rule and show the split, without writing anything."""
    files = _select(tsmorph_path, repo_root, prefix)
    console.print(f"\n[bold]{len(files)}[/bold] files qualify under the selection rule\n")
    _report(files)
    console.print(f"\ndigest: [dim]{digest_of(files)}[/dim]\n")


@corpus_app.command("freeze")
def corpus_freeze(
    tsmorph_path: TsmorphOption = DEFAULT_TSMORPH,
    repo_root: RepoOption = DEFAULT_REPO,
    out: Annotated[Path, typer.Option("--out")] = DEFAULT_MANIFEST,
    repo: Annotated[str, typer.Option("--name")] = "remeda",
    prefix: Annotated[str, typer.Option("--src-prefix")] = SRC_PREFIX,
    force: Annotated[bool, typer.Option("--force", help="Overwrite a differing manifest")] = False,
) -> None:
    """Write the manifest. Refuses to silently change an existing split."""
    files = _select(tsmorph_path, repo_root, prefix)
    manifest = to_manifest(repo, files, prefix)

    if out.exists() and not force:
        existing = cast(Manifest, json.loads(out.read_text(encoding="utf8")))
        if existing["digest"] != manifest["digest"]:
            console.print(
                f"\n[red]refusing to overwrite[/red] {out}\n"
                f"  recorded  {existing['digest'][:16]}  ({existing['counts']})\n"
                f"  would be  {manifest['digest'][:16]}  ({manifest['counts']})\n\n"
                "The split has already been frozen. Re-splitting after a score exists is how a\n"
                "result gets chosen rather than measured. Pass --force, and record why, if\n"
                "this is deliberate.\n"
            )
            raise typer.Exit(1)
        console.print(f"[dim]{out} already frozen, identical — nothing to do[/dim]")
        return

    write_manifest(out, manifest)
    console.print(f"\nfroze [bold]{len(files)}[/bold] files to {out}\n")
    _report(files)
    console.print(f"\ndigest: [dim]{manifest['digest']}[/dim]\n")


@corpus_app.command("show")
def corpus_show(
    split: Annotated[str, typer.Argument(help="dev | test")] = "dev",
    manifest_path: ManifestOption = DEFAULT_MANIFEST,
    limit: LimitOption = 20,
) -> None:
    """List the files in one split, verifying the manifest digest on load.

    Reads the test split deliberately: the rule reserves scoring, not listing.
    """
    if split not in SPLITS:
        console.print(f"[red]split must be one of {', '.join(SPLITS)}[/red]")
        raise typer.Exit(1)

    rows = split_of(load_manifest(manifest_path), split)
    rows.sort(key=lambda f: -f.edges)
    console.print(f"\n[bold]{split}[/bold]  ·  {len(rows)} files  ·  top {limit} by edges\n")

    table = Table("path", "edges", "lines")
    for f in rows[:limit]:
        table.add_row(f.path, str(f.edges), str(f.lines))
    console.print(table)
