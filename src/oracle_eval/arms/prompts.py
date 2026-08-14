from __future__ import annotations

import hashlib
import re
from dataclasses import dataclass
from functools import cache
from pathlib import Path
from typing import Any

THEIRS = Path("../slm/reference/cassini-prompts/javascript.yaml")
OURS = Path("../slm/prompts/typescript.yaml")

_BLOCK = re.compile(r"^(?P<key>[a-z_]+):\s*\|\s*$")
_SCALAR = re.compile(r'^(?P<key>[a-z_]+):\s*"(?P<value>[^"]*)"\s*$')


def _read_yaml_fields(path: Path) -> dict[str, str]:
    if not path.exists():
        raise FileNotFoundError(
            f"prompt file not found: {path}\n"
            "Prompt templates are not part of this repository. They are only needed to "
            "run an arm against a live model; every scoring command reads stored "
            "responses from data/predictions and does not touch them."
        )
    fields: dict[str, str] = {}
    lines = path.read_text(encoding="utf8").splitlines()
    index = 0
    while index < len(lines):
        line = lines[index]
        block = _BLOCK.match(line)
        if block:
            body: list[str] = []
            index += 1
            while index < len(lines):
                if lines[index].strip() and not lines[index].startswith("  "):
                    break
                body.append(lines[index][2:])
                index += 1
            fields[block.group("key")] = "\n".join(body).rstrip() + "\n"
            continue
        scalar = _SCALAR.match(line)
        if scalar:
            fields[scalar.group("key")] = scalar.group("value")
        index += 1
    return fields


@dataclass(frozen=True, slots=True)
class Prompt:
    name: str
    template: str
    declared_version: str

    @property
    def version(self) -> str:
        digest = hashlib.sha256(self.template.encode("utf8")).hexdigest()[:12]
        return f"{self.name}-{self.declared_version}-{digest}"

    def render(self, relative_path: str, source: str) -> str:
        if "CONTENT_PLACEHOLDER" in self.template:
            return self.template.replace("FILEPATH_PLACEHOLDER", relative_path).replace(
                "CONTENT_PLACEHOLDER", source
            )
        return self.template.replace("{path}", relative_path).replace("{source}", source)


@cache
def load_prompts() -> dict[str, Prompt]:
    theirs: dict[str, Any] = _read_yaml_fields(THEIRS)
    ours: dict[str, Any] = _read_yaml_fields(OURS)
    version = ours.get("version", "?")
    return {
        "theirs": Prompt("theirs", theirs["prompt"], theirs.get("prompt_version", "?")),
        "ours": Prompt("ours", ours["zero_shot_prompt"], version),
        "calls": Prompt("calls", ours["calls_prompt"], version),
        "refs": Prompt("refs", ours["refs_prompt"], version),
        "refs-strict": Prompt("refs-strict", ours["refs_strict_prompt"], version),
    }


SYSTEM = "You are a code structure extractor. Reply with JSON only."
