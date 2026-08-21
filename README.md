# oracle-eval

An eval harness that set out to measure **how far prompt-only optimisation can push off-the-shelf
models on code-structure extraction**, scored against the TypeScript compiler as ground truth.

**It has an answer, and the answer redefined the question.** Prompt work took a 1.5B model from
**5.0% to 50.1% F1**, a tenfold gain, no weight changes, and left it **46 points below a free
tree-sitter parser scoring 99.8%**. The parser wins because the primary metric was defined so that
syntax alone suffices, which is a critique of the metric's design rather than a triumph of
tree-sitter. Models contribute in exactly one place: functions passed as values, which need type
knowledge no parser has. So the honest form of the project today is

> **Where is a language model the wrong tool for code-structure extraction, and where is it the
> only tool?**

**That outcome was pre-committed.** Three results were written down before any model ran, each with
its consequence, and "the naive parser wins" was one of them, including the reframe onto the
residue. Nothing was rescued after the fact.

### Where to look

| | |
|---|---|
| The claim, and the arithmetic behind it | the demo site under `web/`, or the tables below |
| Every rule that could favour an outcome | `src/oracle_eval/score/`, frozen in code before the runs |
| Whether the scorer is right | `tests/`, 74 cases on the scoring path and nothing else |
| What was decided and why | the comments where the decision lives, not a separate document |

**Status.** Two rounds run and scored, on remeda's **dev split only**. Three outcomes were written
down before any model ran; the third, "the naive parser wins", is the one that fired, and the
reframe onto the residue was already on paper when it did. Round 2's ensemble was **dropped by its
own kill switch** at 82.8% pairwise error overlap against a threshold of 80% fixed before the
number existed. The 38-file test split and the held-out repository have never been scored.

---

## The headline numbers

All figures: **dev split, remeda, 112 files.** Every one is copied from an artefact under
`data/results/`, and the demo site names that artefact beside the figure.

### The primary cut is a solved syntactic task, `calls_only`, 331 edges

| arm | raw JSON validity | P | R | **F1** |
|---|---|---|---|---|
| tree-sitter, free, deterministic, no model | 112/112 | 100.0% | 99.7% | **99.8% [99.2 to 100.0]** |
| Round 0, the published 8k prompt | **0/112** | 13.9% | 3.0% | **5.0%** |
| Round 1, qwen2.5-coder 1.5B, `calls` + JSON mode | 108/112 | 48.3% | 52.0% | **50.1% [42.7 to 56.6]** |
| Round 1, llama3.2 3B, `calls` + JSON mode | 112/112 | 36.7% | 63.1% | **46.4% [41.0 to 51.4]** |

And the parser replicates: **1,229 edges across hexo, nest, ink and tus-node-server, zero errors**,
each with its own frozen corpus and its own ts-morph oracle.

### Where models do contribute, `full`, 454 edges

| construct | P | R | **F1** |
|---|---|---|---|
| tree-sitter alone | 100.0% | 72.7% | **84.2% [81.8 to 86.7]** |
| + both models, agreement required | **96.0%** | **90.3%** | **93.1% [90.8 to 94.7]** |

**86.7 and 90.8 do not overlap**, so this is the project's one *measured* improvement over the
parser. The mechanism: tree-sitter is blind to 124 type-dependent edges, one model recovers most but
its additions are only ~45% precise, and requiring two models **from different labs** to name the
same edge lifts addition precision to 82%.

**Its sharpest limitation, stated here rather than left to be found:** remeda's idiom is
higher-order functions, so 27% of its edges are type-dependent against hexo's 3%. The 84.2 to 93.1
result may be a fact about functional TypeScript rather than about TypeScript.

---

## Setup

```bash
python -m venv .venv
./.venv/Scripts/python.exe -m pip install -e ".[arms,dev]"
```

The `arms` extra brings `tree-sitter`, which the baseline arm needs, and that arm carries the
finding, so it is not optional in practice. `dev` brings ruff, mypy and pytest.

That is the whole setup for everything in the next section. Nothing below needs an API key, a
model, or a checkout of the repository the corpus was drawn from.

**What this repository does not carry.** The `ts-morph` extractor that builds ground truth, and the
two prompt templates, live in the sibling project this harness was split out of. Rebuilding the
oracle from source and running an arm against a live model both need that tree; scoring does not,
because every response is stored and re-scored from disk. Commands that need it say so and stop
rather than failing halfway.

## Run it yourself

Nothing below calls a model. Every arm's raw responses are on disk and every score is re-derived
from them, because LLM APIs are not deterministic even at temperature 0.

```bash
P=./.venv/Scripts/python.exe

$P -m oracle_eval.cli score selfcheck                          # must print exactly 1.000
$P -m oracle_eval.cli score run treesitter --cut calls_only    # the floor: 99.8%
$P -m oracle_eval.cli hybrid run treesitter qwen15b-refs llama32b-refs --require-agreement
$P -m oracle_eval.cli oracle blindspots                        # what the oracle cannot see
$P -m oracle_eval.cli export demo                              # rebuild the dashboard's data (needs the sibling tree)
cd web && pnpm install && pnpm dev
```

`score selfcheck` is the one to run first. It scores the oracle against itself under a known amount
of damage, and its expectations were fixed in code before it was first run: an undamaged run must
report exactly 1.000, and three *negative* controls must score badly. Every scoring bug found on
08 Aug 2026 lived on a path only a wrong answer reaches, which is what that command exists to walk.

