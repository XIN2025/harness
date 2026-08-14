from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class Row:
    stem: str
    label: str
    note: str = ""
    short: str = ""


CURVE: tuple[Row, ...] = (
    Row(
        "treesitter.dev.calls_only",
        "tree-sitter parser · free, deterministic, no model",
        "The floor every prompted arm is read against: 1 wrong edge in 331, from syntax alone.",
        short="tree-sitter",
    ),
    Row(
        "qwen15b-theirs.dev.calls_only",
        "Round 0 · Cassini's published 8k prompt",
        "Not one of 112 responses was valid JSON.",
        short="R0 · Cassini prompt",
    ),
    Row(
        "qwen15b-ours.dev.calls_only",
        "Round 0 · oracle-eval's zero-shot prompt",
        "Attributed 82 of 84 calls to module scope, which the primary cut excludes: "
        "plausible content, structurally unscoreable.",
        short="R0 · oracle-eval prompt",
    ),
    Row(
        "qwen15b-calls.dev.calls_only",
        "Round 1 · qwen2.5-coder 1.5B, calls prompt + JSON mode",
        "Ten times the published prompt's score, from prompt work alone. No weight changes.",
        short="R1 · qwen",
    ),
    Row(
        "llama32b-calls.dev.calls_only",
        "Round 1 · llama3.2 3B, calls prompt + JSON mode",
        "Higher recall and lower precision than qwen: it over-emits where qwen under-emits.",
        short="R1 · llama",
    ),
    Row(
        "ensemble-2of2.dev.calls_only",
        "Round 1 · both models must name the edge",
        "Precision is a measured gain. F1 is not, because its interval overlaps qwen's.",
        short="R1 · agreement",
    ),
)

HYBRID: tuple[Row, ...] = (
    Row(
        "treesitter.dev.full",
        "tree-sitter alone",
        "The free deterministic baseline. Perfect precision, blind to 124 type-dependent edges.",
        short="tree-sitter",
    ),
    Row(
        "hybrid-treesitter-qwen15b-refs.dev.full",
        "+ qwen residue (union)",
        "Recovers most of the missing edges, but its additions are only 45% precise.",
        short="+ qwen union",
    ),
    Row(
        "hybrid-treesitter-llama32b-refs.dev.full",
        "+ llama residue (union)",
        "Same shape, same problem.",
        short="+ llama union",
    ),
    Row(
        "hybrid-treesitter-qwen15b-refs-llama32b-refs.dev.full",
        "+ both, agreement required (Round 1)",
        "Requiring two models from different labs to name the same edge lifts addition "
        "precision to 82%.",
        short="R1 · agreement",
    ),
    Row(
        "hybrid-treesitter-qwen15b-refs-strict-llama32b-refs-strict.dev.full",
        "+ both, agreement required (Round 2)",
        "A stricter prompt made each model cleaner on its own and the combination no better, "
        "then pushed the pair's error overlap past the threshold that permits combining them "
        "at all.",
        short="R2 · agreement",
    ),
)

BASELINES: tuple[Row, ...] = (
    Row(
        "treesitter.dev.calls_only",
        "remeda · 112 files",
        "The scored corpus. One wrong edge in 331.",
        short="remeda",
    ),
    Row("ts-hexo.dev.calls_only", "hexo · 53 files", "549 edges, none wrong.", short="hexo"),
    Row("ts-nest.dev.calls_only", "nest · 43 files", "271 edges, none wrong.", short="nest"),
    Row("ts-ink.dev.calls_only", "ink · 26 files", "247 edges, none wrong.", short="ink"),
    Row(
        "ts-tus.dev.calls_only",
        "tus-node-server · 7 files",
        "162 edges, none wrong.",
        short="tus",
    ),
)


@dataclass(frozen=True, slots=True)
class HeadroomRow:
    stem: str
    repo: str
    idiom: str
    note: str = ""


HEADROOM: tuple[HeadroomRow, ...] = (
    HeadroomRow(
        "treesitter.dev.full",
        "remeda",
        "point-free functional",
        "The scored corpus. Its whole idiom is higher-order functions (purry, pipe, "
        "comparators, callbacks), so a quarter of its edges need type knowledge.",
    ),
    HeadroomRow(
        "ts-hexo.dev.full",
        "hexo",
        "imperative application framework",
        "Sixteen edges of room across 53 files. Model false-positive rates of 30-50% "
        "would swamp that by an order of magnitude.",
    ),
    HeadroomRow(
        "ts-ink.dev.full",
        "ink",
        "React renderer for the terminal",
        "Three edges of room. Running the hybrid here would measure its error rate, "
        "not its benefit.",
    ),
)

UNSCOREABLE: tuple[dict[str, str], ...] = (
    {
        "repo": "nest",
        "reason": "Corpus drifted from its frozen manifest. Unscoreable on the "
        "full cut without re-freezing or an explicit --allow-drift.",
    },
    {
        "repo": "tus-node-server",
        "reason": "Corpus drifted from its frozen manifest. Same fault, same fix.",
    },
)

OVERLAPS: tuple[Row, ...] = (
    Row("ensemble-2of2.dev.calls_only.overlap", "calls arms · Round 1", short="calls · R1"),
    Row("ensemble-2of2.dev.full.overlap", "refs arms · Round 1", short="refs · R1"),
    Row("ensemble-refs-strict.dev.full.overlap", "refs arms · Round 2", short="refs · R2"),
)

EXPLORER_BASE = "treesitter"
EXPLORER_MODELS: tuple[str, ...] = ("qwen15b-refs", "llama32b-refs")
HYBRID_PANEL = "hybrid"

NOT_CLAIMED: tuple[str, ...] = (
    "No F1 claim for the ensemble over qwen alone. The intervals overlap.",
    "No F1 claim for single-model hybrids over the parser. The intervals overlap.",
    "Nothing about generalisation. These are dev-split numbers. The test split and the "
    "held-out repo have never been scored.",
    "No comparison to any published figure from another system: different edge unit, "
    "different corpus, different ground truth.",
    "The refs arms overlap at 69.1%, close enough to the 80% kill threshold that adding "
    "a third arm could change it.",
)

MODELS: tuple[dict[str, str], ...] = (
    {
        "arm": "qwen15b",
        "model": "qwen2.5-coder:1.5b-instruct",
        "lab": "Alibaba",
        "params": "1.5B",
    },
    {
        "arm": "llama32b",
        "model": "llama3.2:3b-instruct-q4_K_M",
        "lab": "Meta",
        "params": "3B",
    },
)
