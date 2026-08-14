from __future__ import annotations

import json
from collections.abc import Mapping
from pathlib import Path
from typing import Any, cast

import typer

from oracle_eval.console import console


def _canonical(value: object) -> object:
    if isinstance(value, (list, tuple)):
        return [_canonical(item) for item in value]
    return value


def _render(value: object) -> str:
    if isinstance(value, (list, tuple)):
        return " + ".join(str(item) for item in value)
    return str(value)


def refuse_clobber(
    path: Path,
    identity: Mapping[str, object],
    *,
    force: bool = False,
    note: str = "",
) -> None:
    if force or not path.exists():
        return
    try:
        loaded: object = json.loads(path.read_text(encoding="utf8"))
    except json.JSONDecodeError:
        return
    if not isinstance(loaded, dict):
        return
    existing = cast(dict[str, Any], loaded)

    differing = [
        (field, existing[field], value)
        for field, value in identity.items()
        if field in existing and _canonical(existing[field]) != _canonical(value)
    ]
    if not differing:
        return

    width = max(len(field) for field, _, _ in differing)
    console.print(f"\n[red]refusing to overwrite[/red] {path}")
    for field, recorded, incoming in differing:
        console.print(f"  {field:<{width}}  it holds  {_render(recorded)}")
        console.print(f"  {'':<{width}}  this run  {_render(incoming)}")
    if note:
        console.print(f"\n{note}")
    console.print(
        "\nWriting would replace a published figure with a different construct under the\n"
        "same name. Pass --out to keep them apart, or --force if the replacement is\n"
        "what you mean.\n"
    )
    raise typer.Exit(1)


def write_json(path: Path, payload: Mapping[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf8")


def write_result(
    out: Path,
    stem: str,
    payload: Mapping[str, Any],
    diff: str,
    *,
    identity: Mapping[str, object],
    force: bool = False,
    note: str = "",
) -> Path:
    json_path = out / f"{stem}.json"
    refuse_clobber(json_path, identity, force=force, note=note)
    out.mkdir(parents=True, exist_ok=True)
    write_json(json_path, payload)
    (out / f"{stem}.diff.md").write_text(diff, encoding="utf8")
    return json_path
