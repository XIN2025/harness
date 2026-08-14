from __future__ import annotations

import re
from enum import IntFlag
from typing import Final

LOCAL_PREFIX: Final = "local "

VALUE_SUFFIXES: Final = frozenset({".", "()."})


class SymbolRole(IntFlag):
    REFERENCE = 0
    DEFINITION = 1
    IMPORT = 2
    WRITE_ACCESS = 4
    READ_ACCESS = 8
    GENERATED = 16
    TEST = 32
    FORWARD_DEFINITION = 64


def is_local(symbol: str) -> bool:
    return symbol.startswith(LOCAL_PREFIX)


def package_name(symbol: str) -> str:
    if is_local(symbol):
        return "<local>"
    parts = symbol.split(" ", 4)
    return parts[2] if len(parts) >= 3 else "<unknown>"


def descriptor_suffix(symbol: str) -> str:
    if is_local(symbol):
        return "local"
    if symbol.endswith("()."):
        return "()."
    for suffix in ("/", "#", ".", ":", "!"):
        if symbol.endswith(suffix):
            return suffix
    if symbol.endswith(")"):
        return "(param)"
    if symbol.endswith("]"):
        return "[typeparam]"
    return "?"


def is_value_symbol(symbol: str) -> bool:
    return descriptor_suffix(symbol) in VALUE_SUFFIXES


def short_name(symbol: str) -> str:
    if is_local(symbol):
        return symbol
    tail = symbol.split(" ", 4)[-1] if " " in symbol else symbol
    tail = tail.rstrip()
    for suffix in ("().", "/", "#", ".", ":", "!"):
        if tail.endswith(suffix):
            tail = tail[: -len(suffix)]
            break
    if "`" in tail:
        tail = tail.rsplit("`", 1)[-1]
    tail = tail.lstrip("/")
    for sep in ("/", "#", ":", "."):
        if sep in tail:
            tail = tail.rsplit(sep, 1)[-1]
    if tail:
        return tail
    path = file_path_of(symbol)
    return path.rsplit("/", 1)[-1] if path else symbol


def file_path_of(symbol: str) -> str | None:
    if is_local(symbol):
        return None
    match = re.search(r"([\w./\-@]*)`([^`]+)`", symbol)
    if match is None:
        return None
    return f"{match.group(1)}{match.group(2)}"


_FENCE: Final = re.compile(r"^```ts\n(?P<body>.*?)\n?```$", re.DOTALL)
_NON_CALLABLE_LEAD: Final = re.compile(r"^\s*(type|interface|enum|namespace|module)\s")
_FUNCTION_LEAD: Final = re.compile(r"^\s*(export\s+)?(async\s+)?function\b")
_METHOD_LEAD: Final = re.compile(r"^\s*\((method|getter|setter)\)")
_ARROW_TYPE: Final = re.compile(r":\s*[^=]*=>")


def signature_of(documentation: list[str] | None) -> str:
    if not documentation:
        return ""
    match = _FENCE.match(documentation[0].strip())
    return (match.group("body") if match else documentation[0]).strip()


def is_callable_signature(signature: str) -> bool:
    if not signature:
        return False
    if _NON_CALLABLE_LEAD.match(signature):
        return False
    if _FUNCTION_LEAD.match(signature) or _METHOD_LEAD.match(signature):
        return True
    return bool(_ARROW_TYPE.search(signature))
