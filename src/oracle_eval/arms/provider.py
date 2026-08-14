from __future__ import annotations

import os
from dataclasses import dataclass
from functools import cache
from typing import TYPE_CHECKING, Any

if TYPE_CHECKING:
    from openai import OpenAI

TEMPERATURE = 0.0

MAX_TOKENS = 8192

REQUEST_TIMEOUT_SECONDS = 300.0


@dataclass(frozen=True, slots=True)
class Provider:
    name: str
    base_url: str
    api_key_env: str
    signup: str

    keyless: bool = False

    @property
    def api_key(self) -> str | None:
        if self.keyless:
            return "local"
        return os.environ.get(self.api_key_env) or None


GROQ = Provider(
    name="groq",
    base_url="https://api.groq.com/openai/v1",
    api_key_env="GROQ_API_KEY",
    signup="https://console.groq.com",
)

GEMINI = Provider(
    name="gemini",
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
    api_key_env="GEMINI_API_KEY",
    signup="https://aistudio.google.com",
)

OPENROUTER = Provider(
    name="openrouter",
    base_url="https://openrouter.ai/api/v1",
    api_key_env="OPENROUTER_API_KEY",
    signup="https://openrouter.ai/settings/keys",
)

LOCAL = Provider(
    name="local",
    base_url="http://localhost:11434/v1",
    api_key_env="OLLAMA_API_KEY",
    signup="https://ollama.com/download",
    keyless=True,
)

PROVIDERS = {p.name: p for p in (GROQ, GEMINI, OPENROUTER, LOCAL)}


@dataclass(frozen=True, slots=True)
class Arm:
    name: str
    provider: Provider
    model: str
    prompt_version: str
    max_tokens: int = MAX_TOKENS
    json_mode: bool = False


ENV_FILES = (".env.local", ".env")


def load_env(paths: tuple[str, ...] = ENV_FILES) -> None:
    from dotenv import load_dotenv

    for path in paths:
        load_dotenv(path, override=False)


@cache
def client_for(provider: Provider) -> OpenAI:
    from openai import OpenAI

    key = provider.api_key
    if key is None:
        raise RuntimeError(
            f"{provider.api_key_env} is not set. Copy .env.example to .env.local (or .env) "
            f"and paste a key from {provider.signup}. Keys belong in that file, nowhere else."
        )
    return OpenAI(api_key=key, base_url=provider.base_url, timeout=REQUEST_TIMEOUT_SECONDS)


def list_models(provider: Provider) -> list[str]:
    models = client_for(provider).models.list()
    return sorted(model.id for model in models.data)


@dataclass(frozen=True, slots=True)
class Completion:
    text: str
    finish_reason: str
    served_by: str
    prompt_tokens: int = 0
    completion_tokens: int = 0


TRUNCATION_CHARS_PER_TOKEN = 4.5


def looks_truncated(prompt_chars: int, completion: Completion) -> bool:
    if completion.prompt_tokens <= 0:
        return False
    return prompt_chars / completion.prompt_tokens > TRUNCATION_CHARS_PER_TOKEN


def _is_transient_server_error(error: BaseException) -> bool:
    from openai import APIStatusError

    return isinstance(error, APIStatusError) and 500 <= error.status_code < 600


def complete(arm: Arm, system: str, user: str) -> Completion:
    from openai import APIConnectionError, RateLimitError
    from tenacity import (
        retry,
        retry_if_exception,
        retry_if_exception_type,
        stop_after_attempt,
        wait_exponential,
    )

    client = client_for(arm.provider)

    @retry(
        retry=(
            retry_if_exception_type((RateLimitError, APIConnectionError))
            | retry_if_exception(_is_transient_server_error)
        ),
        wait=wait_exponential(multiplier=2, min=2, max=60),
        stop=stop_after_attempt(6),
        reraise=True,
    )
    def call() -> Any:
        extra: dict[str, Any] = (
            {"response_format": {"type": "json_object"}} if arm.json_mode else {}
        )
        return client.chat.completions.create(
            model=arm.model,
            temperature=TEMPERATURE,
            max_tokens=arm.max_tokens,
            messages=[
                {"role": "system", "content": system},
                {"role": "user", "content": user},
            ],
            **extra,
        )

    completion = call()
    if not completion.choices:
        raise RuntimeError(
            f"{arm.provider.name} returned a response with no choices for model "
            f"{arm.model}. Nothing was generated, so there is no answer to cache."
        )
    choice = completion.choices[0]
    content = choice.message.content
    served_by = getattr(completion, "provider", None)
    usage = completion.usage
    return Completion(
        text=content if isinstance(content, str) else "",
        finish_reason=choice.finish_reason or "unknown",
        served_by=served_by if isinstance(served_by, str) else "",
        prompt_tokens=usage.prompt_tokens if usage else 0,
        completion_tokens=usage.completion_tokens if usage else 0,
    )
