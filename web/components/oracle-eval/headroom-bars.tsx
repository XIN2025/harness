import { pct } from "@/lib/oracle-eval/format";
import type { Headroom } from "@/lib/oracle-eval/types";

export function HeadroomBars({ headroom }: { headroom: Headroom }) {
  return (
    <div>
      <ol className="divide-y divide-border/60">
        {headroom.scored.map((row) => (
          <li key={row.source} className="py-6 first:pt-0">
            <div className="flex flex-wrap items-baseline justify-between gap-x-4 gap-y-1">
              <h3 className="text-sm font-medium">
                {row.repo}
                <span className="ml-2 text-xs font-normal text-muted-foreground">
                  {row.idiom}
                </span>
              </h3>
              <p className="font-mono text-sm font-medium tabular">
                {pct(row.headroom)}
                <span className="ml-2 text-xs font-normal text-muted-foreground">
                  {row.parser_missed} of {row.edges} edges
                </span>
              </p>
            </div>

            <div
              className="mt-3 h-2 w-full overflow-hidden rounded-full bg-secondary"
              role="img"
              aria-label={`${row.repo}: the parser misses ${pct(row.headroom)} of the oracle's ${row.edges} edges`}
            >
              <div
                className="h-full rounded-full bg-brand"
                style={{ width: `${Math.max(row.headroom * 100, 0.6)}%` }}
              />
            </div>

            <p className="mt-3 max-w-prose text-xs leading-relaxed text-muted-foreground">
              {row.note}
            </p>
            <p className="mt-1.5 font-mono text-[11px] break-all text-muted-foreground">
              {row.source}
            </p>
          </li>
        ))}
      </ol>

      {headroom.unscoreable.length > 0 ? (
        <div className="mt-8 rounded-2xl border border-border/70 p-5">
          <p className="text-sm font-medium">
            Frozen, and currently unscoreable on this cut
          </p>
          <dl className="mt-3 space-y-2">
            {headroom.unscoreable.map((repo) => (
              <div key={repo.repo} className="flex flex-wrap gap-x-3 text-xs">
                <dt className="font-mono text-foreground">{repo.repo}</dt>
                <dd className="max-w-prose flex-1 leading-relaxed text-muted-foreground">
                  {repo.reason}
                </dd>
              </div>
            ))}
          </dl>
        </div>
      ) : null}
    </div>
  );
}
