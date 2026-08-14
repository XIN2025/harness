import pytest

from oracle_eval.score.match import FileScore
from oracle_eval.score.metrics import Interval, aggregate

FAST = {"n_resamples": 999}


def score(path: str, tp: int, fp: int, fn: int) -> FileScore:
    return FileScore(
        path=path,
        matched=tuple(("f", "c", f"tp{i}") for i in range(tp)),
        spurious=tuple(("f", "c", f"fp{i}") for i in range(fp)),
        missed=tuple(("f", "c", f"fn{i}") for i in range(fn)),
    )


def test_the_average_is_micro_not_macro() -> None:
    result = aggregate([score("big.ts", 10, 10, 0), score("tiny.ts", 1, 0, 0)], **FAST)
    assert result.precision.point == pytest.approx(11 / 21)


def test_zero_files_is_refused_rather_than_reported_as_zero() -> None:
    with pytest.raises(ValueError, match="zero files"):
        aggregate([], **FAST)


def test_the_interval_actually_widens_with_disagreement() -> None:
    uniform = aggregate([score(f"f{i}.ts", 5, 5, 5) for i in range(20)], **FAST)
    mixed = aggregate(
        [score(f"g{i}.ts", 10, 0, 0) if i % 2 else score(f"g{i}.ts", 0, 10, 10) for i in range(20)],
        **FAST,
    )
    uniform_width = uniform.f1.high - uniform.f1.low
    mixed_width = mixed.f1.high - mixed.f1.low
    assert mixed_width > uniform_width


def test_a_single_file_is_labelled_degenerate_not_given_a_fake_interval() -> None:
    result = aggregate([score("only.ts", 5, 1, 1)], **FAST)
    assert result.f1.method == "degenerate"
    assert "degenerate" in result.f1.render()


def test_the_bootstrap_is_reproducible() -> None:
    files = [score(f"f{i}.ts", i % 7, i % 3, i % 5) for i in range(30)]
    first, second = aggregate(files, **FAST), aggregate(files, **FAST)
    assert (first.f1.low, first.f1.high) == (second.f1.low, second.f1.high)


def test_overlap_detection_is_what_gates_a_claimed_improvement() -> None:
    round_one = Interval(0.50, 0.45, 0.55, "BCa")
    round_two = Interval(0.54, 0.49, 0.59, "BCa")
    round_five = Interval(0.70, 0.66, 0.74, "BCa")

    assert round_one.overlaps(round_two), "4 points with overlap is not an improvement"
    assert not round_one.overlaps(round_five)


def test_render_never_shows_a_bare_number() -> None:
    assert "[" in aggregate([score(f"f{i}.ts", 3, 1, 1) for i in range(5)], **FAST).render()
