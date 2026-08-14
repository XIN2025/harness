from pathlib import Path

import pytest

from oracle_eval.oracle.build import EdgeKind, build_oracle, primary_edges
from oracle_eval.oracle.tsmorph import MODULE_SCOPE, TsCall, TsExtraction, load_tsmorph

TSMORPH_PATH = Path(__file__).parent.parent / "data" / "oracle" / "remeda" / "tsmorph.jsonl"
requires_data = pytest.mark.skipif(
    not TSMORPH_PATH.exists(), reason="run tools/extract_corpus.ts first"
)


def call(
    caller: str,
    callee: str,
    *,
    file: str = "src/a.ts",
    kind: str = "free",
    line: int = 1,
) -> TsCall:
    return TsCall(
        file=file,
        caller=caller,
        callee_text=callee,
        kind=kind,
        receiver=None,
        callee_file_hint=None,
        line=line,
    )


def extraction(calls: list[TsCall], refs: list[TsCall] | None = None) -> TsExtraction:
    return TsExtraction(
        calls=calls,
        callable_refs=refs or [],
        definitions={},
        line_counts={},
        failures={},
    )


def test_an_invocation_beats_a_callable_reference_for_the_same_edge() -> None:
    edges = build_oracle(
        extraction(
            [call("funnel", "handleBurstEnd", kind=EdgeKind.FREE, line=305)],
            [call("funnel", "handleBurstEnd", kind=EdgeKind.CALLABLE_REF, line=285)],
        )
    )
    assert len(edges) == 1
    assert edges[0].kind == "free"
    assert edges[0].line == 305


def test_edges_are_deduplicated_per_file_caller_callee() -> None:
    edges = build_oracle(extraction([call("f", "purry", line=3), call("f", "purry", line=9)]))
    assert len(edges) == 1


def test_primary_excludes_module_scope() -> None:
    edges = build_oracle(extraction([call("f", "purry"), call(MODULE_SCOPE, "Symbol")]))
    assert len(edges) == 2
    assert [e.caller for e in primary_edges(edges)] == ["f"]


@requires_data
def test_remeda_oracle_figures_are_pinned() -> None:
    edges = build_oracle(load_tsmorph(TSMORPH_PATH))
    assert len(edges) == 712
    assert len(primary_edges(edges)) == 686


@requires_data
def test_callable_refs_recover_the_two_deferred_edges_in_funnel() -> None:
    edges = build_oracle(load_tsmorph(TSMORPH_PATH))
    funnel = {e.callee for e in edges if e.file.endswith("src/funnel.ts")}
    assert {"handleIntervalEnd", "handleBurstEnd", "voidReducer"} <= funnel


@requires_data
def test_object_literal_keys_are_not_edges() -> None:
    edges = build_oracle(load_tsmorph(TSMORPH_PATH))
    funnel = {e.callee for e in edges if e.file.endswith("src/funnel.ts")}
    assert not ({"call", "cancel", "flush"} & funnel)


@requires_data
def test_imports_are_not_edges() -> None:
    edges = build_oracle(load_tsmorph(TSMORPH_PATH))
    add = [e for e in edges if e.file.endswith("src/add.ts")]
    assert all(e.caller != MODULE_SCOPE for e in add)
