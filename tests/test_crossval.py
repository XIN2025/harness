from pathlib import Path

import pytest

from oracle_eval.oracle.crossval import (
    cross_validate,
    scip_vocabulary,
    tsmorph_name_edges,
)
from oracle_eval.oracle.projection import CallEdge, ScopeKind, project_index
from oracle_eval.oracle.tsmorph import TsCall, TsExtraction, load_tsmorph
from oracle_eval.scip.load import load_index

DATA = Path(__file__).parent.parent / "data" / "oracle" / "remeda"
INDEX_PATH = DATA / "index.jsonl"
TSMORPH_PATH = DATA / "tsmorph.jsonl"

requires_data = pytest.mark.skipif(
    not (INDEX_PATH.exists() and TSMORPH_PATH.exists()),
    reason="build the oracle first, see README",
)

PKG = "scip-typescript npm remeda 2.0.0 src/`add.ts`/"


def scip_edge(
    caller: str,
    callee: str,
    *,
    kind: ScopeKind = ScopeKind.FUNCTION,
    file: str = "src/add.ts",
    in_repo: bool = True,
    test: bool = False,
) -> CallEdge:
    return CallEdge(
        caller=f"{PKG}{caller}().",
        callee=f"{PKG}{callee}.",
        file=file,
        line=1,
        caller_kind=kind,
        callee_package="remeda" if in_repo else "typescript",
        in_repo=in_repo,
        is_test_file=test,
    )


def ts_call(
    caller: str,
    callee: str,
    *,
    file: str = "src/add.ts",
    kind: str = "free",
    receiver: str | None = None,
) -> TsCall:
    return TsCall(
        file=file,
        caller=caller,
        callee_text=callee,
        kind=kind,
        receiver=receiver,
        callee_file_hint=None,
        line=1,
    )


def extraction(*calls: TsCall) -> TsExtraction:
    return TsExtraction(calls=list(calls), definitions={}, line_counts={}, failures={})


def test_receiver_calls_are_excluded_from_the_tsmorph_side() -> None:
    calls = extraction(
        ts_call("f", "entries"),
        ts_call("f", "entries", kind="method", receiver="Object"),
    )
    assert tsmorph_name_edges(calls) == {("src/add.ts", "f", "entries")}


def test_vocabulary_comes_from_scip_not_from_tsmorph_definitions() -> None:
    assert scip_vocabulary([scip_edge("add", "purry")]) == {"purry"}


@requires_data
def test_remeda_crossval_figures_are_pinned() -> None:
    edges = project_index(load_index(INDEX_PATH), "remeda")
    report = cross_validate(edges, load_tsmorph(TSMORPH_PATH))

    assert len(report.both) == 195
    assert len(report.scip_only) == 144
    assert len(report.tsmorph_only) == 14
    assert report.scip_recall_of_tsmorph == pytest.approx(0.933, abs=0.001)
    assert report.agreement == pytest.approx(0.552, abs=0.001)
