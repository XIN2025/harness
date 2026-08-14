import { cn } from "@/lib/utils";

export type Stat = {
  value: string;
  from?: string;
  label: string;
  detail: string;
};

export function StatRow({
  stats,
  className,
}: {
  stats: readonly Stat[];
  className?: string;
}) {
  return (
    <dl
      className={cn(
        "grid gap-px overflow-hidden rounded-3xl border border-border/70 bg-border/70 sm:grid-cols-3",
        className,
      )}
    >
      {stats.map((stat) => (
        <div key={stat.label} className="bg-background p-6 md:p-7">
          <dt className="text-[11px] font-medium tracking-[0.08em] text-muted-foreground uppercase">
            {stat.label}
          </dt>
          <dd className="mt-4 flex items-baseline gap-1.5 whitespace-nowrap sm:gap-2">
            {stat.from && (
              <>
                <span className="text-base font-medium text-muted-foreground lg:text-xl">
                  {stat.from}
                </span>
                <span
                  aria-hidden
                  className="text-sm text-muted-foreground/70 lg:text-lg"
                >
                  →
                </span>
              </>
            )}
            <span className="text-[1.75rem] leading-none font-semibold tracking-[-0.03em] sm:text-[2rem] lg:text-[2.5rem]">
              {stat.value}
            </span>
          </dd>
          <p className="mt-4 text-[13px] leading-relaxed text-muted-foreground">
            {stat.detail}
          </p>
        </div>
      ))}
    </dl>
  );
}
