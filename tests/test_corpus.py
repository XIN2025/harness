import json
from pathlib import Path

import pytest

from oracle_eval.corpus import (
    CorpusFile,
    digest_of,
    load_manifest,
    qualifies,
    select_corpus,
    split_of,
    to_manifest,
    write_manifest,
)
from oracle_eval.oracle.build import Edge, EdgeKind

MANIFEST_PATH = Path(__file__).parent.parent / "data" / "corpus" / "remeda" / "manifest.json"
requires_manifest = pytest.mark.skipif(
    not MANIFEST_PATH.exists(), reason="run `harness corpus freeze` first"
)


def edge(file: str, callee: str = "purry") -> Edge:
    return Edge(file=file, caller="f", callee=callee, kind=EdgeKind.FREE, receiver=None, line=1)


def fake_repo(tmp_path: Path, paths: list[str]) -> Path:
    for path in paths:
        target = tmp_path / path
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(f"// {path}\n", encoding="utf8")
    return tmp_path


def test_test_files_and_non_src_files_never_qualify() -> None:
    assert not qualifies("src/a.test.ts", 100, 5)
    assert not qualifies("src/a.test-d.ts", 100, 5)
    assert not qualifies("test/a.ts", 100, 5)
    assert not qualifies("scripts/build.ts", 100, 5)


def test_the_split_is_deterministic_and_not_alphabetical(tmp_path: Path) -> None:
    paths = [f"src/{name}.ts" for name in "abcdefghijklmnop"]
    repo = fake_repo(tmp_path, paths)
    lines = dict.fromkeys(paths, 100)

    forward = select_corpus([edge(p) for p in paths], lines, repo)
    reverse = select_corpus([edge(p) for p in reversed(paths)], lines, repo)

    assert digest_of(forward) == digest_of(reverse)
    dev = {f.path for f in forward if f.split == "dev"}
    assert dev != set(paths[: len(dev)]), "split fell back to alphabetical order"


def test_the_digest_covers_content_and_split_not_just_paths() -> None:
    base = [CorpusFile(path="src/a.ts", sha256="aaa", lines=100, edges=3, split="dev")]
    edited = [CorpusFile(path="src/a.ts", sha256="bbb", lines=100, edges=3, split="dev")]
    moved = [CorpusFile(path="src/a.ts", sha256="aaa", lines=100, edges=3, split="test")]

    assert digest_of(base) != digest_of(edited)
    assert digest_of(base) != digest_of(moved)


def test_load_manifest_rejects_a_hand_edited_row(tmp_path: Path) -> None:
    files = [CorpusFile(path="src/a.ts", sha256="aaa", lines=100, edges=3, split="dev")]
    path = tmp_path / "manifest.json"
    write_manifest(path, to_manifest("fake", files))

    raw = json.loads(path.read_text(encoding="utf8"))
    raw["files"][0]["split"] = "test"
    path.write_text(json.dumps(raw), encoding="utf8")

    with pytest.raises(ValueError, match="digest mismatch"):
        load_manifest(path)


@requires_manifest
def test_the_frozen_split_is_pinned() -> None:
    files = load_manifest(MANIFEST_PATH)
    assert digest_of(files) == "8a26bfbc5f4ba0a3c61018544189a37257d919ef30f42e0c0b528dbc64e40e5f"
    assert len(split_of(files, "dev")) == 112
    assert len(split_of(files, "test")) == 38
