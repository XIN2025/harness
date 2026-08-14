from __future__ import annotations

from collections.abc import Mapping, Sequence

from oracle_eval.corpus import CorpusFile
from oracle_eval.oracle.build import Edge
from oracle_eval.predict.parse import ParseResult, ValidityReport
from oracle_eval.predict.schema import Prediction
from oracle_eval.score.match import (
    NO_ALIASES,
    Aliases,
    EdgeKey,
    FileScore,
    OracleCut,
    classify,
    predicted_keys,
)
from oracle_eval.score.metrics import aggregate
from oracle_eval.score.run import ArmReport


def score_union_file(
    path: str,
    edges: list[Edge],
    predictions: Sequence[Prediction],
    cut: OracleCut,
    aliases: Aliases = NO_ALIASES,
    *,
    base_count: int = 0,
    require_agreement: bool = False,
) -> FileScore:
    keysets = [predicted_keys(path, p, cut, aliases).keys() for p in predictions]
    base_keys = keysets[:base_count]
    model_keys = keysets[base_count:]

    if require_agreement and len(model_keys) < 2:
        raise ValueError(
            f"--require-agreement needs at least two model arms, got {len(model_keys)}. "
            "One arm has nothing to agree with, and unioning it instead would publish a "
            "different construct under the agreement arm's name."
        )

    united: set[EdgeKey] = set()
    for keys in base_keys:
        united |= keys
    if require_agreement:
        agreed = set(model_keys[0])
        for keys in model_keys[1:]:
            agreed &= keys
        united |= agreed
    else:
        for keys in model_keys:
            united |= keys

    return classify(path, united, edges, cut)


def _predictions_for(
    arm: str, path: str, predictions: Mapping[str, dict[str, ParseResult]]
) -> Prediction:
    result = predictions.get(arm, {}).get(path)
    return (result.prediction if result else None) or Prediction(calls=[])


def run_hybrid(
    base: str,
    additions: Sequence[str],
    files: list[CorpusFile],
    oracle: dict[str, list[Edge]],
    predictions: Mapping[str, dict[str, ParseResult]],
    *,
    cut: OracleCut = OracleCut.FULL,
    aliases: Mapping[str, Aliases] | None = None,
    split: str = "dev",
    require_agreement: bool = False,
) -> tuple[ArmReport, ArmReport]:
    hybrid_scores: list[FileScore] = []
    base_scores: list[FileScore] = []
    validity = ValidityReport()

    for corpus_file in files:
        edges = oracle.get(corpus_file.path, [])
        alias = (aliases or {}).get(corpus_file.path, NO_ALIASES)

        base_prediction = _predictions_for(base, corpus_file.path, predictions)
        answered = predictions.get(base, {}).get(corpus_file.path)
        ok = bool(answered and answered.schema_valid)
        validity.add(
            ParseResult(
                ok, ok, ok, error=None if ok else f"{corpus_file.path}: base arm has no answer"
            )
        )

        added = [_predictions_for(a, corpus_file.path, predictions) for a in additions]
        base_scores.append(
            score_union_file(corpus_file.path, edges, [base_prediction], cut, alias, base_count=1)
        )
        hybrid_scores.append(
            score_union_file(
                corpus_file.path,
                edges,
                [base_prediction, *added],
                cut,
                alias,
                base_count=1,
                require_agreement=require_agreement,
            )
        )

    joiner = " & " if require_agreement else "+"
    name = f"hybrid({base}+{joiner.join(additions)})"
    return (
        ArmReport(name, split, cut, aggregate(hybrid_scores), validity),
        ArmReport(base, split, cut, aggregate(base_scores), validity),
    )
