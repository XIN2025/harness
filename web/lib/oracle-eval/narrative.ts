export type Note = {
  readonly title: string;
  readonly body: string;
};

export type RegisteredOutcome = {
  readonly condition: string;
  readonly consequence: string;
  readonly actual: string;
  readonly fired: boolean;
};

export const REGISTERED_OUTCOMES: readonly RegisteredOutcome[] = [
  {
    condition: "Prompting plateaus early",
    consequence:
      "Validates spending training compute instead of prompt effort.",
    actual: "Partly. It plateaued, but far below a parser.",
    fired: false,
  },
  {
    condition: "Prompting climbs high",
    consequence:
      "Interesting for languages a parser handles poorly, where no cheap oracle exists.",
    actual: "No.",
    fired: false,
  },
  {
    condition: "The naive parser wins",
    consequence:
      "The residue is the interesting territory. Reframe onto it: where is a model the wrong tool, and where is it the only tool?",
    actual: "This one. The reframe was already on paper when it happened.",
    fired: true,
  },
];

export const CONSTRAINTS: readonly Note[] = [
  {
    title: "No paid inference budget",
    body: "Every arm ran on free or local inference, which ruled out frontier models entirely. The study is about small models because those were the ones available, not because small models were the research target.",
  },
  {
    title: "A consumer laptop, no real GPU",
    body: "Models served locally through Ollama, which restricted the work to two small open models from different labs. The exact identifiers and revisions are pinned in the repository.",
  },
  {
    title: "Free hosted GPU in short sessions only",
    body: "Anything needing sustained GPU time was out of scope. This is why the study measures prompting rather than fine-tuning, and why no fine-tuning claim appears anywhere.",
  },
  {
    title: "Windows, solo, evenings and weekends",
    body: "Surfaced real portability faults during the build, including a crash on the default console encoding. It also forced a narrow scope: one language, one repository for the model arms, four more for the parser baseline.",
  },
];

export const PROPERTIES: readonly Note[] = [
  {
    title: "Nothing is scored from a live API call",
    body: "Every raw response is written to disk and scored from that file. LLM endpoints are not deterministic even at temperature zero, so a number that cannot be re-derived from a stored artefact is an anecdote rather than a result.",
  },
  {
    title: "Every rule that could favour an outcome was frozen before use",
    body: "Cut definitions, matching rules, normalisation and kill conditions were all written before the data they would be applied to existed. The preregistration is append-only and carries fifteen dated amendments.",
  },
  {
    title: "Schema validity is never blended into accuracy",
    body: "A model scoring well on the fraction of outputs that parse is worse than a lower score on nearly all of them, and only separate counters can say so. This distinction carries the entire Round 0 story.",
  },
  {
    title: "Every number carries an interval, and overlap is enforced in code",
    body: "The bootstrap resamples over files rather than edges, because edges inside one file share a caller and an idiom. Comparisons route through a single function that reports overlapping intervals as no measured change, including on this page.",
  },
  {
    title: "The demo reads the harness, it never re-implements it",
    body: "Summary metrics are copied out of the result files. Per-file edges are recomputed by calling the harness's own scoring functions. The two reconcile exactly, which is checkable on any file in the explorer.",
  },
];

export type Decision = Note & {
  readonly id: string;
  readonly intent: string;
};

