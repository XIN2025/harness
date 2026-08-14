from __future__ import annotations

import hashlib
import json
from collections import Counter
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Literal, TypedDict, cast

from oracle_eval.oracle.build import Edge
from oracle_eval.paths import is_test_file

Split = Literal["dev", "test"]

SPLITS: tuple[Split, ...] = ("dev", "test")

SRC_PREFIX = "src/"
MIN_LINES = 30
MAX_LINES = 600
MIN_EDGES = 1
DEV_FRACTION = 0.75


class ManifestRow(TypedDict):
    path: str
    sha256: str
    lines: int
    edges: int
    split: str


class Manifest(TypedDict):
    repo: str
    rule: dict[str, int | str | float]
    counts: dict[str, int]
    digest: str
    files: list[ManifestRow]


@dataclass(frozen=True, slots=True)
class CorpusFile:
    path: str
    sha256: str
    lines: int
    edges: int
    split: Split


def path_bucket(path: str) -> str:
    return hashlib.sha256(path.encode("utf8")).hexdigest()


def content_hash(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def qualifies(path: str, lines: int, edges: int, prefix: str = SRC_PREFIX) -> bool:
    return (
        path.startswith(prefix)
        and not is_test_file(path)
        and edges >= MIN_EDGES
        and MIN_LINES <= lines <= MAX_LINES
    )


def select_corpus(
    edges: list[Edge],
    line_counts: dict[str, int],
    repo_root: Path,
    prefix: str = SRC_PREFIX,
) -> list[CorpusFile]:
    per_file = Counter(e.file for e in edges)

    eligible = [
        (path, line_counts.get(path, 0), count)
        for path, count in per_file.items()
        if qualifies(path, line_counts.get(path, 0), count, prefix)
    ]
    eligible.sort(key=lambda row: path_bucket(row[0]))

    cutoff = round(len(eligible) * DEV_FRACTION)
    return [
        CorpusFile(
            path=path,
            sha256=content_hash(repo_root / path),
            lines=lines,
            edges=count,
            split="dev" if index < cutoff else "test",
        )
        for index, (path, lines, count) in enumerate(eligible)
    ]


def digest_of(files: list[CorpusFile]) -> str:
    payload = "\n".join(f"{f.path}:{f.sha256}:{f.split}" for f in files)
    return hashlib.sha256(payload.encode("utf8")).hexdigest()


def to_manifest(repo: str, files: list[CorpusFile], prefix: str = SRC_PREFIX) -> Manifest:
    counts = Counter(f.split for f in files)
    return Manifest(
        repo=repo,
        rule={
            "src_prefix": prefix,
            "min_lines": MIN_LINES,
            "max_lines": MAX_LINES,
            "min_edges": MIN_EDGES,
            "dev_fraction": DEV_FRACTION,
            "order": "sha256(relative_path)",
        },
        counts={"dev": counts["dev"], "test": counts["test"], "total": len(files)},
        digest=digest_of(files),
        files=[cast(ManifestRow, asdict(f)) for f in files],
    )


def write_manifest(path: Path, manifest: Manifest) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(manifest, indent=2) + "\n", encoding="utf8")


def load_manifest(path: Path) -> list[CorpusFile]:
    raw = cast(Manifest, json.loads(Path(path).read_text(encoding="utf8")))
    files = [
        CorpusFile(
            path=row["path"],
            sha256=row["sha256"],
            lines=row["lines"],
            edges=row["edges"],
            split=cast(Split, row["split"]),
        )
        for row in raw["files"]
    ]
    actual = digest_of(files)
    if actual != raw["digest"]:
        raise ValueError(
            f"manifest digest mismatch in {path}: recorded {raw['digest'][:12]}, "
            f"rows hash to {actual[:12]} — the file was edited by hand"
        )
    return files


def split_of(files: list[CorpusFile], split: Split) -> list[CorpusFile]:
    return [f for f in files if f.split == split]


def verify_manifest(files: list[CorpusFile], repo_root: Path) -> list[str]:
    problems: list[str] = []
    for corpus_file in files:
        path = repo_root / corpus_file.path
        if not path.exists():
            problems.append(f"{corpus_file.path}: missing under {repo_root}")
        elif content_hash(path) != corpus_file.sha256:
            problems.append(f"{corpus_file.path}: content changed since the split was frozen")
    return problems
