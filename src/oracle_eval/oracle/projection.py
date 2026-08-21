from __future__ import annotations

from dataclasses import dataclass
from enum import StrEnum

from oracle_eval.paths import is_test_file
from oracle_eval.scip.model import Document, Index, Occurrence, Range
from oracle_eval.scip.symbols import (
    descriptor_suffix,
    is_local,
    is_value_symbol,
    package_name,
    short_name,
)


class ScopeKind(StrEnum):
    FUNCTION = "function"
    VALUE = "value"
    TYPE = "type"
    MODULE = "module"


@dataclass(frozen=True, slots=True)
class Scope:
    symbol: str
    kind: ScopeKind
    range: Range


@dataclass(frozen=True, slots=True)
class CallEdge:
    caller: str
    callee: str
    file: str
    line: int
    caller_kind: ScopeKind
    callee_package: str
    in_repo: bool
    is_test_file: bool

    @property
    def key(self) -> tuple[str, str, str]:
        return (self.caller, self.callee, self.file)

    @property
    def counts_toward_primary(self) -> bool:
        return self.caller_kind is ScopeKind.FUNCTION and self.in_repo and not self.is_test_file

    def render(self) -> str:
        return f"{short_name(self.caller)} -> {short_name(self.callee)}"


def _scope_kind(symbol: str, callable_symbols: frozenset[str]) -> ScopeKind:
    match descriptor_suffix(symbol):
        case "().":
            return ScopeKind.FUNCTION
        case "/":
            return ScopeKind.MODULE
        case "#":
            return ScopeKind.TYPE
        case ".":
            return ScopeKind.FUNCTION if symbol in callable_symbols else ScopeKind.VALUE
        case _:
            return ScopeKind.VALUE


def scopes_of(doc: Document, callable_symbols: frozenset[str]) -> list[Scope]:
    return [
        Scope(
            symbol=occ.symbol,
            kind=_scope_kind(occ.symbol, callable_symbols),
            range=occ.enclosing_range,
        )
        for occ in doc.occurrences
        if occ.is_definition and occ.enclosing_range is not None
    ]


def innermost_scope(scopes: list[Scope], line: int) -> Scope | None:
    best: Scope | None = None
    for scope in scopes:
        if not scope.range.contains_line(line):
            continue
        if best is None or scope.range.span < best.range.span:
            best = scope
    return best


def _is_callee(occ: Occurrence, callable_symbols: frozenset[str]) -> bool:
    if occ.is_definition:
        return False
    if is_local(occ.symbol):
        return False
    if not is_value_symbol(occ.symbol):
        return False
    return occ.symbol in callable_symbols


def project_document(
    doc: Document,
    callable_symbols: frozenset[str],
    project_package: str,
) -> list[CallEdge]:
    scopes = scopes_of(doc, callable_symbols)
    module_symbol = doc.module_symbol
    test_file = is_test_file(doc.relative_path)

    seen: dict[tuple[str, str, str], CallEdge] = {}
    for occ in doc.occurrences:
        if not _is_callee(occ, callable_symbols):
            continue

        scope = innermost_scope(scopes, occ.range.start_line)
        if scope is None:
            if module_symbol is None:
                continue
            caller, caller_kind = module_symbol, ScopeKind.MODULE
        else:
            caller, caller_kind = scope.symbol, scope.kind

        edge = CallEdge(
            caller=caller,
            callee=occ.symbol,
            file=doc.relative_path,
            line=occ.range.start_line,
            caller_kind=caller_kind,
            callee_package=package_name(occ.symbol),
            in_repo=package_name(occ.symbol) == project_package,
            is_test_file=test_file,
        )
        seen.setdefault(edge.key, edge)

    return list(seen.values())


def project_index(index: Index, project_package: str) -> list[CallEdge]:
    callable_symbols = frozenset(index.callable_symbols())
    edges: list[CallEdge] = []
    for doc in index.documents:
        edges.extend(project_document(doc, callable_symbols, project_package))
    return edges
