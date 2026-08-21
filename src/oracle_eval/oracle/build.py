from __future__ import annotations

from dataclasses import dataclass
from enum import StrEnum

from oracle_eval.oracle.tsmorph import MODULE_SCOPE, TsExtraction
from oracle_eval.paths import is_test_file


class EdgeKind(StrEnum):
    FREE = "free"
    METHOD = "method"
    STATIC = "static"
    THIS = "this"
    SUPER = "super"
    NEW = "new"
    HOOK = "hook"
    CALLABLE_REF = "callable_ref"


@dataclass(frozen=True, slots=True)
class Edge:
    file: str
    caller: str
    callee: str
    kind: EdgeKind
    receiver: str | None
    line: int
    external: bool = False
    lines: tuple[int, ...] = ()

    @property
    def key(self) -> tuple[str, str, str]:
        return (self.file, self.caller, self.callee)

    @property
    def call_lines(self) -> tuple[int, ...]:
        return self.lines or (self.line,)

    @property
    def is_module_scope(self) -> bool:
        return self.caller == MODULE_SCOPE

    def render(self) -> str:
        return f"{self.caller} -> {self.callee}"


def build_oracle(
    extraction: TsExtraction,
    *,
    include_tests: bool = False,
) -> list[Edge]:
    edges: dict[tuple[str, str, str], Edge] = {}

    for source in (extraction.callable_refs, extraction.calls):
        for call in source:
            if not include_tests and is_test_file(call.file):
                continue
            key = (call.file, call.caller, call.callee_text)
            previous = edges.get(key)
            supersedes = (
                previous is not None
                and previous.kind is EdgeKind.CALLABLE_REF
                and call.kind != EdgeKind.CALLABLE_REF
            )
            keep = () if previous is None or supersedes else previous.lines
            edges[key] = Edge(
                file=call.file,
                caller=call.caller,
                callee=call.callee_text,
                kind=EdgeKind(call.kind),
                receiver=call.receiver,
                line=call.line,
                external=call.is_external,
                lines=(*keep, call.line),
            )

    return sorted(edges.values(), key=lambda e: (e.file, e.line, e.callee))


def primary_edges(edges: list[Edge]) -> list[Edge]:
    return [e for e in edges if not e.is_module_scope]
