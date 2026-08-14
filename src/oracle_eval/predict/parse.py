from __future__ import annotations

import json
import re
from dataclasses import dataclass, field
from typing import Any

from pydantic import ValidationError

from oracle_eval.predict.schema import Prediction

_FENCE = re.compile(r"```[a-zA-Z0-9_+-]*[ \t]*\r?\n(.*?)(?:\r?\n)?```", re.DOTALL)


def strip_fence(text: str) -> str:
    match = _FENCE.search(text)
    return match.group(1) if match else text


@dataclass(frozen=True, slots=True)
class ParseResult:
    raw_valid: bool
    parseable: bool
    schema_valid: bool
    prediction: Prediction | None = None
    error: str | None = None


def parse_response(text: str) -> ParseResult:
    raw: Any = None
    raw_valid = False
    try:
        raw = json.loads(text)
        raw_valid = True
    except json.JSONDecodeError:
        try:
            raw = json.loads(strip_fence(text))
        except json.JSONDecodeError as exc:
            return ParseResult(False, False, False, error=f"not JSON: {exc.msg} at char {exc.pos}")

    if not isinstance(raw, dict):
        kind = type(raw).__name__
        return ParseResult(raw_valid, True, False, error=f"top level is {kind}, not an object")

    try:
        prediction = Prediction.model_validate(raw)
    except ValidationError as exc:
        first = exc.errors()[0]
        location = ".".join(str(part) for part in first["loc"]) or "<root>"
        return ParseResult(
            raw_valid, True, False, error=f"{location}: {first['msg']} ({exc.error_count()} total)"
        )

    return ParseResult(raw_valid, True, True, prediction=prediction)


@dataclass(slots=True)
class ValidityReport:
    total: int = 0
    raw_valid: int = 0
    parseable: int = 0
    schema_valid: int = 0
    errors: list[str] = field(default_factory=list)

    def add(self, result: ParseResult) -> None:
        self.total += 1
        self.raw_valid += result.raw_valid
        self.parseable += result.parseable
        self.schema_valid += result.schema_valid
        if result.error:
            self.errors.append(result.error)

    def _rate(self, count: int) -> float:
        return count / self.total if self.total else 0.0

    @property
    def raw_valid_rate(self) -> float:
        return self._rate(self.raw_valid)

    @property
    def parseable_rate(self) -> float:
        return self._rate(self.parseable)

    @property
    def schema_valid_rate(self) -> float:
        return self._rate(self.schema_valid)

    def render(self) -> str:
        return (
            f"raw {self.raw_valid}/{self.total} ({self.raw_valid_rate:.1%})  ·  "
            f"fence-stripped {self.parseable}/{self.total} ({self.parseable_rate:.1%})  ·  "
            f"schema {self.schema_valid}/{self.total} ({self.schema_valid_rate:.1%})"
        )
