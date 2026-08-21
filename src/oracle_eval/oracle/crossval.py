from __future__ import annotations

from collections import Counter
from dataclasses import dataclass, field

from oracle_eval.oracle.projection import CallEdge, ScopeKind
from oracle_eval.oracle.tsmorph import MODULE_SCOPE, TsExtraction
from oracle_eval.paths import is_test_file
from oracle_eval.scip.symbols import short_name

NameEdge = tuple[str, str, str]


def _normalise_file(path: str) -> str:
    return path.replace("\\", "/")


def scip_name_edges(edges: list[CallEdge]) -> set[NameEdge]:
    out: set[NameEdge] = set()
    for e in edges:
        if e.is_test_file or not e.in_repo:
            continue
        if e.caller_kind is ScopeKind.MODULE:
            continue
        out.add((_normalise_file(e.file), short_name(e.caller), short_name(e.callee)))
    return out


def tsmorph_name_edges(extraction: TsExtraction, *, include_tests: bool = False) -> set[NameEdge]:
    return {
        (c.file, c.caller, c.callee_text)
        for c in extraction.calls
        if (include_tests or not is_test_file(c.file))
        and c.caller != MODULE_SCOPE
        and c.kind == "free"
        and c.receiver is None
    }


@dataclass(slots=True)
class CrossValReport:
    in_repo_names: set[str]
    both: set[NameEdge] = field(default_factory=set)
    scip_only: set[NameEdge] = field(default_factory=set)
    tsmorph_only: set[NameEdge] = field(default_factory=set)

    @property
    def agreement(self) -> float:
        union = len(self.both) + len(self.scip_only) + len(self.tsmorph_only)
        return len(self.both) / union if union else 0.0

    @property
    def scip_recall_of_tsmorph(self) -> float:
        denom = len(self.both) + len(self.tsmorph_only)
        return len(self.both) / denom if denom else 0.0

    @property
    def tsmorph_recall_of_scip(self) -> float:
        denom = len(self.both) + len(self.scip_only)
        return len(self.both) / denom if denom else 0.0


def scip_vocabulary(scip_edges: list[CallEdge]) -> set[str]:
    return {short_name(e.callee) for e in scip_edges if e.in_repo}


def cross_validate(
    scip_edges: list[CallEdge],
    extraction: TsExtraction,
) -> CrossValReport:
    in_repo_names = scip_vocabulary(scip_edges)

    def comparable(edges: set[NameEdge]) -> set[NameEdge]:
        return {e for e in edges if e[2] in in_repo_names}

    scip = comparable(scip_name_edges(scip_edges))
    ts = comparable(tsmorph_name_edges(extraction))

    return CrossValReport(
        in_repo_names=in_repo_names,
        both=scip & ts,
        scip_only=scip - ts,
        tsmorph_only=ts - scip,
    )


def disagreement_profile(report: CrossValReport, top: int = 10) -> dict[str, list[tuple[str, int]]]:
    return {
        "scip_only_callees": Counter(e[2] for e in report.scip_only).most_common(top),
        "tsmorph_only_callees": Counter(e[2] for e in report.tsmorph_only).most_common(top),
    }
