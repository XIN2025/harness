export type Interval = {
  readonly point: number;
  readonly low: number;
  readonly high: number;
  readonly method: string;
};

export type Metrics = {
  readonly precision: Interval;
  readonly recall: Interval;
  readonly f1: Interval;
};

export type MetricName = keyof Metrics;

export type Validity = {
  readonly total: number;
  readonly raw_valid: number;
  readonly parseable: number;
  readonly schema_valid: number;
};

export type Counts = {
  readonly tp: number;
  readonly fp: number;
  readonly fn: number;
  readonly unscored: number;
  readonly files: number;
};

export type ResultRow = {
  readonly label: string;
  readonly short: string;
  readonly note: string;
  readonly source: string;
  readonly arm: string;
  readonly split: string;
  readonly cut: string;
  readonly validity: Validity;
  readonly counts: Counts;
  readonly metrics: Metrics;
  readonly base?: Omit<ResultRow, "label" | "short" | "note" | "source">;
  readonly additions?: readonly string[];
};

export type OverlapRow = {
  readonly label: string;
  readonly short: string;
  readonly source: string;
  readonly arms: readonly string[];
  readonly cut: string;
  readonly formula: string;
  readonly limit: number;
  readonly max: number;
  readonly errors_by_arm: Readonly<Record<string, number>>;
  readonly ensemble_dropped: boolean;
};

export type HeadroomRow = {
  readonly repo: string;
  readonly idiom: string;
  readonly note: string;
  readonly source: string;
  readonly files: number;
  readonly edges: number;
  readonly parser_reached: number;
  readonly parser_missed: number;
  readonly parser_spurious: number;
  readonly unscored: number;
  readonly headroom: number;
  readonly recall: Interval;
};

export type UnscoreableRepo = {
  readonly repo: string;
  readonly reason: string;
};

export type Headroom = {
  readonly scored: readonly HeadroomRow[];
  readonly unscoreable: readonly UnscoreableRepo[];
};

export type Edge = readonly [caller: string, callee: string];

export type EdgeStatus = "matched" | "spurious" | "missed" | "unscored";

export type Panel = {
  readonly [K in EdgeStatus]: readonly Edge[];
};

export type FileEntry = {
  readonly path: string;
  readonly lines: number;
  readonly truth: readonly Edge[];
  readonly panels: Readonly<Record<string, Panel>>;
};

export type Model = {
  readonly arm: string;
  readonly model: string;
  readonly lab: string;
  readonly params: string;
};

export type ManifestSummary = {
  readonly path: string;
  readonly repo: string;
  readonly counts: Readonly<Record<string, number>>;
  readonly rule: Readonly<Record<string, string | number>>;
  readonly digest: string;
};

export type Meta = {
  readonly project: string;
  readonly split: string;
  readonly explorer_cut: string;
  readonly corpus: {
    readonly repo: string;
    readonly files: number;
    readonly oracle_edges: number;
    readonly manifest: ManifestSummary;
  };
  readonly models: readonly Model[];
  readonly prompts: number;
  readonly not_claimed: readonly string[];
  readonly explorer_panels: readonly string[];
};

export type OracleEval = {
  readonly meta: Meta;
  readonly curve: readonly ResultRow[];
  readonly baselines: readonly ResultRow[];
  readonly hybrid: readonly ResultRow[];
  readonly overlap: readonly OverlapRow[];
  readonly headroom: Headroom;
  readonly files: readonly FileEntry[];
};