Without a checkout of the corpus repository the harness says so and continues, because scores come
from stored responses rather than from the sources. What it cannot then confirm is that the oracle
still matches the code it was built from, and it prints exactly that.

## Where ground truth comes from

**Call expressions plus callable references**, both from the TypeScript compiler's own typechecker
via `ts-morph`. `scip-typescript` was the original plan; it is now a one-off cross-validation rather
than part of scoring, because its entire unique contribution turned out to be the callable-reference
class the extractor covers directly. The numbers behind that are in the table below and in the
comment at the head of `src/oracle_eval/oracle/build.py`.

`tools/extract_corpus.ts` batches the extractor over a repository. It imports that extractor from
the sibling project, so it does not run from a checkout of this repository alone.

## What the oracle contains

remeda, 522 files walked, tests excluded:

| cut | edges |
|---|---|
| all edges, non-test | 712 |
| **PRIMARY, function caller** | **686** |
| module scope (imports, top-level) | 26 |

By kind: `free` 282 · `callable_ref` 163 · `method` 138 · `static` 82 · `new` 21.
Files with ≥1 primary edge: **159**, median **4**, max **23**.

The scored corpus is the selection-rule subset of those: **150 files, frozen 112 dev / 38 test**,
split on `sha256(relative_path)` so it correlates with neither filename nor size, and digest-guarded
so a hand-edited manifest is refused. The rule and the frozen manifest are both committed, under
`src/oracle_eval/corpus.py` and `data/corpus/`.

## How far the oracle is trusted

**Hand-adjudicated: 22/22 correct**, each row checked against its quoted source line. With n=22 and
no errors that supports **precision ≥86% at 95% confidence** (rule of three). Not "100%": the sample
needs to reach ~60 edges to claim ≥95%, and that is the highest-value hour left in the project.
`harness oracle adjudicate --files ...` emits the blank sheet.

**Cross-validated against `scip-typescript`**, third-party and compiler-accurate:

| | |
|---|---|
| coverage of SCIP's valid contribution | **97.8%** |
| SCIP false positives correctly absent | 6 |
| genuinely still missing | 2 (both `x in COMPARATORS`, a membership test) |
| oracle edges SCIP could never express | **383** |

## What it cannot do

Precise static call-graph construction is **undecidable** in general (Rice's theorem). `obj[name]()`,
`eval`, dynamic `import()` and structural dispatch have no static answer. Those call sites are the
**residue**: counted, published, and excluded from scoring in both directions, because scoring a
model right or wrong there would be inventing ground truth.

The oracle also walks `CallExpression` and `NewExpression` only, so tagged templates, bare
decorators, JSX elements and getter reads are invisible to it. All four measure **zero on remeda**,
which is exactly why neither the hand adjudication nor the SCIP agreement could have detected them.
`harness oracle blindspots` counts them per repository, and a repo with a non-zero count cannot be
scored until the walk is widened or those files are excluded and the count published.

## Quality gates

```bash
./.venv/Scripts/python.exe -m ruff check .
./.venv/Scripts/python.exe -m ruff format --check .
./.venv/Scripts/python.exe -m mypy --strict          # src, tests and tools
./.venv/Scripts/python.exe -m pytest -q              # 74 passed
```

All four run in CI on every push and pull request, together with the web app's typecheck, lint,
format and build, plus a check that no em or en dash reaches the rendered site. The point is that
"lint, format and types are clean" stops being a claim in a handoff document.

## Layout

```
src/oracle_eval/
  cli.py            mounts seven command groups, does no work
  paths.py          frozen default locations. Imports nothing from the package
  console.py        the one Console; stdout hardened at the entry point
  loading.py        THE corpus + oracle loader, both integrity checks live here
  results.py        THE result writer, the clobber guard lives here
  commands/         one module per job; a `typer.Typer` lives here and nowhere else
  oracle/           the oracle: ts-morph extraction, edge build, SCIP cross-validation
  corpus.py         the selection rule, the split, and the manifest digest
  arms/             prompts, the immutable response cache, providers, tree-sitter
  predict/          fence-strip parsing and the answer schema
  score/            matching, cuts, metrics with bootstrap CIs, ensemble, hybrid
  export/           the demo's one JSON, and the frozen list of rows it may show
tests/              74 tests, on the scoring path and the frozen rules, nothing else
tools/              corpus extraction, the SCIP cross-check, the local model definitions
web/                the demo site, Next 16 · React 19 · TS strict · Tailwind v4
data/oracle/<repo>/ tsmorph.jsonl + index.scip (git-ignored, regenerable)
data/corpus/<repo>/ the frozen manifest, committed, because it IS the split
data/results/       scored output (git-ignored, see below)
```

One rule the layout follows without exception: **a `typer.Typer` lives under `commands/`; a domain
module holds none.** `arms/treesitter.py` is 454 lines and that is deliberate, twelve private
helpers behind a three-name public surface. A long file with one job is not a god file.

## What is not in this repository, and why that is a gap

**`data/results/` is git-ignored, and those files are the published numbers.** `export demo` reads
them, every figure on the site names one as its source, and a reviewer checking a figure against
its artefact needs them. They total ~470 KB.

They stay out only because the pipeline that regenerates them also needs `data/oracle/*.jsonl`
(19 MB) and `data/predictions/` (3.7 MB). Committing the results alone would hand a reviewer the
claims without the means to re-derive them, which is worse than committing neither. Committing all
three is the honest option and costs ~24 MB.

Stated here rather than left to be discovered, because it is the one claim on this page that the
repository alone cannot support.
