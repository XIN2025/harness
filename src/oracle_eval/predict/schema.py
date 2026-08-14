from __future__ import annotations

from typing import Any

from pydantic import BaseModel, ConfigDict, Field, field_validator, model_validator


class PredictedCall(BaseModel):
    model_config = ConfigDict(extra="ignore", str_strip_whitespace=True)

    caller: str = Field(min_length=1)
    callee_text: str = Field(min_length=1)
    kind: str | None = None
    receiver: str | None = None
    receiver_type_hint: str | None = None
    callee_file_hint: str | None = None
    line: int | None = None


class Prediction(BaseModel):
    model_config = ConfigDict(extra="ignore")

    calls: list[PredictedCall] = Field(default_factory=list)

    relative_path: str | None = None
    definitions: list[str] = Field(default_factory=list)
    callable_refs: list[PredictedCall] = Field(default_factory=list)

    @model_validator(mode="before")
    @classmethod
    def _must_answer_something(cls, data: Any) -> Any:
        if isinstance(data, dict) and "calls" not in data and "callable_refs" not in data:
            raise ValueError(
                "neither `calls` nor `callable_refs` is present, that is a failure to "
                "answer, not an empty answer"
            )
        return data

    @field_validator("definitions", mode="before")
    @classmethod
    def _names_only(cls, value: Any) -> Any:
        if isinstance(value, list):
            return [v.get("name", "") if isinstance(v, dict) else v for v in value]
        return value

    @property
    def all_calls(self) -> list[PredictedCall]:
        return [*self.calls, *self.callable_refs]
