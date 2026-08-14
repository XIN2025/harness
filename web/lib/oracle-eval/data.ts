import rawExport from "@/data/oracle-eval.json";
import { disagreement, fileSlug } from "./analysis";
import type {
  FileEntry,
  Headroom,
  OracleEval,
  OverlapRow,
  ResultRow,
} from "./types";

const oracleEval = rawExport as unknown as OracleEval;

export const meta = oracleEval.meta;
export const curve: readonly ResultRow[] = oracleEval.curve;
export const baselines: readonly ResultRow[] = oracleEval.baselines;
export const hybrid: readonly ResultRow[] = oracleEval.hybrid;
export const overlap: readonly OverlapRow[] = oracleEval.overlap;
export const headroom: Headroom = oracleEval.headroom;
export const files: readonly FileEntry[] = oracleEval.files;

export const SOURCE = {
  parserPrimary: "treesitter.dev.calls_only.json",
  parserFull: "treesitter.dev.full.json",
  theirPrompt: "qwen15b-theirs.dev.calls_only.json",
  qwenPrompted: "qwen15b-calls.dev.calls_only.json",
  llamaPrompted: "llama32b-calls.dev.calls_only.json",
  qwenUnion: "hybrid-treesitter-qwen15b-refs.dev.full.json",
  llamaUnion: "hybrid-treesitter-llama32b-refs.dev.full.json",
  agreementRound1: "hybrid-treesitter-qwen15b-refs-llama32b-refs.dev.full.json",
  agreementRound2:
    "hybrid-treesitter-qwen15b-refs-strict-llama32b-refs-strict.dev.full.json",
} as const;

export function bySource(
  rows: readonly ResultRow[],
  source: string,
): ResultRow {
  const row = rows.find((candidate) => candidate.source === source);
  if (!row) {
    throw new Error(
      `oracle-eval: no exported result named ${source}. The pages' headline ` +
        "figures are derived from published results, not written by hand.",
    );
  }
  return row;
}

export function filesWorstFirst(): readonly FileEntry[] {
  return [...files].sort(
    (a, b) => disagreement(b) - disagreement(a) || a.path.localeCompare(b.path),
  );
}

export function fileByPath(path: string): FileEntry | undefined {
  return files.find((file) => file.path === path);
}

export type Reconciliation = {
  readonly arm: string;
  readonly label: string;
  readonly source: string;
  readonly published: {
    readonly tp: number;
    readonly fp: number;
    readonly fn: number;
  };
  readonly recomputed: {
    readonly tp: number;
    readonly fp: number;
    readonly fn: number;
  };
  readonly agrees: boolean;
};

function sumPanel(arm: string): { tp: number; fp: number; fn: number } {
  return files.reduce(
    (total, file) => {
      const panel = file.panels[arm];
      if (!panel) return total;
      return {
        tp: total.tp + panel.matched.length,
        fp: total.fp + panel.spurious.length,
        fn: total.fn + panel.missed.length,
      };
    },
    { tp: 0, fp: 0, fn: 0 },
  );
}

export function reconciliation(): readonly Reconciliation[] {
  const pairs = [
    { arm: "treesitter", row: bySource(hybrid, SOURCE.parserFull) },
    { arm: "hybrid", row: bySource(hybrid, SOURCE.agreementRound1) },
  ];

  return pairs.map(({ arm, row }) => {
    const recomputed = sumPanel(arm);
    const published = {
      tp: row.counts.tp,
      fp: row.counts.fp,
      fn: row.counts.fn,
    };
    return {
      arm,
      label: row.label,
      source: row.source,
      published,
      recomputed,
      agrees:
        published.tp === recomputed.tp &&
        published.fp === recomputed.fp &&
        published.fn === recomputed.fn,
    };
  });
}

export type FileSummary = {
  readonly path: string;
  readonly slug: string;
  readonly lines: number;
  readonly truth: number;
  readonly disagreement: number;
  readonly panels: Readonly<
    Record<
      string,
      {
        readonly matched: number;
        readonly spurious: number;
        readonly missed: number;
      }
    >
  >;
};

export function fileSummaries(): readonly FileSummary[] {
  return filesWorstFirst().map((file) => ({
    path: file.path,
    slug: fileSlug(file.path),
    lines: file.lines,
    truth: file.truth.length,
    disagreement: disagreement(file),
    panels: Object.fromEntries(
      Object.entries(file.panels).map(([arm, panel]) => [
        arm,
        {
          matched: panel.matched.length,
          spurious: panel.spurious.length,
          missed: panel.missed.length,
        },
      ]),
    ),
  }));
}
