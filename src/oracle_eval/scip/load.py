from __future__ import annotations

import json
from pathlib import Path
from typing import NotRequired, TypedDict, cast

from oracle_eval.scip.model import Document, Index, Occurrence, Range, SymbolInfo


class RawMeta(TypedDict):
    tool: NotRequired[str | None]
    tool_version: NotRequired[str | None]
    project_root: NotRequired[str | None]
    document_count: NotRequired[int]
    external_symbol_count: NotRequired[int]


class RawOccurrence(TypedDict):
    range: list[int]
    symbol: str
    roles: NotRequired[int]
    enclosing_range: NotRequired[list[int]]
    syntax_kind: NotRequired[int]


class RawSymbol(TypedDict):
    symbol: str
    kind: NotRequired[int]
    display_name: NotRequired[str]
    enclosing_symbol: NotRequired[str]
    documentation: NotRequired[list[str]]


class RawDocument(TypedDict):
    relative_path: str
    language: NotRequired[int]
    occurrences: NotRequired[list[RawOccurrence]]
    symbols: NotRequired[list[RawSymbol]]


class RawHeader(TypedDict):
    _meta: RawMeta


def load_index(path: Path | str) -> Index:
    path = Path(path)
    index: Index | None = None

    with path.open(encoding="utf8") as fh:
        for lineno, line in enumerate(fh):
            stripped = line.strip()
            if not stripped:
                continue
            record = json.loads(stripped)

            if "_meta" in record:
                meta = cast(RawHeader, record)["_meta"]
                index = Index(
                    project_root=meta.get("project_root") or "",
                    tool=meta.get("tool") or "",
                    tool_version=meta.get("tool_version") or "",
                )
                continue

            if index is None:
                raise ValueError(f"{path}: line {lineno} came before the _meta header")

            index.documents.append(_document(cast(RawDocument, record)))

    if index is None:
        raise ValueError(f"{path}: no _meta header found")
    return index


def _document(record: RawDocument) -> Document:
    return Document(
        relative_path=record["relative_path"],
        occurrences=[_occurrence(o) for o in record.get("occurrences", [])],
        symbols=[
            SymbolInfo(
                symbol=s["symbol"],
                documentation=tuple(s.get("documentation") or ()),
            )
            for s in record.get("symbols", [])
        ],
    )


def _occurrence(raw: RawOccurrence) -> Occurrence:
    enclosing = raw.get("enclosing_range")
    return Occurrence(
        range=Range.from_list(raw["range"]),
        symbol=raw["symbol"],
        roles=raw.get("roles", 0),
        enclosing_range=Range.from_list(enclosing) if enclosing else None,
    )