export const DECISIONS: readonly Decision[] = [
  {
    id: "D-14",
    title: "tree-sitter is a baseline arm, not part of the oracle",
    intent:
      "A parser with no type resolution is wrong as ground truth and exactly right as a deliberately dumb control.",
    body: "The rationale recorded at the time: if a regex-grade extractor scores 70% and the best model 81%, the whole framing changes and we need that number. This decision is why the project has a result at all. The parser did not score 70%.",
  },
  {
    id: "D-9",
    title: "The ensemble kill condition was fixed before the overlap was known",
    intent:
      "Fix the threshold in advance so it cannot be adjusted once it becomes inconvenient.",
    body: "It fired in Round 2 and cost the project a construct. A threshold that never fires is decoration.",
  },
  {
    id: "D-3",
    title: "Micro-averaged F1 on function-to-function call edges",
    intent:
      "Four defensible denominators existed; choosing the most conservative in advance is the only way a headline is not simply a choice of denominator.",
    body: "It is also the source of two open metric gaps, both stated on the limits page rather than left to be found.",
  },
  {
    id: "D-5",
    title: "The bootstrap resamples files, not edges",
    intent:
      "Edges within a file share a caller and an idiom; resampling edges would treat correlated observations as independent.",
    body: "Edge resampling would have produced narrower intervals and more apparent findings. Every interval on this site is the wider, correct one.",
  },
  {
    id: "D-4",
    title: "Schema validity is reported separately from accuracy, always",
    intent: "Prevent the most common evaluation error.",
    body: "It earned its place twice: Round 0's zero valid responses are the whole Round 0 finding, and a stale six-file artefact was caught purely by a validity badge that disagreed with its own label.",
  },
  {
    id: "D-6",
    title: "Two prompts per model: one published, one written from scratch",
    intent:
      "So that “this prompt does not transfer” can never be reported as “off-the-shelf models are bad.”",
    body: "Both Round 0 arms failed, and they failed differently. Only having both makes that separable.",
  },
  {
    id: "D-17",
    title: "Fence-stripping is the only permitted repair",
    intent:
      "Every additional repair silently converts a model that ignored an instruction into an accuracy number.",
    body: "Responses that did not parse are counted as responses that did not parse.",
  },
  {
    id: "D-10",
    title: "An immutable, content-addressed cache",
    intent:
      "Re-running an unchanged input costs zero calls, which under a no-budget constraint is what made multiple rounds possible at all.",
    body: "Round 2 resumed straight past its smoke-test files because of it.",
  },
  {
    id: "D-15",
    title:
      "Scored on the primary cut, with the wider cut as a mandatory secondary",
    intent:
      "The published prompt asks for calls and never for functions passed as values; scoring it against the full oracle would charge it for a class it never mentions.",
    body: "Complicated by the finding, since the common ground turned out to be the cut a parser solves for free. The kill-switch moved to the wider cut without moving the metric, and every page states which cut it is reporting.",
  },
];

export type Failure = Note & {
  readonly id: string;
  readonly lesson: string;
};

export const FAILURES: readonly Failure[] = [
  {
    id: "F-1",
    title: "Three silent bugs moved one number twice before it settled",
    body: "Caught only because the first value was too bad to be true.",
    lesson:
      "A merely plausible wrong number gets published. Implausibility is not a detection strategy.",
  },
  {
    id: "F-9",
    title:
      "An entire SCIP pipeline was built to answer an objection nobody had checked was real",
    body: "The circularity concern it addressed turned out not to apply.",
    lesson: "Verify the objection before building the answer.",
  },
  {
    id: "F-10",
    title: "Half the test suite was pinning deleted code",
    body: "And the total was being quoted as a quality signal while it did so.",
    lesson: "Test count is not a quality signal.",
  },
  {
    id: "F-11",
    title: "Schema over-strictness discarded most of one arm's valid responses",
    body: "A single wrong field name folded a substantive answer into a zero.",
    lesson:
      "Validation strictness is a measurement decision, not a hygiene decision.",
  },
  {
    id: "F-12",
    title: "A published artefact was zero bytes and nobody had looked",
    body: "It contained the most important number in the project. The floor was invisible for a day because a file was empty and nothing checked.",
    lesson:
      "Artefacts now self-describe, and the exporter refuses to publish a row it cannot reconcile.",
  },
  {
    id: "F-13",
    title: "A six-file smoke test overwrote a full-corpus result in place",
    body: "The dashboard rendered the six-file figure under a label that said the full corpus.",
    lesson:
      "Caught by a validity badge reading 6/6. The exporter now fails the build if a row's file count does not match the corpus, so the check that would have caught it is the check that now runs.",
  },
  {
    id: "F-14",
    title:
      "An output was named by vote count rather than by the arms that produced it",
    body: "Round 2's run silently clobbered a published Round 1 figure.",
    lesson: "Naming schemes are correctness surfaces.",
  },
  {
    id: "F-15",
    title: "A command crashed on the default Windows console",
    body: "It printed a set-intersection glyph the console's code page cannot encode.",
    lesson: "Portability faults are found by running on the machine you have.",
  },
  {
    id: "F-16",
    title: "The demo overclaimed for a day",
    body: "The first version of this dashboard led with the prompt curve and no baseline, presenting a tenfold climb as progress toward something already solved for free.",
    lesson:
      "The instrument was honest; the presentation was not, and the presentation is what people see. The parser floor now leads every chart it belongs on.",
  },
  {
    id: "F-17",
    title: "Two of the extra corpora drifted from their frozen manifests",
    body: "They are currently unscoreable without re-freezing, and they are named as such on the headroom table rather than quietly dropped from it.",
    lesson: "Freezing is not a one-time act.",
  },
];

