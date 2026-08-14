import pytest

from oracle_eval.arms.treesitter import Bucket, extract_file
from oracle_eval.oracle.tsmorph import MODULE_SCOPE

pytest.importorskip("tree_sitter", reason="the `arms` extra is not installed")


def calls(source: str, *, tsx: bool = False) -> set[tuple[str, str, str]]:
    result = extract_file(source, tsx=tsx)
    assert result.parse_errors == 0, "the fixture does not parse; the test measures nothing"
    return {(c.caller, c.callee_text, c.kind) for c in result.calls}


def skipped(source: str, *, tsx: bool = False) -> set[tuple[Bucket, str | None]]:
    return {(s.bucket, s.callee_text) for s in extract_file(source, tsx=tsx).skipped}


def test_a_call_inside_a_closure_is_attributed_to_the_outermost_function() -> None:
    source = """
    function funnel() {
      const invoke = () => { log(1); };
      return invoke;
    }
    """
    assert calls(source) == {("funnel", "log", "free")}


def test_a_call_outside_every_function_belongs_to_module_scope() -> None:
    assert calls("const ready = boot();") == {(MODULE_SCOPE, "boot", "free")}


def test_an_anonymous_function_takes_the_name_it_is_declared_under() -> None:
    assert calls("const f = function g() { helper(); };") == {("f", "helper", "free")}


@pytest.mark.parametrize(
    ("expression", "expected"),
    [
        ("free()", ("free", "free")),
        ("obj.method()", ("method", "method")),
        ("Math.min(1)", ("min", "static")),
        ("this.handler()", ("handler", "this")),
        ("new Widget()", ("Widget", "new")),
        ("useState(0)", ("useState", "hook")),
    ],
)
def test_the_callee_and_its_kind(expression: str, expected: tuple[str, str]) -> None:
    callee, kind = expected
    assert calls(f"function f() {{ {expression}; }}") == {("f", callee, kind)}


def test_a_receiver_beginning_super_classifies_as_super() -> None:
    assert calls("function f() { superman.fly(); }") == {("f", "fly", "super")}


def test_a_tagged_template_is_skipped_rather_than_claimed() -> None:
    source = "function f() { sql`select 1`; }"
    assert calls(source) == set()
    assert skipped(source) == {(Bucket.TAGGED_TEMPLATE, "sql")}


def test_a_bare_decorator_is_skipped_but_a_called_one_is_reached_normally() -> None:
    source = """
    class C {
      @Bare
      @Called()
      method() {}
    }
    """
    assert calls(source) == {(MODULE_SCOPE, "Called", "free")}
    assert skipped(source) == {(Bucket.BARE_DECORATOR, "Bare")}


def test_a_jsx_component_is_skipped_and_a_host_element_is_not_an_invocation() -> None:
    source = "function App() { return <><Foo /><div /></>; }"
    assert skipped(source, tsx=True) == {(Bucket.JSX_COMPONENT, "Foo")}


def test_a_computed_callee_with_a_literal_index_is_named_but_not_claimed() -> None:
    assert skipped('function f() { handlers["run"](); }') == {(Bucket.COMPUTED_LITERAL, "run")}
    assert skipped("function f() { handlers[k](); }") == {(Bucket.RESIDUE, None)}
