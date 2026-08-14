from __future__ import annotations

import re
from collections.abc import Iterable, Mapping
from collections.abc import Set as AbstractSet
from dataclasses import dataclass
from enum import StrEnum
from types import MappingProxyType

from oracle_eval.oracle.build import Edge, EdgeKind
from oracle_eval.oracle.tsmorph import MODULE_SCOPE, FunctionScope
from oracle_eval.predict.schema import PredictedCall, Prediction

EdgeKey = tuple[str, str, str]

Aliases = Mapping[EdgeKey, EdgeKey]

NO_ALIASES: Aliases = MappingProxyType({})

_SUFFIX = re.compile(r"[(<\[].*$", re.DOTALL)
_QUOTES = "\"'`"


class OracleCut(StrEnum):
    CALLS_ONLY = "calls_only"
    FULL = "full"

    def scores(self, edge: Edge) -> bool:
        if edge.external or edge.is_module_scope:
            return False
        return self is OracleCut.FULL or edge.kind is not EdgeKind.CALLABLE_REF

    @property
    def reads_callable_refs(self) -> bool:
        return self is OracleCut.FULL

    def partition_edges(self, edges: Iterable[Edge]) -> tuple[dict[EdgeKey, Edge], set[EdgeKey]]:
        truth: dict[EdgeKey, Edge] = {}
        excluded: set[EdgeKey] = set()
        for edge in edges:
            key = key_of(edge.file, edge.caller, edge.callee)
            if self.scores(edge):
                truth.setdefault(key, edge)
            else:
                excluded.add(key)
        return truth, excluded - truth.keys()


def normalise(text: str) -> str:
    cleaned = _SUFFIX.sub("", text.strip()).strip().strip(_QUOTES)
    cleaned = cleaned.replace("?.", ".")
    return cleaned.rsplit(".", 1)[-1].strip()


def key_of(file: str, caller: str, callee: str) -> EdgeKey:
    return (file.replace("\\", "/"), normalise(caller), normalise(callee))


def alias_index(edges: Iterable[Edge], scopes: Iterable[FunctionScope]) -> Aliases:
    ranges: dict[str, FunctionScope] = {}
    duplicated: set[str] = set()
    for scope in scopes:
        name = normalise(scope.name)
        if name in ranges:
            duplicated.add(name)
        ranges[name] = scope
    for name in duplicated:
        del ranges[name]

    truth = {key_of(e.file, e.caller, e.callee) for e in edges}
    index: dict[EdgeKey, EdgeKey] = {}
    contested: set[EdgeKey] = set()

    for edge in edges:
        key = key_of(edge.file, edge.caller, edge.callee)
        outer = ranges.get(key[1])
        if outer is None:
            continue
        for name, scope in ranges.items():
            if name == key[1] or not scope.within(outer):
                continue
            if not any(scope.contains(line) for line in edge.call_lines):
                continue
            alias = (key[0], name, key[2])
            if alias in truth:
                continue
            if index.get(alias, key) != key:
                contested.add(alias)
            index[alias] = key

    for alias in contested:
        del index[alias]
    return index


def predicted_keys(
    file: str,
    prediction: Prediction,
    cut: OracleCut = OracleCut.CALLS_ONLY,
    aliases: Aliases = NO_ALIASES,
) -> dict[EdgeKey, PredictedCall]:
    calls = prediction.all_calls if cut.reads_callable_refs else prediction.calls
    indexed: dict[EdgeKey, PredictedCall] = {}
    for call in calls:
        key = key_of(file, call.caller, call.callee_text)
        indexed.setdefault(aliases.get(key, key), call)
    return indexed


@dataclass(frozen=True, slots=True)
class FileScore:
    path: str
    matched: tuple[EdgeKey, ...]
    spurious: tuple[EdgeKey, ...]
    missed: tuple[EdgeKey, ...]
    unscored: tuple[EdgeKey, ...] = ()

    @property
    def tp(self) -> int:
        return len(self.matched)

    @property
    def fp(self) -> int:
        return len(self.spurious)

    @property
    def fn(self) -> int:
        return len(self.missed)

    @property
    def truth(self) -> int:
        return self.tp + self.fn


def classify(
    path: str,
    predicted: AbstractSet[EdgeKey],
    edges: list[Edge],
    cut: OracleCut,
) -> FileScore:
    truth, excluded = cut.partition_edges(edges)
    wrong = predicted - truth.keys()
    unscored = {key for key in wrong if key in excluded or key[1] == MODULE_SCOPE}

    return FileScore(
        path=path,
        matched=tuple(sorted(truth.keys() & predicted)),
        spurious=tuple(sorted(wrong - unscored)),
        missed=tuple(sorted(truth.keys() - predicted)),
        unscored=tuple(sorted(unscored)),
    )


def score_file(
    path: str,
    edges: list[Edge],
    prediction: Prediction,
    cut: OracleCut = OracleCut.CALLS_ONLY,
    aliases: Aliases = NO_ALIASES,
) -> FileScore:
    guess = predicted_keys(path, prediction, cut, aliases)
    return classify(path, guess.keys(), edges, cut)


def render_key(key: EdgeKey) -> str:
    _, caller, callee = key
    return f"{caller} -> {callee}"
