from __future__ import annotations

import json
from dataclasses import dataclass, field
from pathlib import Path
from typing import NotRequired, TypedDict, cast

MODULE_SCOPE = "__module__"


class RawCall(TypedDict):
    caller: str
    callee_text: str
    kind: str
    receiver: str | None
    receiver_type_hint: NotRequired[str | None]
    callee_file_hint: NotRequired[str | None]
    line: int


class RawScope(TypedDict):
    name: str
    start_line: int
    end_line: int


class RawFile(TypedDict):
    relative_path: str
    line_count: NotRequired[int]
    definitions: NotRequired[list[str]]
    calls: NotRequired[list[RawCall]]
    callable_refs: NotRequired[list[RawCall]]
    function_scopes: NotRequired[list[RawScope]]
    error: NotRequired[str]


@dataclass(frozen=True, slots=True)
class FunctionScope:
    name: str
    start_line: int
    end_line: int

    def contains(self, line: int) -> bool:
        return self.start_line <= line <= self.end_line

    def within(self, other: FunctionScope) -> bool:
        return other.start_line <= self.start_line and self.end_line <= other.end_line


@dataclass(frozen=True, slots=True)
class TsCall:
    file: str
    caller: str
    callee_text: str
    kind: str
    receiver: str | None
    callee_file_hint: str | None
    line: int

    @property
    def key(self) -> tuple[str, str, str]:
        return (self.file, self.caller, self.callee_text)

    @property
    def is_external(self) -> bool:
        return self.callee_file_hint == "external"


@dataclass(slots=True)
class TsExtraction:
    calls: list[TsCall]
    definitions: dict[str, list[str]]
    line_counts: dict[str, int]
    failures: dict[str, str]
    callable_refs: list[TsCall] = field(default_factory=list)
    function_scopes: dict[str, list[FunctionScope]] = field(default_factory=dict)


def _call(rel: str, raw: RawCall) -> TsCall:
    return TsCall(
        file=rel,
        caller=raw["caller"],
        callee_text=raw["callee_text"],
        kind=raw["kind"],
        receiver=raw.get("receiver"),
        callee_file_hint=raw.get("callee_file_hint"),
        line=raw["line"],
    )


def load_tsmorph(path: Path | str) -> TsExtraction:
    calls: list[TsCall] = []
    callable_refs: list[TsCall] = []
    definitions: dict[str, list[str]] = {}
    line_counts: dict[str, int] = {}
    failures: dict[str, str] = {}
    function_scopes: dict[str, list[FunctionScope]] = {}

    with Path(path).open(encoding="utf8") as fh:
        for line in fh:
            stripped = line.strip()
            if not stripped:
                continue
            record = cast(RawFile, json.loads(stripped))
            rel = record["relative_path"].replace("\\", "/")

            if "error" in record:
                failures[rel] = record["error"]
                continue

            definitions[rel] = record.get("definitions", [])
            line_counts[rel] = record.get("line_count", 0)
            calls.extend(_call(rel, raw) for raw in record.get("calls", []))
            callable_refs.extend(_call(rel, raw) for raw in record.get("callable_refs", []))
            function_scopes[rel] = [
                FunctionScope(
                    name=raw["name"],
                    start_line=raw["start_line"],
                    end_line=raw["end_line"],
                )
                for raw in record.get("function_scopes", [])
            ]

    return TsExtraction(
        calls=calls,
        callable_refs=callable_refs,
        definitions=definitions,
        line_counts=line_counts,
        failures=failures,
        function_scopes=function_scopes,
    )
