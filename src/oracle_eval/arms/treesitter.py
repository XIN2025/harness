from __future__ import annotations

from collections.abc import Sequence
from dataclasses import dataclass, field
from enum import StrEnum
from functools import cache
from pathlib import Path
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from tree_sitter import Node, Tree

from oracle_eval.oracle.tsmorph import MODULE_SCOPE

FUNCTION_LIKE = frozenset(
    {
        "function_declaration",
        "generator_function_declaration",
        "function_expression",
        "generator_function",
        "arrow_function",
        "method_definition",
    }
)

NAMING_PARENT = {
    "variable_declarator": "name",
    "public_field_definition": "name",
    "field_definition": "name",
    "pair": "key",
}

GLOBALS = frozenset(
    {
        "console", "JSON", "Math", "Object", "Array", "Promise", "document",
        "window", "localStorage", "sessionStorage", "fetch", "process", "Date",
        "String", "Number", "Boolean",
    }
)  # fmt: skip

REACT_HOOKS = frozenset(
    {
        "useState", "useEffect", "useMemo", "useRef", "useCallback", "useContext",
        "useReducer", "useLayoutEffect", "useImperativeHandle", "useDebugValue",
        "useTransition", "useDeferredValue", "useId",
    }
)  # fmt: skip


class Bucket(StrEnum):
    TAGGED_TEMPLATE = "tagged_template"
    BARE_DECORATOR = "bare_decorator"
    JSX_COMPONENT = "jsx_component"
    COMPUTED_LITERAL = "computed_literal_callee"
    RESIDUE = "residue"


@dataclass(frozen=True, slots=True)
class Call:
    caller: str
    callee_text: str
    kind: str
    receiver: str | None
    receiver_type_hint: str | None
    callee_file_hint: str | None
    line: int


@dataclass(frozen=True, slots=True)
class Skipped:
    bucket: Bucket
    caller: str
    callee_text: str | None
    line: int
    source_line: str


@dataclass(slots=True)
class FileResult:
    calls: list[Call] = field(default_factory=list)
    skipped: list[Skipped] = field(default_factory=list)
    parse_errors: int = 0


@cache
def _parser(tsx: bool = False) -> object:
    import tree_sitter_typescript as ts_typescript
    from tree_sitter import Language, Parser

    grammar = ts_typescript.language_tsx() if tsx else ts_typescript.language_typescript()
    return Parser(Language(grammar))


def _text(node: Node) -> str:
    return str(node.text.decode("utf8")) if node.text is not None else ""


def _walk(root: Node) -> list[Node]:
    out: list[Node] = []
    cursor = root.walk()
    while True:
        if cursor.node is not None:
            out.append(cursor.node)
        if cursor.goto_first_child() or cursor.goto_next_sibling():
            continue
        while True:
            if not cursor.goto_parent():
                return out
            if cursor.goto_next_sibling():
                break


def _has_body(node: Node) -> bool:
    return node.child_by_field_name("body") is not None


def _class_name(node: Node) -> str | None:
    current = node.parent
    while current is not None:
        if current.type == "class_declaration":
            name = current.child_by_field_name("name")
            return _text(name) if name else None
        if current.type == "class":
            name = current.child_by_field_name("name")
            if name:
                return _text(name)
            parent = current.parent
            if parent is not None and parent.type == "variable_declarator":
                declared = parent.child_by_field_name("name")
                return _text(declared) if declared else None
            return None
        current = current.parent
    return None


def _function_name(node: Node) -> str | None:
    if node.type == "method_definition":
        name = node.child_by_field_name("name")
        return _text(name) if name else None

    if node.type in ("function_declaration", "generator_function_declaration"):
        name = node.child_by_field_name("name")
        return _text(name) if name else None

    parent = node.parent
    if parent is None:
        return None
    field_name = NAMING_PARENT.get(parent.type)
    if field_name is None:
        return None
    named = parent.child_by_field_name(field_name)
    return _text(named) if named else None


def caller_of(node: Node) -> str:
    outermost: Node | None = None
    current = node.parent
    while current is not None:
        if current.type in FUNCTION_LIKE and _has_body(current):
            outermost = current
        current = current.parent

    if outermost is None:
        return MODULE_SCOPE
    name = _function_name(outermost)
    if name is None:
        return MODULE_SCOPE
    cls = _class_name(outermost)
    return f"{cls}.{name}" if cls else name


def _is_pascal_case(text: str) -> bool:
    if "." in text or not text:
        return False
    first = text[0]
    return first.isupper() and first.lower() != first


def _describe(callee: Node) -> tuple[str, str, str | None] | None:
    if callee.type == "identifier":
        return _text(callee), "free", None
    if callee.type == "super":
        return "super", "super", "super"
    if callee.type != "member_expression":
        return None

    prop = callee.child_by_field_name("property")
    obj = callee.child_by_field_name("object")
    if prop is None or prop.type != "property_identifier" or obj is None:
        return None

    name, receiver = _text(prop), _text(obj)
    if receiver == "this" or receiver.startswith("this."):
        return name, "this", receiver
    if receiver.startswith("super"):
        return name, "super", receiver
    if _is_pascal_case(receiver):
        return name, "static", receiver
    return name, "method", receiver


