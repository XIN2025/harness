from __future__ import annotations

from dataclasses import dataclass, field
from typing import Self

from oracle_eval.scip.symbols import (
    SymbolRole,
    is_callable_signature,
    signature_of,
)


@dataclass(frozen=True, slots=True)
class Range:
    start_line: int
    start_char: int
    end_line: int
    end_char: int

    @classmethod
    def from_list(cls, raw: list[int]) -> Self:
        return cls(raw[0], raw[1], raw[2], raw[3])

    def contains_line(self, line: int) -> bool:
        return self.start_line <= line <= self.end_line

    @property
    def span(self) -> int:
        return self.end_line - self.start_line


@dataclass(frozen=True, slots=True)
class Occurrence:
    range: Range
    symbol: str
    roles: int
    enclosing_range: Range | None = None

    @property
    def is_definition(self) -> bool:
        return bool(self.roles & SymbolRole.DEFINITION)


@dataclass(frozen=True, slots=True)
class SymbolInfo:
    symbol: str
    documentation: tuple[str, ...] = ()

    @property
    def signature(self) -> str:
        return signature_of(list(self.documentation))

    @property
    def is_callable(self) -> bool:
        return is_callable_signature(self.signature)


@dataclass(slots=True)
class Document:
    relative_path: str
    occurrences: list[Occurrence] = field(default_factory=list)
    symbols: list[SymbolInfo] = field(default_factory=list)

    @property
    def module_symbol(self) -> str | None:
        for occ in self.occurrences:
            if occ.is_definition and occ.symbol.endswith("/"):
                return occ.symbol
        return None


@dataclass(slots=True)
class Index:
    project_root: str
    tool: str
    tool_version: str
    documents: list[Document] = field(default_factory=list)

    def callable_symbols(self) -> set[str]:
        return {info.symbol for doc in self.documents for info in doc.symbols if info.is_callable}
