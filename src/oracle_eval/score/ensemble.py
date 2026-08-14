from __future__ import annotations

from collections import Counter
from collections.abc import Mapping, Sequence
from itertools import combinations

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
    score_file,
)
from oracle_eval.score.metrics import aggregate
from oracle_eval.score.run import ArmReport

OVERLAP_LIMIT = 0.80

OVERLAP_FORMULA = "containment: |E_a ∩ E_b| / min(|E_a|, |E_b|); 0.0 when either set is empty"


def score_ensemble_file(
    path: str,
    edges: list[Edge],
    predictions: Sequence[Prediction],
    cut: OracleCut,
    aliases: Aliases = NO_ALIASES,
    min_votes: int = 2,
) -> FileScore:
    votes: Counter[EdgeKey] = Counter()
    for prediction in predictions:
        votes.update(predicted_keys(path, prediction, cut, aliases).keys())
    winners = {key for key, count in votes.items() if count >= min_votes}

    return classify(path, winners, edges, cut)


def arm_errors(scores: list[FileScore]) -> set[EdgeKey]:
    errors: set[EdgeKey] = set()
    for score in scores:
        errors.update(score.spurious)
        errors.update(score.missed)
    return errors


def pairwise_overlap(errors_by_arm: Mapping[str, set[EdgeKey]]) -> list[tuple[str, str, float]]:
    pairs: list[tuple[str, str, float]] = []
    for (arm_a, errors_a), (arm_b, errors_b) in combinations(errors_by_arm.items(), 2):
        smaller = min(len(errors_a), len(errors_b))
        overlap = len(errors_a & errors_b) / smaller if smaller else 0.0
        pairs.append((arm_a, arm_b, overlap))
    return pairs


def max_overlap(pairs: Sequence[tuple[str, str, float]]) -> float:
    return max((overlap for _, _, overlap in pairs), default=0.0)


def run_ensemble(
    arms: Sequence[str],
    files: list[CorpusFile],
    oracle: dict[str, list[Edge]],
    predictions: Mapping[str, dict[str, ParseResult]],
    *,
    cut: OracleCut = OracleCut.CALLS_ONLY,
    aliases: Mapping[str, Aliases] | None = None,
    split: str = "dev",
    min_votes: int = 2,
) -> tuple[ArmReport, dict[str, list[FileScore]], list[tuple[str, str, float]]]:
    validity = ValidityReport()
    ensemble_scores: list[FileScore] = []
    per_arm: dict[str, list[FileScore]] = {arm: [] for arm in arms}

    for corpus_file in files:
        edges = oracle.get(corpus_file.path, [])
        alias = (aliases or {}).get(corpus_file.path, NO_ALIASES)

        voters: list[Prediction] = []
        answered = 0
        for arm in arms:
            result = predictions[arm].get(corpus_file.path)
            if result is not None and result.schema_valid:
                answered += 1
            prediction = (result.prediction if result else None) or Prediction(calls=[])
            voters.append(prediction)
            per_arm[arm].append(score_file(corpus_file.path, edges, prediction, cut, alias))

        quorum = answered >= min_votes
        validity.add(
            ParseResult(
                quorum,
                quorum,
                quorum,
                error=None
                if quorum
                else (
                    f"{corpus_file.path}: only {answered} of {len(arms)} arms answered"
                    f" (quorum {min_votes})"
                ),
            )
        )
        ensemble_scores.append(
            score_ensemble_file(corpus_file.path, edges, voters, cut, alias, min_votes)
        )

    name = f"ensemble-{min_votes}of{len(arms)}"
    report = ArmReport(name, split, cut, aggregate(ensemble_scores), validity)
    overlaps = pairwise_overlap({arm: arm_errors(scores) for arm, scores in per_arm.items()})
    return report, per_arm, overlaps
