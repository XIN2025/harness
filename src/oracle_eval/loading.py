from __future__ import annotations

from pathlib import Path

import typer

from oracle_eval.console import console
from oracle_eval.corpus import (
    SPLITS,
    CorpusFile,
    load_manifest,
    split_of,
    verify_manifest,
)
from oracle_eval.oracle.build import Edge, build_oracle, primary_edges
from oracle_eval.oracle.tsmorph import load_tsmorph
from oracle_eval.paths import DEFAULT_REPO
from oracle_eval.score.match import Aliases
from oracle_eval.score.run import aliases_by_file, edges_by_file


def corpus_for(
    manifest_path: Path,
    split: str,
    limit: int = 0,
    repo_root: Path = DEFAULT_REPO,
    allow_drift: bool = False,
    spend_test_split: bool = False,
) -> list[CorpusFile]:
    if split not in SPLITS:
        console.print(f"[red]split must be one of {', '.join(SPLITS)}[/red]")
        raise typer.Exit(1)

    if split == "test" and not spend_test_split:
        console.print(
            "\n[red]refusing to read the test split[/red]\n"
            "  The split is spendable exactly once, and it has not been spent.\n"
            "  Adjudicating the oracle comes first: every number the\n"
            "  test split would produce is bounded by the oracle's own error rate.\n\n"
            "  Pass [bold]--spend-test-split[/bold] if this is that once, and record the date.\n"
        )
        raise typer.Exit(1)

    files = split_of(load_manifest(manifest_path), split)
    files.sort(key=lambda f: f.path)
    files = files[:limit] if limit else files

    if not repo_root.exists():
        console.print(
            f"\n[yellow]corpus verification skipped[/yellow]: no checkout at {repo_root}\n"
            "  Scores are re-derived from stored responses, so they are unaffected.\n"
            "  What is unverified is that the oracle still matches its sources.\n"
            "  Pass [bold]--repo[/bold] pointing at a checkout to run the check.\n"
        )
        return files

    drift = verify_manifest(files, repo_root)
    if drift:
        console.print(f"\n[red]{len(drift)} corpus files no longer match the frozen split[/red]")
        for problem in drift[:5]:
            console.print(f"  [dim]{problem}[/dim]")
        console.print(
            "\nThe oracle is rebuilt from this repo by a separate command, so scoring now\n"
            "would compare arms against ground truth the frozen corpus never saw. Re-freeze\n"
            "with a recorded reason, or pass --allow-drift and say so in\n"
            "the writeup.\n"
        )
        if not allow_drift:
            raise typer.Exit(1)
    return files


def require_sources(repo_root: Path) -> None:
    """Stop before doing any work if a command needs the corpus files themselves.

    Scoring re-derives from stored responses and only warns; these cannot.
    """
    if repo_root.exists():
        return
    console.print(
        f"\n[red]no corpus checkout at {repo_root}[/red]\n"
        "  This command reads the source files themselves, so it cannot run without\n"
        "  them. Scoring commands can: they re-derive every number from the stored\n"
        "  responses under data/predictions.\n\n"
        "  Pass [bold]--repo[/bold] pointing at a checkout.\n"
    )
    raise typer.Exit(1)


def oracle_for(tsmorph_path: Path) -> tuple[dict[str, list[Edge]], dict[str, Aliases]]:
    extraction = load_tsmorph(tsmorph_path)
    oracle = edges_by_file(primary_edges(build_oracle(extraction)))
    return oracle, aliases_by_file(extraction, oracle)
