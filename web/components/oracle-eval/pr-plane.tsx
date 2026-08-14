import type { ReactNode } from "react";

import { pct } from "@/lib/oracle-eval/format";
import type { ResultRow } from "@/lib/oracle-eval/types";

const W = 560;
const H = 380;
const PAD = { left: 52, right: 22, top: 22, bottom: 46 } as const;
const PLOT_W = W - PAD.left - PAD.right;
const PLOT_H = H - PAD.top - PAD.bottom;
const CLIP_ID = "pr-plane-clip";
const MARK_INSET = 12;

const ISO_F1 = [0.5, 0.6, 0.7, 0.8, 0.9, 0.95] as const;

export type PrPoint = {
  readonly row: ResultRow;
  readonly emphasis?: boolean;
};

type Domain = { readonly min: number; readonly max: number };

function domainOf(values: readonly number[]): Domain {
  const low = Math.min(...values);
  const high = Math.max(...values);
  const min = Math.max(0, Math.floor((low - 0.04) * 20) / 20);
  const max = Math.min(1, Math.ceil((high + 0.04) * 20) / 20);
  if (max - min >= 0.25) return { min, max };
  const centre = (min + max) / 2;
  return {
    min: Math.max(0, Math.min(centre - 0.125, 1 - 0.25)),
    max: Math.min(1, Math.max(centre + 0.125, 0.25)),
  };
}

function ticksOf({ min, max }: Domain): readonly number[] {
  const span = (max - min) * 100;
  const step = [5, 10, 20, 25].find((candidate) => span / candidate <= 5) ?? 25;
  const ticks: number[] = [];
  for (
    let value = Math.ceil((min * 100) / step) * step;
    value <= max * 100 + 1e-9;
    value += step
  ) {
    ticks.push(value / 100);
  }
  return ticks;
}

function isoPrecision(f1: number, recall: number): number | null {
  const denominator = 2 * recall - f1;
  if (denominator <= 0) return null;
  const precision = (f1 * recall) / denominator;
  return precision > 1 ? null : precision;
}

