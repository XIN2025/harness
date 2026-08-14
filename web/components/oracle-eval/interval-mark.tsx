import { withInterval } from "@/lib/oracle-eval/format";
import type { Interval } from "@/lib/oracle-eval/types";
import { cn } from "@/lib/utils";

const TONE = {
  brand: { band: "bg-brand/30", dot: "bg-brand" },
  muted: { band: "bg-foreground/15", dot: "bg-muted-foreground" },
} as const;

export type MarkTone = keyof typeof TONE;

interface IntervalMarkProps {
  interval: Interval;
  label: string;
  tone?: MarkTone;
  className?: string;
}

export function IntervalMark({
  interval,
  label,
  tone = "brand",
  className,
}: IntervalMarkProps) {
  const clamp = (value: number) => Math.min(100, Math.max(0, value * 100));
  const low = clamp(interval.low);
  const high = clamp(interval.high);
  const point = clamp(interval.point);
  const { band, dot } = TONE[tone];

  const width = Math.max(high - low, 0.6);
  const left = Math.min(low, 100 - width);

  return (
    <div
      role="img"
      aria-label={`${label}: ${withInterval(interval)}`}
      className={cn("relative h-2.5 w-full", className)}
    >
      <div
        className={cn(
          "absolute top-1/2 h-2.5 -translate-y-1/2 rounded-full",
          band,
        )}
        style={{ left: `${left}%`, width: `${width}%` }}
      />
      <div
        className={cn(
          "absolute top-1/2 size-2.5 -translate-x-1/2 -translate-y-1/2 rounded-full ring-2 ring-background",
          dot,
        )}
        style={{ left: `${point}%` }}
      />
    </div>
  );
}