def _trailing_name(node: Node) -> str | None:
    if node.type == "identifier":
        return _text(node)
    if node.type == "member_expression":
        prop = node.child_by_field_name("property")
        return _text(prop) if prop else None
    return None


def _file_hint(
    callee_text: str, receiver: str | None, kind: str, imports: dict[str, str]
) -> str | None:
    if kind in ("this", "super"):
        return None
    if receiver is not None:
        root = receiver.split(".")[0]
        if root in GLOBALS:
            return "external"
        return imports.get(root)
    if callee_text in GLOBALS:
        return "external"
    return imports.get(callee_text)


def _imports(nodes: Sequence[Node]) -> dict[str, str]:
    found: dict[str, str] = {}
    for node in nodes:
        if node.type != "import_statement":
            continue
        source = node.child_by_field_name("source")
        if source is None:
            continue
        specifier = _text(source).strip("\"'`")
        for child in _walk(node):
            if child.type in ("import_specifier", "namespace_import"):
                alias = child.child_by_field_name("alias") or child.child_by_field_name("name")
                if alias is not None:
                    found[_text(alias)] = specifier
            elif child.type == "identifier" and child.parent is not None:
                if child.parent.type == "import_clause":
                    found[_text(child)] = specifier
    return found


def _is_tagged_template(node: Node) -> bool:
    args = node.child_by_field_name("arguments")
    return args is not None and args.type == "template_string"


def extract_file(source: str, *, tsx: bool = False) -> FileResult:
    tree: Tree = _parser(tsx).parse(source.encode("utf8"))  # type: ignore[attr-defined]
    root = tree.root_node
    lines = source.splitlines()
    nodes = _walk(root)
    imports = _imports(nodes)
    result = FileResult()

    def source_line(node: Node) -> str:
        row = node.start_point[0]
        return lines[row].strip() if 0 <= row < len(lines) else ""

    def skip(bucket: Bucket, node: Node, name: str | None) -> None:
        result.skipped.append(
            Skipped(bucket, caller_of(node), name, node.start_point[0] + 1, source_line(node))
        )

    for node in nodes:
        if node.type == "ERROR":
            result.parse_errors += 1
            continue

        if node.type in ("jsx_opening_element", "jsx_self_closing_element"):
            element = node.child_by_field_name("name")
            name = _trailing_name(element) if element else None
            if name and name[:1].isupper():
                skip(Bucket.JSX_COMPONENT, node, name)
            continue

        if node.type == "decorator":
            inner = node.named_children[0] if node.named_children else None
            if inner is not None and inner.type != "call_expression":
                skip(Bucket.BARE_DECORATOR, node, _trailing_name(inner))
            continue

        if node.type == "new_expression":
            constructor = node.child_by_field_name("constructor")
            name = _trailing_name(constructor) if constructor else None
            if name is None:
                skip(Bucket.RESIDUE, node, None)
                continue
            result.calls.append(
                Call(
                    caller=caller_of(node),
                    callee_text=name,
                    kind="new",
                    receiver=None,
                    receiver_type_hint=None,
                    callee_file_hint=_file_hint(name, None, "new", imports),
                    line=node.start_point[0] + 1,
                )
            )
            continue

        if node.type != "call_expression":
            continue

        if _is_tagged_template(node):
            callee = node.child_by_field_name("function")
            skip(Bucket.TAGGED_TEMPLATE, node, _trailing_name(callee) if callee else None)
            continue

        callee = node.child_by_field_name("function")
        if callee is None:
            skip(Bucket.RESIDUE, node, None)
            continue

        described = _describe(callee)
        if described is None:
            bucket, named = Bucket.RESIDUE, None
            if callee.type == "subscript_expression":
                index = callee.child_by_field_name("index")
                if index is not None and index.type == "string":
                    bucket, named = Bucket.COMPUTED_LITERAL, _text(index).strip("\"'`")
            skip(bucket, node, named)
            continue

        callee_text, kind, receiver = described
        result.calls.append(
            Call(
                caller=caller_of(node),
                callee_text=callee_text,
                kind="hook" if callee_text in REACT_HOOKS else kind,
                receiver=receiver,
                receiver_type_hint=None,
                callee_file_hint=_file_hint(callee_text, receiver, kind, imports),
                line=node.start_point[0] + 1,
            )
        )

    return result


def predict_file(path: Path, relative_path: str) -> tuple[dict[str, object], FileResult]:
    result = extract_file(path.read_text(encoding="utf8"), tsx=path.suffix == ".tsx")
    answer: dict[str, object] = {
        "relative_path": relative_path,
        "definitions": [],
        "calls": [
            {
                "caller": call.caller,
                "callee_text": call.callee_text,
                "kind": call.kind,
                "receiver": call.receiver,
                "receiver_type_hint": call.receiver_type_hint,
                "callee_file_hint": call.callee_file_hint,
                "line": call.line,
            }
            for call in result.calls
            if call.caller and call.callee_text
        ],
        "callable_refs": [],
    }
    return answer, result