export function PrecisionRecallPlane({
  points,
  cut,
  caption,
}: {
  points: readonly PrPoint[];
  cut: string;
  caption?: ReactNode;
}) {
  const recall = domainOf(
    points.flatMap(({ row }) => [
      row.metrics.recall.low,
      row.metrics.recall.high,
    ]),
  );
  const precision = domainOf(
    points.flatMap(({ row }) => [
      row.metrics.precision.low,
      row.metrics.precision.high,
    ]),
  );

  const x = (value: number) =>
    PAD.left +
    MARK_INSET +
    ((value - recall.min) / (recall.max - recall.min)) *
      (PLOT_W - MARK_INSET * 2);
  const y = (value: number) =>
    PAD.top +
    MARK_INSET +
    (1 - (value - precision.min) / (precision.max - precision.min)) *
      (PLOT_H - MARK_INSET * 2);

  const isoPath = (f1: number): string => {
    const steps = 240;
    const points: string[] = [];
    for (let step = 0; step <= steps; step += 1) {
      const r = recall.min + ((recall.max - recall.min) * step) / steps;
      const p = isoPrecision(f1, r);
      if (p === null) continue;
      points.push(`${points.length === 0 ? "M" : "L"} ${x(r)} ${y(p)}`);
    }
    return points.join(" ");
  };

  return (
    <figure className="m-0 grid gap-8 lg:grid-cols-[minmax(0,1.5fr)_minmax(0,1fr)] lg:items-center">
      <div className="-mx-1 min-w-0 overflow-x-auto px-1">
        <svg
          viewBox={`0 0 ${W} ${H}`}
          style={{ minWidth: 420 }}
          className="h-auto w-full"
          role="img"
          aria-label={`Precision against recall on the ${cut} cut. ${points
            .map(
              ({ row }, index) =>
                `Point ${index + 1}, ${row.short}: recall ${pct(row.metrics.recall.point)}, precision ${pct(row.metrics.precision.point)}`,
            )
            .join(". ")}.`}
        >
          <defs>
            <clipPath id={CLIP_ID}>
              <rect x={PAD.left} y={PAD.top} width={PLOT_W} height={PLOT_H} />
            </clipPath>
          </defs>

          <g clipPath={`url(#${CLIP_ID})`}>
            {ISO_F1.map((f1) => (
              <path
                key={f1}
                d={isoPath(f1)}
                fill="none"
                stroke="var(--border)"
                strokeWidth={1}
                strokeDasharray="3 4"
              />
            ))}
            {ISO_F1.map((f1) => {
              const p = isoPrecision(f1, recall.max);
              if (p === null || p < precision.min || p > precision.max)
                return null;
              return (
                <text
                  key={`label-${f1}`}
                  x={x(recall.max) - 6}
                  y={y(p) - 5}
                  textAnchor="end"
                  fill="var(--muted-foreground)"
                  fontSize={9.5}
                  fontFamily="var(--font-mono)"
                >
                  F1 {f1}
                </text>
              );
            })}
          </g>

          <line
            x1={PAD.left}
            y1={PAD.top}
            x2={PAD.left}
            y2={PAD.top + PLOT_H}
            stroke="var(--border)"
          />
          <line
            x1={PAD.left}
            y1={PAD.top + PLOT_H}
            x2={PAD.left + PLOT_W}
            y2={PAD.top + PLOT_H}
            stroke="var(--border)"
          />

          {ticksOf(recall).map((tick) => (
            <text
              key={`x-${tick}`}
              x={x(tick)}
              y={PAD.top + PLOT_H + 18}
              textAnchor="middle"
              fill="var(--muted-foreground)"
              fontSize={10}
              fontFamily="var(--font-mono)"
            >
              {(tick * 100).toFixed(0)}
            </text>
          ))}
          {ticksOf(precision).map((tick) => (
            <text
              key={`y-${tick}`}
              x={PAD.left - 10}
              y={y(tick) + 3.5}
              textAnchor="end"
              fill="var(--muted-foreground)"
              fontSize={10}
              fontFamily="var(--font-mono)"
            >
              {(tick * 100).toFixed(0)}
            </text>
          ))}

          <text
            x={PAD.left + PLOT_W / 2}
            y={H - 8}
            textAnchor="middle"
            fill="var(--muted-foreground)"
            fontSize={11}
          >
            Recall %
          </text>
          <text
            x={-(PAD.top + PLOT_H / 2)}
            y={14}
            transform="rotate(-90)"
            textAnchor="middle"
            fill="var(--muted-foreground)"
            fontSize={11}
          >
            Precision %
          </text>
          {points.map(({ row, emphasis = false }, index) => {
            const cx = x(row.metrics.recall.point);
            const cy = y(row.metrics.precision.point);
            const colour = emphasis ? "var(--brand)" : "var(--foreground)";
            return (
              <g key={row.source}>
                <line
                  x1={x(row.metrics.recall.low)}
                  y1={cy}
                  x2={x(row.metrics.recall.high)}
                  y2={cy}
                  stroke={colour}
                  strokeOpacity={0.25}
                  strokeWidth={1.5}
                />
                <line
                  x1={cx}
                  y1={y(row.metrics.precision.low)}
                  x2={cx}
                  y2={y(row.metrics.precision.high)}
                  stroke={colour}
                  strokeOpacity={0.25}
                  strokeWidth={1.5}
                />
                <circle
                  cx={cx}
                  cy={cy}
                  r={9}
                  fill={emphasis ? colour : "var(--background)"}
                  stroke={colour}
                  strokeWidth={1.5}
                />
                <text
                  x={cx}
                  y={cy + 3.5}
                  textAnchor="middle"
                  fill={
                    emphasis ? "var(--brand-foreground)" : "var(--foreground)"
                  }
                  fontSize={10}
                  fontWeight={600}
                  pointerEvents="none"
                >
                  {index + 1}
                </text>
              </g>
            );
          })}
        </svg>
      </div>

      <figcaption className="min-w-0">
        <p className="mb-4 font-mono text-[11px] text-muted-foreground">
          {cut} cut · axes clipped to the data
        </p>
        <ol className="space-y-3">
          {points.map(({ row, emphasis = false }, index) => (
            <li key={row.source} className="flex gap-3">
              <span
                className={
                  emphasis
                    ? "mt-px flex size-5 shrink-0 items-center justify-center rounded-full bg-brand text-[10px] font-semibold text-brand-foreground"
                    : "mt-px flex size-5 shrink-0 items-center justify-center rounded-full border border-foreground/40 text-[10px] font-semibold"
                }
              >
                {index + 1}
              </span>
              <span className="min-w-0">
                <span className="block text-[13px] font-medium">
                  {row.short}
                </span>
                <span className="mt-0.5 block font-mono text-[11px] text-muted-foreground tabular">
                  P {pct(row.metrics.precision.point)} · R{" "}
                  {pct(row.metrics.recall.point)} · F1{" "}
                  {pct(row.metrics.f1.point)}
                </span>
              </span>
            </li>
          ))}
        </ol>
        {caption ? (
          <p className="mt-6 text-xs leading-relaxed text-muted-foreground">
            {caption}
          </p>
        ) : null}
      </figcaption>
    </figure>
  );
}