export const LIMITS: readonly Note[] = [
  {
    title:
      "The headline may be a fact about functional TypeScript, not about TypeScript",
    body: "How blind the parser is varies enormously by idiom, and the scored repository is a point-free functional library, which is where this phenomenon lives. The headroom table measures exactly that.",
  },
  {
    title:
      "The instrument is not independent of the repository it was built on",
    body: "Not only the prompts: the output schema, a caller-alias rule, the normalisation, the cut definitions, the parser arm and the oracle adjudication were all shaped by that one repository. Any number the instrument produces on it is a number produced by a tool it shaped.",
  },
  {
    title: "The headline may sit inside oracle noise",
    body: "Oracle precision rests on a hand-checked sample, and the hybrid figure is not cleanly separated from that bound. Adjudicating more rows is the highest-value work remaining, and it is reading rather than engineering.",
  },
  {
    title: "The weighting is a convention, not a justified choice",
    body: "A spurious edge and a missed edge do not cost the same downstream, and F1 weights them equally here because that is the convention, not because the trade-off was argued.",
  },
  {
    title: "Every figure is micro-averaged",
    body: "Counts are pooled across files, so a file with forty edges counts forty times a file with one. No per-file mean exists yet.",
  },
  {
    title: "Unscored predictions are an unaudited escape hatch",
    body: "Precision is computed after removing predictions the cut excluded, and what it would be if those counted as errors has never been published. The named fix is a risk-coverage curve.",
  },
  {
    title: "And the deepest one: this measures reproduction, not usefulness",
    body: "F1 answers whether the oracle edge set was reproduced, not whether the graph is useful. Naming the right callee under the wrong caller scores the same as inventing one, and no downstream task was run.",
  },
];

export const CLAIMED: readonly string[] = [
  "The harness and what it does.",
  "The scoring rules, and when each was frozen.",
  "The numbers, each with its interval.",
  "What the design controls for.",
  "The mechanism behind the agreement filter.",
  "The failures, in full.",
  "The limits, in full.",
];

export const QUALIFIED: readonly string[] = [
  "Generality: one language, one repository for the model arms, four repositories for the parser baseline only.",
  "That this measures off-the-shelf small models under a no-budget constraint, which says nothing about fine-tuned models.",
];

export const NEXT: readonly Note[] = [
  {
    title: "Adjudicate a larger sample of oracle rows",
    body: "Everything else is downstream of the oracle being trustworthy, and the current headline is not cleanly separated from the oracle's own error bound. Roughly an hour of reading.",
  },
  {
    title: "Publish the headroom table as a scope claim",
    body: "Already measured, costs nothing, and turns the study's largest weakness into a stated limit. It is on the results page.",
  },
  {
    title: "Add the unscored-sensitivity analysis and a macro-averaged figure",
    body: "Pure code, no new model runs, and it closes two of the four metric gaps.",
  },
  {
    title: "Spend the held-back test split, once",
    body: "It does not test cross-repository generalisation, since nothing currently can, but it answers a different real question: did three rounds of prompt iteration overfit the split they were tuned on?",
  },
  {
    title: "Run a second extractor as an arm inside the harness",
    body: "Which is the only honest way to compare anything to anything here.",
  },
];
