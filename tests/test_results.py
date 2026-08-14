import json
from pathlib import Path

import pytest
import typer

from oracle_eval.results import refuse_clobber, write_json, write_result


def existing(tmp_path: Path, payload: dict[str, object]) -> Path:
    path = tmp_path / "result.json"
    write_json(path, payload)
    return path


def test_a_different_construct_under_the_same_name_is_refused(tmp_path: Path) -> None:
    path = existing(tmp_path, {"arms": ["qwen15b-refs", "llama32b-refs"]})
    with pytest.raises(typer.Exit):
        refuse_clobber(path, {"arms": ["qwen15b-refs-strict", "llama32b-refs-strict"]})


def test_a_union_hybrid_is_refused_over_an_agreement_hybrid(tmp_path: Path) -> None:
    path = existing(tmp_path, {"arm": "hybrid(treesitter+qwen15b-refs & llama32b-refs)"})
    with pytest.raises(typer.Exit):
        refuse_clobber(path, {"arm": "hybrid(treesitter+qwen15b-refs+llama32b-refs)"})


def test_arm_lists_are_compared_as_values_and_never_as_rendered_text(tmp_path: Path) -> None:
    path = existing(tmp_path, {"arms": ["a", "b"]})
    with pytest.raises(typer.Exit):
        refuse_clobber(path, {"arms": ["a + b"]})


def test_re_running_the_same_construct_is_allowed(tmp_path: Path) -> None:
    path = existing(tmp_path, {"arms": ["a", "b"]})
    refuse_clobber(path, {"arms": ["a", "b"]})


def test_force_overwrites(tmp_path: Path) -> None:
    path = existing(tmp_path, {"arms": ["a", "b"]})
    refuse_clobber(path, {"arms": ["c", "d"]}, force=True)


def test_a_field_the_recorded_payload_lacks_is_not_a_mismatch(tmp_path: Path) -> None:
    path = existing(tmp_path, {"arm": "ensemble-2of2"})
    refuse_clobber(path, {"arm": "ensemble-2of2", "arms": ["a", "b"]})


def test_a_result_and_its_diff_are_written_together(tmp_path: Path) -> None:
    out = tmp_path / "results" / "nested"
    written = write_result(
        out, "arm.dev.full", {"arm": "arm", "counts": {}}, "# diff\n", identity={"arm": "arm"}
    )

    assert written == out / "arm.dev.full.json"
    assert json.loads(written.read_text(encoding="utf8"))["arm"] == "arm"
    assert (out / "arm.dev.full.diff.md").read_text(encoding="utf8") == "# diff\n"
