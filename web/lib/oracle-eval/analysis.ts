import type { Edge, FileEntry, Interval, ResultRow } from "./types";

export function intervalsOverlap(a: Interval, b: Interval): boolean {
  return a.low <= b.high && b.low <= a.high;
}

export type Verdict = "measured-gain" | "measured-loss" | "no-measured-change";

export function verdict(subject: Interval, baseline: Interval): Verdict {
  if (intervalsOverlap(subject, baseline)) return "no-measured-change";
  return subject.point > baseline.point ? "measured-gain" : "measured-loss";
}

export const VERDICT_LABEL: Readonly<Record<Verdict, string>> = {
  "measured-gain": "measured gain",
  "measured-loss": "measured loss",
  "no-measured-change": "no measured change",
};

export type CutBreakdown = {
  readonly invocations: number;
  readonly refs: number;
  readonly fullEdges: number;
  readonly parserReached: number;
  readonly parserMissedInvocations: number;
  readonly parserReachedRefs: number;
  readonly agreementAdded: number;
  readonly agreementFalse: number;
  readonly agreementMissed: number;
};

export function cutBreakdown(
  parserPrimary: ResultRow,
  parserFull: ResultRow,
  agreement: ResultRow,
): CutBreakdown {
  const invocations = parserPrimary.counts.tp + parserPrimary.counts.fn;
  const fullEdges = parserFull.counts.tp + parserFull.counts.fn;
  return {
    invocations,
    refs: fullEdges - invocations,
    fullEdges,
    parserReached: parserPrimary.counts.tp,
    parserMissedInvocations: parserPrimary.counts.fn,
    parserReachedRefs: parserFull.counts.tp - parserPrimary.counts.tp,
    agreementAdded: agreement.counts.tp - parserFull.counts.tp,
    agreementFalse: agreement.counts.fp,
    agreementMissed: agreement.counts.fn,
  };
}

export function rawValidity(row: ResultRow): number {
  return row.validity.total === 0
    ? 0
    : row.validity.raw_valid / row.validity.total;
}

export function disagreement(file: FileEntry): number {
  return Object.values(file.panels).reduce(
    (total, panel) => total + panel.spurious.length + panel.missed.length,
    0,
  );
}

export function fileSlug(path: string): string {
  return path.replace(/\//g, "__");
}

export function pathFromSlug(slug: string): string {
  return slug.replace(/__/g, "/");
}

export function edgeKey(edge: Edge): string {
  return `${edge[0]} -> ${edge[1]}`;
}
