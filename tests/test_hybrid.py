import pytest

from oracle_eval.oracle.build import Edge, EdgeKind
from oracle_eval.predict.schema import PredictedCall, Prediction
from oracle_eval.score.hybrid import score_union_file
from oracle_eval.score.match import EdgeKey, OracleCut

PATH = "src/a.ts"


def oracle_edge(caller: str, callee: str, *, kind: str = "free") -> Edge:
    return Edge(file=PATH, caller=caller, callee=callee, kind=EdgeKind(kind), receiver=None, line=1)


def predict(*pairs: tuple[str, str]) -> Prediction:
    return Prediction(
        calls=[PredictedCall(caller=caller, callee_text=callee) for caller, callee in pairs]
    )


def key(caller: str, callee: str) -> EdgeKey:
    return (PATH, caller, callee)


def test_the_base_arms_edges_are_never_voted_on() -> None:
    edges = [oracle_edge("f", "parsed"), oracle_edge("f", "typed")]
    score = score_union_file(
        PATH,
        edges,
        [predict(("f", "parsed")), predict(("f", "typed")), predict(("f", "typed"))],
        OracleCut.FULL,
        base_count=1,
        require_agreement=True,
    )

    assert score.matched == (key("f", "parsed"), key("f", "typed"))
    assert score.fn == 0


def test_agreement_intersects_the_model_arms_and_a_union_does_not() -> None:
    edges = [oracle_edge("f", "typed", kind="callable_ref")]
    arms = [
        predict(),
        predict(("f", "typed"), ("f", "ghostA")),
        predict(("f", "typed"), ("f", "ghostB")),
    ]

    agreement = score_union_file(
        PATH, edges, arms, OracleCut.FULL, base_count=1, require_agreement=True
    )
    union = score_union_file(PATH, edges, arms, OracleCut.FULL, base_count=1)

    assert (agreement.tp, agreement.fp) == (1, 0)
    assert (union.tp, union.fp) == (1, 2)


def test_combination_happens_after_normalisation() -> None:
    edges = [oracle_edge("f", "min")]
    score = score_union_file(
        PATH,
        edges,
        [predict(), predict(("f", "Math.min")), predict(("f", "min"))],
        OracleCut.FULL,
        base_count=1,
        require_agreement=True,
    )

    assert score.tp == 1


def test_an_arm_with_no_answer_removes_nothing_from_a_union() -> None:
    edges = [oracle_edge("f", "parsed")]
    score = score_union_file(
        PATH,
        edges,
        [predict(("f", "parsed")), Prediction(calls=[])],
        OracleCut.FULL,
        base_count=1,
    )

    assert score.tp == 1


def test_an_arm_with_no_answer_does_veto_under_agreement() -> None:
    edges = [oracle_edge("f", "typed", kind="callable_ref")]
    score = score_union_file(
        PATH,
        edges,
        [predict(), predict(("f", "typed")), Prediction(calls=[])],
        OracleCut.FULL,
        base_count=1,
        require_agreement=True,
    )

    assert (score.tp, score.fn) == (0, 1)


def test_agreement_with_one_model_arm_raises_rather_than_unioning() -> None:
    edges = [oracle_edge("f", "typed", kind="callable_ref")]
    with pytest.raises(ValueError, match="at least two model arms"):
        score_union_file(
            PATH,
            edges,
            [predict(), predict(("f", "typed"))],
            OracleCut.FULL,
            base_count=1,
            require_agreement=True,
        )
