import pytest

from oracle_eval.oracle.build import Edge, EdgeKind
from oracle_eval.predict.schema import PredictedCall, Prediction
from oracle_eval.score.ensemble import (
    OVERLAP_LIMIT,
    max_overlap,
    pairwise_overlap,
    score_ensemble_file,
)
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


def test_an_edge_needs_the_votes_to_enter() -> None:
    edges = [oracle_edge("f", "purry"), oracle_edge("f", "isArray")]
    score = score_ensemble_file(
        PATH,
        edges,
        [predict(("f", "purry"), ("f", "isArray")), predict(("f", "purry"))],
        OracleCut.CALLS_ONLY,
    )

    assert score.matched == (key("f", "purry"),)
    assert score.missed == (key("f", "isArray"),)


def test_two_arms_naming_one_edge_differently_have_agreed() -> None:
    edges = [oracle_edge("f", "min")]
    score = score_ensemble_file(
        PATH, edges, [predict(("f", "Math.min")), predict(("f", "min"))], OracleCut.CALLS_ONLY
    )

    assert score.tp == 1


def test_one_arm_cannot_reach_quorum_by_repeating_itself() -> None:
    edges = [oracle_edge("f", "purry")]
    loud = predict(("f", "purry"), ("f", "purry"), ("f", "Math.purry"))
    score = score_ensemble_file(PATH, edges, [loud, predict()], OracleCut.CALLS_ONLY)

    assert (score.tp, score.fp, score.fn) == (0, 0, 1)


def test_a_silent_arm_cannot_veto_an_edge_the_others_agree_on() -> None:
    edges = [oracle_edge("f", "purry")]
    score = score_ensemble_file(
        PATH,
        edges,
        [predict(("f", "purry")), predict(("f", "purry")), Prediction(calls=[])],
        OracleCut.CALLS_ONLY,
    )

    assert score.tp == 1


def test_overlap_divides_by_the_smaller_error_set() -> None:
    small = {key("f", f"e{i}") for i in range(2)}
    large = {key("f", f"e{i}") for i in range(10)}
    [(_, _, overlap)] = pairwise_overlap({"a": small, "b": large})

    assert overlap == pytest.approx(1.0)


def test_the_worst_pair_governs() -> None:
    assert max_overlap([("a", "b", 0.1), ("b", "c", 0.9), ("a", "c", 0.2)]) == 0.9
    assert max_overlap([]) == 0.0


def test_the_pre_committed_threshold_is_where_it_was_frozen() -> None:
    assert OVERLAP_LIMIT == 0.80
    assert max_overlap([("qwen-refs-strict", "llama-refs-strict", 0.828)]) > OVERLAP_LIMIT
