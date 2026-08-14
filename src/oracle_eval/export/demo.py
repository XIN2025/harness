from __future__ import annotations

import json
from collections.abc import Mapping, Sequence
from pathlib import Path
from typing import Any, cast

import typer

from oracle_eval.console import console
from oracle_eval.corpus import CorpusFile
from oracle_eval.export.catalogue import (
    EXPLORER_BASE,
    EXPLORER_MODELS,
    HYBRID_PANEL,
    HeadroomRow,
    Row,
)
from oracle_eval.oracle.build import Edge
from oracle_eval.paths import (
    RESULTS_ROOT,
)
from oracle_eval.predict.parse import ParseResult
from oracle_eval.predict.schema import Prediction
from oracle_eval.score.hybrid import score_union_file
from oracle_eval.score.match import NO_ALIASES, Aliases, FileScore, OracleCut, score_file

DEFAULT_OUT = Path("web/data/oracle-eval.json")


def read_result(stem: str, root: Path = RESULTS_ROOT) -> dict[str, Any]:
    path = root / f"{stem}.json"
    if not path.exists():
        console.print(
            f"[red]{path} does not exist[/red] — the demo may only show results that "
            "have been scored and written to disk."
        )
        raise typer.Exit(1)
    return cast(dict[str, Any], json.loads(path.read_text(encoding="utf8")))


def summary_rows(
    rows: Sequence[Row], root: Path = RESULTS_ROOT, expect_files: int | None = None
) -> list[dict[str, Any]]:
    out: list[dict[str, Any]] = []
    for row in rows:
        payload = read_result(row.stem, root)
        counted = payload.get("counts", {}).get("files")
        if expect_files is not None and counted != expect_files:
            console.print(
                f"[red]{row.stem}.json was scored on {counted} files, not {expect_files}[/red] — "
                "this is a partial run overwriting a full one. Re-run the command that "
                "produced it without --limit."
            )
            raise typer.Exit(1)
        out.append(
            {
                "label": row.label,
                "short": row.short,
                "note": row.note,
                "source": f"{row.stem}.json",
                **payload,
            }
        )
    return out


def manifest_summary(path: Path) -> dict[str, Any]:
    manifest = cast(dict[str, Any], json.loads(path.read_text(encoding="utf8")))
    return {
        "path": path.as_posix(),
        "repo": manifest["repo"],
        "counts": manifest["counts"],
        "rule": manifest["rule"],
        "digest": manifest["digest"],
    }


def headroom_rows(rows: Sequence[HeadroomRow], root: Path = RESULTS_ROOT) -> list[dict[str, Any]]:
    out: list[dict[str, Any]] = []
    for row in rows:
        payload = read_result(row.stem, root)
        counts = payload["counts"]
        edges = counts["tp"] + counts["fn"]
        if edges == 0:
            console.print(
                f"[red]{row.stem}.json scored zero edges[/red] — a headroom share over "
                "an empty oracle is not a number."
            )
            raise typer.Exit(1)
        out.append(
            {
                "repo": row.repo,
                "idiom": row.idiom,
                "note": row.note,
                "source": f"{row.stem}.json",
                "files": counts["files"],
                "edges": edges,
                "parser_reached": counts["tp"],
                "parser_missed": counts["fn"],
                "parser_spurious": counts["fp"],
                "unscored": counts["unscored"],
                "headroom": counts["fn"] / edges,
                "recall": payload["metrics"]["recall"],
            }
        )
    return out


def panel_json(score: FileScore) -> dict[str, list[list[str]]]:
    def pairs(keys: Sequence[tuple[str, str, str]]) -> list[list[str]]:
        return [[caller, callee] for _, caller, callee in keys]

    return {
        "matched": pairs(score.matched),
        "spurious": pairs(score.spurious),
        "missed": pairs(score.missed),
        "unscored": pairs(score.unscored),
    }


def file_panels(
    corpus_file: CorpusFile,
    oracle: Mapping[str, list[Edge]],
    aliases: Mapping[str, Aliases],
    predictions: Mapping[str, dict[str, ParseResult]],
    cut: OracleCut,
) -> dict[str, Any]:
    path = corpus_file.path
    edges = oracle.get(path, [])
    alias = aliases.get(path, NO_ALIASES)

    def answer(arm: str) -> Prediction:
        result = predictions.get(arm, {}).get(path)
        return (result.prediction if result else None) or Prediction(calls=[])

    arms = [EXPLORER_BASE, *EXPLORER_MODELS]
    scored = {arm: score_file(path, edges, answer(arm), cut, alias) for arm in arms}
    panels = {arm: panel_json(score) for arm, score in scored.items()}
    panels[HYBRID_PANEL] = panel_json(
        score_union_file(
            path,
            edges,
            [answer(EXPLORER_BASE), *(answer(a) for a in EXPLORER_MODELS)],
            cut,
            alias,
            base_count=1,
            require_agreement=True,
        )
    )

    base = scored[EXPLORER_BASE]
    truth = sorted({*base.matched, *base.missed})

    return {
        "path": path,
        "lines": corpus_file.lines,
        "truth": [[caller, callee] for _, caller, callee in truth],
        "panels": panels,
    }
