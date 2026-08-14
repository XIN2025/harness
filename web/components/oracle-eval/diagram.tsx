import type { ReactNode } from "react";

import { cn } from "@/lib/utils";

const ARROW_ID = "diagram-arrow";

export function DiagramDefs() {
  return (
    <defs>
      <marker
        id={ARROW_ID}
        viewBox="0 0 10 10"
        refX="9"
        refY="5"
        markerWidth="6"
        markerHeight="6"
        orient="auto-start-reverse"
      >
        <path d="M 0 0 L 10 5 L 0 10 z" fill="var(--border)" />
      </marker>
    </defs>
  );
}

export function DiagramFrame({
  viewBox,
  minWidth,
  label,
  caption,
  children,
  className,
}: {
  viewBox: string;
  minWidth: number;
  label: string;
  caption?: ReactNode;
  children: ReactNode;
  className?: string;
}) {
  return (
    <figure className={cn("m-0 min-w-0", className)}>
      <div className="-mx-1 overflow-x-auto px-1 pb-1">
        <svg
          viewBox={viewBox}
          role="img"
          aria-label={label}
          style={{ minWidth }}
          className="h-auto w-full"
        >
          <DiagramDefs />
          {children}
        </svg>
      </div>
      {caption ? (
        <figcaption className="mt-4 text-xs leading-relaxed text-muted-foreground">
          {caption}
        </figcaption>
      ) : null}
    </figure>
  );
}

export type NodeTone = "default" | "truth" | "brand" | "quiet";

const NODE_FILL: Readonly<Record<NodeTone, string>> = {
  default: "var(--background)",
  truth: "color-mix(in oklab, var(--truth) 7%, var(--background))",
  brand: "color-mix(in oklab, var(--brand) 8%, var(--background))",
  quiet: "var(--secondary)",
};

const NODE_STROKE: Readonly<Record<NodeTone, string>> = {
  default: "var(--border)",
  truth: "color-mix(in oklab, var(--truth) 40%, var(--border))",
  brand: "color-mix(in oklab, var(--brand) 40%, var(--border))",
  quiet: "var(--border)",
};

export function DiagramNode({
  x,
  y,
  width,
  height,
  title,
  lines = [],
  tone = "default",
}: {
  x: number;
  y: number;
  width: number;
  height: number;
  title: string;
  lines?: readonly string[];
  tone?: NodeTone;
}) {
  const cx = x + width / 2;
  const titleY = y + height / 2 - lines.length * 6 + 4;

  return (
    <g>
      <rect
        x={x}
        y={y}
        width={width}
        height={height}
        rx={10}
        fill={NODE_FILL[tone]}
        stroke={NODE_STROKE[tone]}
        strokeWidth={1}
      />
      <text
        x={cx}
        y={titleY}
        textAnchor="middle"
        fill="var(--foreground)"
        fontSize={12.5}
        fontWeight={500}
      >
        {title}
      </text>
      {lines.map((line, index) => (
        <text
          key={line}
          x={cx}
          y={titleY + 15 + index * 13}
          textAnchor="middle"
          fill="var(--muted-foreground)"
          fontSize={10.5}
          fontFamily="var(--font-mono)"
        >
          {line}
        </text>
      ))}
    </g>
  );
}

export function DiagramArrow({
  from,
  to,
  label,
  labelSide = "above",
  dashed = false,
}: {
  from: readonly [number, number];
  to: readonly [number, number];
  label?: string;
  labelSide?: "above" | "below" | "right";
  dashed?: boolean;
}) {
  const [x1, y1] = from;
  const [x2, y2] = to;
  const mx = (x1 + x2) / 2;
  const my = (y1 + y2) / 2;

  return (
    <g>
      <line
        x1={x1}
        y1={y1}
        x2={x2}
        y2={y2}
        stroke="var(--border)"
        strokeWidth={1.25}
        strokeDasharray={dashed ? "4 4" : undefined}
        markerEnd={`url(#${ARROW_ID})`}
      />
      {label ? (
        <text
          x={labelSide === "right" ? mx + 8 : mx}
          y={
            labelSide === "above"
              ? my - 7
              : labelSide === "below"
                ? my + 15
                : my + 4
          }
          textAnchor={labelSide === "right" ? "start" : "middle"}
          fill="var(--muted-foreground)"
          fontSize={10.5}
          fontFamily="var(--font-mono)"
        >
          {label}
        </text>
      ) : null}
    </g>
  );
}

export function DiagramLane({
  x,
  y,
  text,
}: {
  x: number;
  y: number;
  text: string;
}) {
  return (
    <text
      x={x}
      y={y}
      fill="var(--muted-foreground)"
      fontSize={10}
      fontWeight={500}
      letterSpacing="0.08em"
    >
      {text.toUpperCase()}
    </text>
  );
}
