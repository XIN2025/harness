from __future__ import annotations

import warnings
from collections.abc import Sequence
from dataclasses import dataclass
from typing import Literal

import numpy as np
from numpy.typing import NDArray
from scipy.stats import bootstrap

from oracle_eval.score.match import FileScore

N_RESAMPLES = 10_000
CONFIDENCE = 0.95
RNG_SEED = 20260808

Method = Literal["BCa", "percentile", "degenerate"]

Counts = NDArray[np.float64]


@dataclass(frozen=True, slots=True)
class Interval:
    point: float
    low: float
    high: float
    method: Method

    def render(self, width: int = 0) -> str:
        flag = "" if self.method == "BCa" else f" ({self.method})"
        return f"{self.point:>{width}.1%} [{self.low:.1%} to {self.high:.1%}]{flag}"

    def overlaps(self, other: Interval) -> bool:
        return self.low <= other.high and other.low <= self.high


def _totals(counts: Counts, axis: int) -> Counts:
    total: Counts = np.asarray(counts, dtype=float).sum(axis=axis)
    return total


def _safe_divide(num: Counts, den: Counts) -> Counts:
    quotient: Counts = np.divide(num, den, out=np.zeros_like(den, dtype=float), where=den > 0)
    return quotient


def _precision(tp: Counts, fp: Counts, fn: Counts, axis: int = -1) -> Counts:
    t, f = _totals(tp, axis), _totals(fp, axis)
    return _safe_divide(t, t + f)


def _recall(tp: Counts, fp: Counts, fn: Counts, axis: int = -1) -> Counts:
    t, m = _totals(tp, axis), _totals(fn, axis)
    return _safe_divide(t, t + m)


def _f1(tp: Counts, fp: Counts, fn: Counts, axis: int = -1) -> Counts:
    t, f, m = _totals(tp, axis), _totals(fp, axis), _totals(fn, axis)
    return _safe_divide(2 * t, 2 * t + f + m)


_STATISTICS = {"precision": _precision, "recall": _recall, "f1": _f1}


def _interval(
    name: str,
    tp: Counts,
    fp: Counts,
    fn: Counts,
    *,
    n_resamples: int,
    confidence: float,
    seed: int,
) -> Interval:
    statistic = _STATISTICS[name]
    point = float(statistic(tp, fp, fn, axis=-1))

    if len(tp) < 2:
        return Interval(point, point, point, "degenerate")

    def run(method: Literal["BCa", "percentile"]) -> tuple[float, float]:
        with warnings.catch_warnings():
            warnings.simplefilter("ignore")
            result = bootstrap(
                (tp, fp, fn),
                statistic,
                paired=True,
                vectorized=True,
                n_resamples=n_resamples,
                confidence_level=confidence,
                method=method,
                rng=np.random.default_rng(seed),
            )
        return float(result.confidence_interval.low), float(result.confidence_interval.high)

    low, high = run("BCa")
    if np.isnan(low) or np.isnan(high):
        low, high = run("percentile")
        return Interval(point, low, high, "percentile")
    return Interval(point, low, high, "BCa")


@dataclass(frozen=True, slots=True)
class ArmScore:
    files: tuple[FileScore, ...]
    precision: Interval
    recall: Interval
    f1: Interval

    @property
    def tp(self) -> int:
        return sum(f.tp for f in self.files)

    @property
    def fp(self) -> int:
        return sum(f.fp for f in self.files)

    @property
    def fn(self) -> int:
        return sum(f.fn for f in self.files)

    @property
    def unscored(self) -> int:
        return sum(len(f.unscored) for f in self.files)

    @property
    def truth(self) -> int:
        return self.tp + self.fn

    @property
    def n_files(self) -> int:
        return len(self.files)

    def render(self) -> str:
        return f"P {self.precision.render()}   R {self.recall.render()}   F1 {self.f1.render()}"

    def render_counts(self) -> str:
        return (
            f"{self.fp + self.fn} wrong of {self.truth}"
            f"   ({self.fn} missed · {self.fp} spurious)"
            f"   ·  {self.n_files} files  ·  {self.unscored} unscored"
        )


def aggregate(
    scores: Sequence[FileScore],
    *,
    n_resamples: int = N_RESAMPLES,
    confidence: float = CONFIDENCE,
    seed: int = RNG_SEED,
) -> ArmScore:
    if not scores:
        raise ValueError("cannot score zero files")

    tp = np.array([f.tp for f in scores], dtype=float)
    fp = np.array([f.fp for f in scores], dtype=float)
    fn = np.array([f.fn for f in scores], dtype=float)

    def interval(name: str) -> Interval:
        return _interval(
            name, tp, fp, fn, n_resamples=n_resamples, confidence=confidence, seed=seed
        )

    return ArmScore(
        files=tuple(scores),
        precision=interval("precision"),
        recall=interval("recall"),
        f1=interval("f1"),
    )
