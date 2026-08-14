from __future__ import annotations

import json
from collections import defaultdict
from collections.abc import Mapping
from dataclasses import dataclass
from pathlib import Path
from typing import Any

from oracle_eval.corpus import CorpusFile
from oracle_eval.oracle.build import Edge
from oracle_eval.oracle.tsmorph import TsExtraction
from oracle_eval.predict.parse import ParseResult, ValidityReport, parse_response
from oracle_eval.predict.schema import Prediction
from oracle_eval.score.match import (
    NO_ALIASES,
    Aliases,
    FileScore,
    OracleCut,
    alias_index,
    render_key,
    score_file,
)
from oracle_eval.score.metrics import ArmScore, aggregate


def edges_by_file(edges: list[Edge]) -> dict[str, list[Edge]]:
    grouped: dict[str, list[Edge]] = defaultdict(list)
    for edge in edges:
        grouped[edge.file].append(edge)
    return dict(grouped)


def aliases_by_file(
    extraction: TsExtraction, oracle: Mapping[str, list[Edge]]
) -> dict[str, Aliases]:
    return {
        path: alias_index(edges, extraction.function_scopes.get(path, []))
        for path, edges in oracle.items()
    }


def prediction_path(root: Path, arm: str, relative_path: str) -> Path:
    return root / arm / f"{relative_path}.json"


@dataclass(frozen=True, slots=True)
class ArmReport:
    arm: str
    split: str
    cut: OracleCut
    score: ArmScore
    validity: ValidityReport

    def render(self) -> str:
        return (
            f"{self.arm}  ·  {self.split}  ·  cut={self.cut.value}\n"
            f"  validity   {self.validity.render()}\n"
            f"  accuracy   {self.score.render()}\n"
            f"  counts     {self.score.render_counts()}"
        )

    def to_json(self) -> dict[str, Any]:
        return {
            "arm": self.arm,
            "split": self.split,
            "cut": self.cut.value,
            "validity": {
                "total": self.validity.total,
                "raw_valid": self.validity.raw_valid,
                "parseable": self.validity.parseable,
                "schema_valid": self.validity.schema_valid,
            },
            "counts": {
                "tp": self.score.tp,
                "fp": self.score.fp,
                "fn": self.score.fn,
                "unscored": self.score.unscored,
                "files": self.score.n_files,
            },
            "metrics": {
                name: {
                    "point": interval.point,
                    "low": interval.low,
                    "high": interval.high,
                    "method": interval.method,
                }
                for name, interval in (
                    ("precision", self.score.precision),
                    ("recall", self.score.recall),
                    ("f1", self.score.f1),
                )
            },
        }


def score_arm(
    arm: str,
    files: list[CorpusFile],
    oracle: dict[str, list[Edge]],
    predictions: dict[str, ParseResult],
    *,
    split: str = "dev",
    cut: OracleCut = OracleCut.CALLS_ONLY,
    aliases: Mapping[str, Aliases] | None = None,
) -> ArmReport:
    validity = ValidityReport()
    scores: list[FileScore] = []

    for corpus_file in files:
        result = predictions.get(
            corpus_file.path, ParseResult(False, False, False, error="no response on disk")
        )
        validity.add(result)
        prediction = result.prediction or Prediction(calls=[])
        edges = oracle.get(corpus_file.path, [])
        alias = (aliases or {}).get(corpus_file.path, NO_ALIASES)
        scores.append(score_file(corpus_file.path, edges, prediction, cut, alias))

    return ArmReport(arm, split, cut, aggregate(scores), validity)


def load_predictions(root: Path, arm: str, files: list[CorpusFile]) -> dict[str, ParseResult]:
    loaded: dict[str, ParseResult] = {}
    for corpus_file in files:
        path = prediction_path(root, arm, corpus_file.path)
        if path.exists():
            loaded[corpus_file.path] = parse_response(path.read_text(encoding="utf8"))
    return loaded


def write_predictions(root: Path, arm: str, responses: Mapping[str, str | dict[str, Any]]) -> int:
    for relative_path, body in responses.items():
        path = prediction_path(root, arm, relative_path)
        path.parent.mkdir(parents=True, exist_ok=True)
        text = body if isinstance(body, str) else json.dumps(body, indent=2)
        path.write_text(text, encoding="utf8")
    return len(responses)


def diff_report(report: ArmReport, limit_per_file: int = 0) -> str:
    lines = [
        f"# {report.arm} / {report.split} / cut={report.cut.value}",
        "",
        report.validity.render(),
        report.score.render(),
        "",
        "`-` missed by the arm (in the oracle, not predicted)",
        "`+` spurious (predicted, not in the oracle)",
        "`~` unscored, this cut excludes the class, so it counts against neither side",
        "",
    ]

    for file_score in sorted(report.score.files, key=lambda f: (-f.fp - f.fn, f.path)):
        if not file_score.missed and not file_score.spurious and not file_score.unscored:
            continue
        lines.append(
            f"## {file_score.path}"
            f"  (tp {file_score.tp}, fp {file_score.fp}, fn {file_score.fn},"
            f" unscored {len(file_score.unscored)})"
        )
        for marker, keys in (
            ("-", file_score.missed),
            ("+", file_score.spurious),
            ("~", file_score.unscored),
        ):
            shown = keys[:limit_per_file] if limit_per_file else keys
            lines += [f"  {marker} {render_key(key)}" for key in shown]
            if limit_per_file and len(keys) > limit_per_file:
                lines.append(f"  {marker} ... and {len(keys) - limit_per_file} more")
        lines.append("")

    perfect = sum(1 for f in report.score.files if not f.missed and not f.spurious)
    lines.append(f"{perfect} of {report.score.n_files} files exactly right.")
    return "\n".join(lines) + "\n"
