"use client";

import {
  IntervalMark,
  type MarkTone,
} from "@/components/oracle-eval/interval-mark";
import { Badge } from "@/components/ui/badge";
import {
  Tooltip,
  TooltipContent,
  TooltipTrigger,
} from "@/components/ui/tooltip";
import {
  VERDICT_LABEL,
  rawValidity,
  verdict,
} from "@/lib/oracle-eval/analysis";
import { intervalRange, pct, withInterval } from "@/lib/oracle-eval/format";
import type { MetricName, ResultRow } from "@/lib/oracle-eval/types";
import { cn } from "@/lib/utils";

const COLUMNS = "grid grid-cols-[minmax(0,1fr)_4rem] items-center gap-x-4";
const PLOT_INSET = "px-[5px]";
const TICKS = [0, 25, 50, 75, 100] as const;

const METRIC_LABEL: Readonly<Record<MetricName, string>> = {
  precision: "Precision",
  recall: "Recall",
  f1: "F1",
};

interface MetricPlotProps {
  rows: readonly ResultRow[];
  baseline?: ResultRow;
  metric?: MetricName;
}

function ValidityBadge({ row }: { row: ResultRow }) {
  const none = row.validity.raw_valid === 0;
  return (
    <Tooltip>
      <TooltipTrigger
        render={
          <Badge
            variant={none ? "destructive" : "secondary"}
            className="font-mono text-[11px] font-normal tabular"
          />
        }
      >
        raw JSON {row.validity.raw_valid}/{row.validity.total}
      </TooltipTrigger>
      <TooltipContent className="max-w-xs">
        Responses that parsed as JSON before any repair
        {none ? "" : `, ${pct(rawValidity(row), 1)}`}. Counted separately from
        accuracy and never blended into it.
      </TooltipContent>
    </Tooltip>
  );
}

function Detail({ row }: { row: ResultRow }) {
  const { counts, metrics } = row;
  return (
    <TooltipContent className="w-72 max-w-none p-0">
      <div className="w-full">
        <div className="border-b border-background/15 px-3 py-2">
          <p className="text-xs font-medium">{row.label}</p>
          <p className="mt-0.5 font-mono text-[11px] break-all text-background/60">
            {row.source}
          </p>
        </div>
        <dl className="grid grid-cols-[auto_1fr] gap-x-4 gap-y-1 px-3 py-2 font-mono text-[11px] tabular">
          {(["precision", "recall", "f1"] as const).map((name) => (
            <div key={name} className="contents">
              <dt className="text-background/60">{METRIC_LABEL[name]}</dt>
              <dd className="text-right whitespace-nowrap">
                {withInterval(metrics[name])}
              </dd>
            </div>
          ))}
          <div className="contents">
            <dt className="text-background/60">Right</dt>
            <dd className="text-right">{counts.tp}</dd>
          </div>
          <div className="contents">
            <dt className="text-background/60">Spurious</dt>
            <dd className="text-right">{counts.fp}</dd>
          </div>
          <div className="contents">
            <dt className="text-background/60">Missed</dt>
            <dd className="text-right">{counts.fn}</dd>
          </div>
        </dl>
      </div>
    </TooltipContent>
  );
}

function Row({
  row,
  metric,
  tone,
  isBaseline,
  baseline,
}: {
  row: ResultRow;
  metric: MetricName;
  tone: MarkTone;
  isBaseline: boolean;
  baseline?: ResultRow;
}) {
  const interval = row.metrics[metric];
  const result = baseline ? verdict(interval, baseline.metrics[metric]) : null;

  return (
    <li className="py-5 first:pt-0 last:pb-0">
      <div className="mb-3 flex flex-wrap items-center gap-x-3 gap-y-2">
        <h3 className="text-sm font-medium">{row.label}</h3>
        {isBaseline ? (
          <Badge variant="outline" className="text-[11px] font-normal">
            baseline
          </Badge>
        ) : (
          <ValidityBadge row={row} />
        )}
      </div>

      <div className={COLUMNS}>
        <Tooltip>
          <TooltipTrigger
            render={<div className={cn("cursor-default py-1.5", PLOT_INSET)} />}
          >
            <IntervalMark
              interval={interval}
              label={`${row.label} ${METRIC_LABEL[metric]}`}
              tone={tone}
            />
          </TooltipTrigger>
          <Detail row={row} />
        </Tooltip>
        <span className="text-right text-sm font-medium tabular">
          {pct(interval.point)}
        </span>
      </div>

      <div className={cn(COLUMNS, "mt-2")}>
        <p className="max-w-prose text-xs leading-relaxed text-muted-foreground">
          {row.note}
          {result && !isBaseline ? (
            <>
              {" "}
              <span
                className={cn(
                  "font-medium",
                  result === "measured-gain" ? "text-foreground" : "",
                )}
              >
                {VERDICT_LABEL[result]} vs baseline.
              </span>
            </>
          ) : null}
        </p>
        <span className="text-right font-mono text-[11px] text-muted-foreground tabular">
          {intervalRange(interval)}
        </span>
      </div>
    </li>
  );
}

export function MetricPlot({ rows, baseline, metric = "f1" }: MetricPlotProps) {
  if (rows.length === 0) {
    return (
      <p className="py-6 text-sm text-muted-foreground">
        No results have been exported yet.
      </p>
    );
  }

  return (
    <div>
      <div className="relative">
        <div
          aria-hidden
          className={cn(COLUMNS, "pointer-events-none absolute inset-0")}
        >
          <div className={cn("relative h-full", PLOT_INSET)}>
            {TICKS.map((tick) => (
              <span
                key={tick}
                className="absolute inset-y-0 w-px bg-border/60"
                style={{ left: `${tick}%` }}
              />
            ))}
          </div>
        </div>

        <ol className="relative divide-y divide-border/60">
          {rows.map((row) => {
            const isBaseline = baseline?.source === row.source;
            const tone: MarkTone =
              !baseline || isBaseline
                ? baseline
                  ? "muted"
                  : "brand"
                : verdict(row.metrics[metric], baseline.metrics[metric]) ===
                    "measured-gain"
                  ? "brand"
                  : "muted";
            return (
              <Row
                key={row.source}
                row={row}
                metric={metric}
                tone={tone}
                isBaseline={isBaseline}
                baseline={baseline}
              />
            );
          })}
        </ol>
      </div>

      <div className={cn(COLUMNS, "mt-4")}>
        <div className={cn("relative h-4", PLOT_INSET)}>
          {TICKS.map((tick, index) => (
            <span
              key={tick}
              className={cn(
                "absolute top-0 font-mono text-[11px] text-muted-foreground tabular",
                index === 0
                  ? "translate-x-0"
                  : index === TICKS.length - 1
                    ? "-translate-x-full"
                    : "-translate-x-1/2",
              )}
              style={{ left: `${tick}%` }}
            >
              {tick}
            </span>
          ))}
        </div>
        <span className="text-right font-mono text-[11px] text-muted-foreground">
          {METRIC_LABEL[metric]} %
        </span>
      </div>
    </div>
  );
}
