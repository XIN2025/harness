from __future__ import annotations

import hashlib
import json
import os
import tempfile
from dataclasses import asdict, dataclass, fields
from datetime import UTC, datetime
from pathlib import Path

CACHE_ROOT = Path("data/cache")


def cache_key(model: str, prompt_version: str, file_sha: str, max_tokens: int) -> str:
    payload = "\x00".join((model, prompt_version, file_sha, str(max_tokens)))
    return hashlib.sha256(payload.encode("utf8")).hexdigest()


@dataclass(frozen=True, slots=True)
class CachedResponse:
    key: str
    model: str
    prompt_version: str
    file_sha: str
    relative_path: str
    response: str
    created: str
    finish_reason: str = "unknown"
    served_by: str = ""
    prompt_tokens: int = 0
    completion_tokens: int = 0

    @property
    def is_empty(self) -> bool:
        return self.response == ""

    @property
    def is_truncated(self) -> bool:
        return self.finish_reason == "length"


def _write_atomic(path: Path, text: str) -> None:
    """Write via a temp file, then rename over the target.

    A content-addressed key is never recomputed, so a partial write is permanent.
    """
    directory = path.parent
    handle, temporary = tempfile.mkstemp(dir=directory, prefix=f".{path.name}.", suffix=".tmp")
    try:
        with os.fdopen(handle, "w", encoding="utf8") as stream:
            stream.write(text)
            stream.flush()
            os.fsync(stream.fileno())
        os.replace(temporary, path)
    except BaseException:
        Path(temporary).unlink(missing_ok=True)
        raise


class ResponseCache:
    def __init__(self, root: Path = CACHE_ROOT) -> None:
        self.root = root

    def path_for(self, key: str) -> Path:
        return self.root / key[:2] / f"{key}.json"

    def get(self, key: str) -> CachedResponse | None:
        path = self.path_for(key)
        if not path.exists():
            return None
        try:
            raw = json.loads(path.read_text(encoding="utf8"))
        except (json.JSONDecodeError, UnicodeDecodeError):
            return None
        if not isinstance(raw, dict):
            return None
        known = {f.name for f in fields(CachedResponse)}
        try:
            return CachedResponse(**{k: v for k, v in raw.items() if k in known})
        except TypeError:
            return None

    def put(
        self,
        *,
        key: str,
        model: str,
        prompt_version: str,
        file_sha: str,
        relative_path: str,
        response: str,
        finish_reason: str = "unknown",
        served_by: str = "",
        prompt_tokens: int = 0,
        completion_tokens: int = 0,
    ) -> CachedResponse:
        existing = self.get(key)
        if existing is not None:
            return existing

        entry = CachedResponse(
            key=key,
            model=model,
            prompt_version=prompt_version,
            file_sha=file_sha,
            relative_path=relative_path,
            response=response,
            created=datetime.now(UTC).isoformat(timespec="seconds"),
            finish_reason=finish_reason,
            served_by=served_by,
            prompt_tokens=prompt_tokens,
            completion_tokens=completion_tokens,
        )
        path = self.path_for(key)
        path.parent.mkdir(parents=True, exist_ok=True)
        _write_atomic(path, json.dumps(asdict(entry), indent=2))
        return entry
