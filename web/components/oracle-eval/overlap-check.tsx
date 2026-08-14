import { pct } from "@/lib/oracle-eval/format";
import type { OverlapRow } from "@/lib/oracle-eval/types";
import { cn } from "@/lib/utils";

export function OverlapCheck({ rows }: { rows: readonly OverlapRow[] }) {
  const limit = rows[0]?.limit ?? 0.8;
  const sameLimit = rows.every((row) => row.limit === limit);

  return (
    <div>
      <div className="relative">
        {sameLimit ? (
          <div
            aria-hidden
            className="pointer-events-none absolute inset-y-0 z-10 border-l border-dashed border-foreground/40"
            style={{ left: `${limit * 100}%` }}
          >
            <span className="absolute -top-1 left-2 font-mono text-[11px] whitespace-nowrap text-muted-foreground">
              {pct(limit, 0)} limit
            </span>
          </div>
        ) : null}

        <ol className="space-y-6 pt-7">
          {rows.map((row) => {
            const arms = Object.entries(row.errors_by_arm);
            return (
              <li key={row.source}>
                <div className="flex flex-wrap items-baseline justify-between gap-x-4 gap-y-1">
                  <h3 className="text-sm font-medium">
                    {row.short}
                    <span className="ml-2 font-mono text-xs font-normal text-muted-foreground">
                      {row.cut}
                    </span>
                  </h3>
                  <p
                    className={cn(
                      "font-mono text-sm font-medium tabular",
                      row.ensemble_dropped && "text-spurious",
                    )}
                  >
                    {pct(row.max)}
                  </p>
                </div>

                <div
                  className="mt-2 h-2.5 w-full overflow-hidden rounded-full bg-secondary"
                  role="img"
                  aria-label={`${row.short}: error overlap ${pct(row.max)} against a ${pct(limit, 0)} limit, ${row.ensemble_dropped ? "over the limit, ensemble dropped" : "under the limit, ensemble reported"}`}
                >
                  <div
                    className={cn(
                      "h-full rounded-full",
                      row.ensemble_dropped ? "bg-spurious" : "bg-foreground/70",
                    )}
                    style={{ width: `${row.max * 100}%` }}
                  />
                </div>

                <p className="mt-2 text-xs leading-relaxed text-muted-foreground">
                  {arms.map(([arm, errors], index) => (
                    <span key={arm}>
                      {index > 0 ? " · " : ""}
                      <span className="font-mono">{arm}</span> {errors} wrong
                    </span>
                  ))}
                  {row.ensemble_dropped ? (
                    <span className="ml-2 font-medium text-foreground">
                      Over the limit, so this ensemble was dropped rather than
                      reported.
                    </span>
                  ) : (
                    <span className="ml-2">
                      Under the limit, so the two arms may be combined.
                    </span>
                  )}
                </p>
              </li>
            );
          })}
        </ol>
      </div>

      <p className="mt-8 border-t border-border/60 pt-4 font-mono text-[11px] leading-relaxed text-muted-foreground">
        {rows[0]?.formula}
      </p>
    </div>
  );
}
