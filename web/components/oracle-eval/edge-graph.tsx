import {
  EDGE_CLASSES,
  GRAPH,
  type GraphLayout,
  clip,
} from "@/lib/oracle-eval/graph";
import type { Edge, Panel } from "@/lib/oracle-eval/types";
import { cn } from "@/lib/utils";

function EdgeLine({
  edge,
  layout,
  colour,
  dashed,
  label,
}: {
  edge: Edge;
  layout: GraphLayout;
  colour: string;
  dashed: boolean;
  label: string;
}) {
  const [caller, callee] = edge;
  const y1 = layout.callers.get(caller);
  const y2 = layout.callees.get(callee);
  if (y1 === undefined || y2 === undefined) return null;

  const control = (GRAPH.calleeX - GRAPH.callerX) * 0.45;
  return (
    <path
      d={`M ${GRAPH.callerX} ${y1} C ${GRAPH.callerX + control} ${y1}, ${GRAPH.calleeX - control} ${y2}, ${GRAPH.calleeX} ${y2}`}
      fill="none"
      stroke={colour}
      strokeWidth={1.4}
      strokeDasharray={dashed ? "4 3" : undefined}
      strokeOpacity={0.85}
      aria-label={`${caller} to ${callee}, ${label}`}
    />
  );
}

export function EdgeGraph({
  panel,
  layout,
  title,
  subtitle,
  className,
}: {
  panel: Panel;
  layout: GraphLayout;
  title: string;
  subtitle?: string;
  className?: string;
}) {
  const total =
    panel.matched.length +
    panel.spurious.length +
    panel.missed.length +
    panel.unscored.length;

  return (
    <figure className={cn("m-0 min-w-0", className)}>
      <figcaption className="flex flex-wrap items-baseline justify-between gap-x-3 gap-y-1">
        <span className="font-mono text-[13px] font-medium">{title}</span>
        {subtitle ? (
          <span className="text-xs text-muted-foreground">{subtitle}</span>
        ) : null}
      </figcaption>

      <div className="mt-3 overflow-x-auto">
        <svg
          viewBox={`0 0 ${GRAPH.width} ${layout.height}`}
          style={{ minWidth: 380 }}
          className="h-auto w-full"
          role="img"
          aria-label={`${title}: ${panel.matched.length} matched, ${panel.spurious.length} spurious, ${panel.missed.length} missed, ${panel.unscored.length} unscored`}
        >
          {[...layout.callers].map(([name, y]) => (
            <g key={`caller-${name}`}>
              <text
                x={GRAPH.callerX - 12}
                y={y + 3.5}
                textAnchor="end"
                fill="var(--foreground)"
                fontSize={11}
                fontFamily="var(--font-mono)"
              >
                {clip(name)}
              </text>
              <circle
                cx={GRAPH.callerX}
                cy={y}
                r={2.5}
                fill="var(--muted-foreground)"
              />
            </g>
          ))}

          {[...layout.callees].map(([name, y]) => (
            <g key={`callee-${name}`}>
              <circle
                cx={GRAPH.calleeX}
                cy={y}
                r={2.5}
                fill="var(--muted-foreground)"
              />
              <text
                x={GRAPH.calleeX + 12}
                y={y + 3.5}
                fill="var(--foreground)"
                fontSize={11}
                fontFamily="var(--font-mono)"
              >
                {clip(name)}
              </text>
            </g>
          ))}

          {EDGE_CLASSES.map((edgeClass) =>
            panel[edgeClass.key].map((edge) => (
              <EdgeLine
                key={`${edgeClass.key}-${edge[0]}-${edge[1]}`}
                edge={edge}
                layout={layout}
                colour={edgeClass.colour}
                dashed={edgeClass.dashed}
                label={edgeClass.label}
              />
            )),
          )}

          {total === 0 ? (
            <text
              x={GRAPH.width / 2}
              y={layout.height / 2}
              textAnchor="middle"
              fill="var(--muted-foreground)"
              fontSize={11}
            >
              no edges
            </text>
          ) : null}
        </svg>
      </div>
    </figure>
  );
}

export function EdgeLegend({ className }: { className?: string }) {
  return (
    <ul className={cn("flex flex-wrap gap-x-6 gap-y-2", className)}>
      {EDGE_CLASSES.map((edgeClass) => (
        <li key={edgeClass.key} className="flex items-center gap-2">
          <svg width={22} height={8} aria-hidden className="shrink-0">
            <line
              x1={0}
              y1={4}
              x2={22}
              y2={4}
              stroke={edgeClass.colour}
              strokeWidth={2}
              strokeDasharray={edgeClass.dashed ? "4 3" : undefined}
            />
          </svg>
          <span className="text-xs text-muted-foreground">
            <span className="font-medium text-foreground">
              {edgeClass.label}
            </span>
            : {edgeClass.meaning}
          </span>
        </li>
      ))}
    </ul>
  );
}
