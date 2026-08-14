from oracle_eval.oracle.build import Edge, EdgeKind
from oracle_eval.oracle.tsmorph import FunctionScope
from oracle_eval.predict.schema import PredictedCall, Prediction
from oracle_eval.score.match import (
    OracleCut,
    alias_index,
    key_of,
    normalise,
    score_file,
)


def oracle_edge(
    caller: str,
    callee: str,
    *,
    kind: str = "free",
    file: str = "src/a.ts",
    external: bool = False,
    lines: tuple[int, ...] = (),
) -> Edge:
    return Edge(
        file=file,
        caller=caller,
        callee=callee,
        kind=EdgeKind(kind),
        receiver=None,
        line=lines[0] if lines else 1,
        external=external,
        lines=lines,
    )


def predict(*pairs: tuple[str, str]) -> Prediction:
    return Prediction(
        calls=[PredictedCall(caller=caller, callee_text=callee) for caller, callee in pairs]
    )


def test_member_access_reduces_to_the_trailing_segment() -> None:
    assert normalise("Math.min") == "min"
    assert normalise("Math.min()") == "min"
    assert normalise("min") == "min"
    assert normalise("a.b.c.deeply") == "deeply"


def test_call_generic_and_index_suffixes_are_dropped() -> None:
    assert normalise("purry(fn, args)") == "purry"
    assert normalise("identity<string>") == "identity"
    assert normalise("handlers[0]") == "handlers"


def test_casing_is_not_folded() -> None:
    assert normalise("Error") != normalise("error")
    assert key_of("src/a.ts", "f", "Error") != key_of("src/a.ts", "f", "error")


def test_calls_only_drops_callable_refs_and_full_keeps_them() -> None:
    edges = [oracle_edge("add", "purry"), oracle_edge("add", "addImpl", kind="callable_ref")]
    assert len(OracleCut.CALLS_ONLY.partition_edges(edges)[0]) == 1
    assert len(OracleCut.FULL.partition_edges(edges)[0]) == 2


def test_an_arm_is_not_charged_for_the_class_its_prompt_never_asked_about() -> None:
    edges = [oracle_edge("add", "purry"), oracle_edge("add", "addImpl", kind="callable_ref")]
    perfect_under_their_prompt = predict(("add", "purry"))

    assert score_file("src/a.ts", edges, perfect_under_their_prompt).fn == 0
    assert score_file("src/a.ts", edges, perfect_under_their_prompt, OracleCut.FULL).fn == 1


def test_hits_misses_and_false_positives_are_partitioned() -> None:
    edges = [oracle_edge("f", "purry"), oracle_edge("f", "isArray")]
    score = score_file("src/a.ts", edges, predict(("f", "purry"), ("f", "invented")))

    assert score.tp == 1
    assert score.fp == 1
    assert score.fn == 1
    assert score.truth == 2


def test_the_model_does_not_get_to_choose_which_file_it_answered_about() -> None:
    prediction = Prediction(
        relative_path="totally/elsewhere.ts",
        calls=[PredictedCall(caller="f", callee_text="purry")],
    )
    assert score_file("src/a.ts", [oracle_edge("f", "purry")], prediction).tp == 1


def test_duplicate_predictions_do_not_multiply_credit() -> None:
    prediction = predict(("f", "purry"), ("f", "Math.purry"), ("f", "purry()"))
    score = score_file("src/a.ts", [oracle_edge("f", "purry")], prediction)
    assert (score.tp, score.fp) == (1, 0)


FUNNEL_SCOPES = [
    FunctionScope(name="funnel", start_line=1, end_line=50),
    FunctionScope(name="invoke", start_line=10, end_line=20),
    FunctionScope(name="isIdle", start_line=30, end_line=34),
    FunctionScope(name="flush", start_line=40, end_line=45),
]


def test_a_caller_containing_the_call_site_is_accepted() -> None:
    edges = [oracle_edge("funnel", "log", lines=(12,))]
    aliases = alias_index(edges, FUNNEL_SCOPES)

    assert score_file("src/a.ts", edges, predict(("invoke", "log")), aliases=aliases).tp == 1
    assert score_file("src/a.ts", edges, predict(("funnel", "log")), aliases=aliases).tp == 1


def test_a_closure_that_contains_no_call_site_is_not_accepted() -> None:
    edges = [oracle_edge("funnel", "log", lines=(12,))]
    aliases = alias_index(edges, FUNNEL_SCOPES)
    score = score_file("src/a.ts", edges, predict(("isIdle", "log")), aliases=aliases)

    assert (score.tp, score.fp) == (0, 1)


def test_every_call_site_of_a_multi_site_edge_is_accepted() -> None:
    edges = [oracle_edge("funnel", "clearTimeout", lines=(12, 42))]
    aliases = alias_index(edges, FUNNEL_SCOPES)

    def blame(caller: str) -> tuple[int, int]:
        score = score_file("src/a.ts", edges, predict((caller, "clearTimeout")), aliases=aliases)
        return score.tp, score.fp

    assert blame("invoke") == (1, 0)
    assert blame("flush") == (1, 0)
    assert blame("funnel") == (1, 0)
    assert blame("isIdle") == (0, 1)


def test_an_excluded_class_is_charged_to_neither_side() -> None:
    edges = [oracle_edge("f", "purry"), oracle_edge("f", "floor", external=True)]
    score = score_file("src/a.ts", edges, predict(("f", "purry"), ("f", "Math.floor")))

    assert (score.tp, score.fp, score.fn) == (1, 0, 0)
    assert len(score.unscored) == 1


def test_a_module_scope_prediction_neither_helps_nor_hurts() -> None:
    edges = [oracle_edge("f", "purry")]
    score = score_file("src/a.ts", edges, predict(("f", "purry"), ("__module__", "invariant")))

    assert (score.tp, score.fp, score.fn) == (1, 0, 0)
    assert len(score.unscored) == 1
