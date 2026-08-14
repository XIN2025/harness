import { edgeKey } from "./analysis";
import type { Edge, EdgeStatus, FileEntry, Panel } from "./types";

export const GRAPH = {
  width: 460,
  rowHeight: 24,
  padding: 18,
  callerX: 166,
  calleeX: 294,
  maxLabel: 24,
} as const;

export type GraphLayout = {
  readonly callers: ReadonlyMap<string, number>;
  readonly callees: ReadonlyMap<string, number>;
  readonly height: number;
};

function column(names: Iterable<string>): Map<string, number> {
  const sorted = [...new Set(names)].sort((a, b) => a.localeCompare(b));
  return new Map(
    sorted.map((name, index) => [
      name,
      GRAPH.padding + index * GRAPH.rowHeight + GRAPH.rowHeight / 2,
    ]),
  );
}

export function allEdges(file: FileEntry): readonly Edge[] {
  const seen = new Map<string, Edge>();
  const add = (edges: readonly Edge[]) => {
    for (const edge of edges) seen.set(edgeKey(edge), edge);
  };
  add(file.truth);
  for (const panel of Object.values(file.panels)) {
    add(panel.matched);
    add(panel.spurious);
    add(panel.missed);
    add(panel.unscored);
  }
  return [...seen.values()];
}

export function graphLayout(file: FileEntry): GraphLayout {
  const edges = allEdges(file);
  const callers = column(edges.map(([caller]) => caller));
  const callees = column(edges.map(([, callee]) => callee));
  const rows = Math.max(callers.size, callees.size);
  return {
    callers,
    callees,
    height: GRAPH.padding * 2 + Math.max(rows, 1) * GRAPH.rowHeight,
  };
}

export function clip(name: string): string {
  return name.length <= GRAPH.maxLabel
    ? name
    : `${name.slice(0, GRAPH.maxLabel - 1)}…`;
}

export function statusByEdge(panel: Panel): ReadonlyMap<string, EdgeStatus> {
  const statuses = new Map<string, EdgeStatus>();
  for (const edgeClass of EDGE_CLASSES) {
    for (const edge of panel[edgeClass.key]) {
      statuses.set(edgeKey(edge), edgeClass.key);
    }
  }
  return statuses;
}

export const EDGE_CLASSES = [
  {
    key: "matched",
    label: "matched",
    colour: "var(--matched)",
    mark: "●",
    dashed: false,
    meaning: "The arm named an edge the oracle has.",
  },
  {
    key: "spurious",
    label: "spurious",
    colour: "var(--spurious)",
    mark: "✕",
    dashed: false,
    meaning: "The arm named an edge the oracle does not have.",
  },
  {
    key: "missed",
    label: "missed",
    colour: "var(--missed)",
    mark: "○",
    dashed: true,
    meaning: "The oracle has this edge and the arm did not name it.",
  },
  {
    key: "unscored",
    label: "unscored",
    colour: "var(--unscored)",
    mark: "◇",
    dashed: true,
    meaning:
      "The arm named it, and the cut excludes the class it belongs to, so it is charged to neither side.",
  },
] as const satisfies readonly {
  key: keyof Panel;
  label: string;
  colour: string;
  mark: string;
  dashed: boolean;
  meaning: string;
}[];

export type EdgeClass = (typeof EDGE_CLASSES)[number];

export function edgeClass(status: EdgeStatus): EdgeClass {
  const found = EDGE_CLASSES.find((candidate) => candidate.key === status);
  if (!found) throw new Error(`oracle-eval: no edge class named ${status}`);
  return found;
}
