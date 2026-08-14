import { REGISTERED_OUTCOMES } from "@/lib/oracle-eval/narrative";
import { cn } from "@/lib/utils";

export function RegisteredOutcomes() {
  return (
    <ol className="grid gap-px overflow-hidden rounded-3xl border border-border/70 bg-border/70 md:grid-cols-3">
      {REGISTERED_OUTCOMES.map((outcome) => (
        <li
          key={outcome.condition}
          className={cn(
            "flex flex-col bg-background p-6",
            outcome.fired && "bg-brand/5",
          )}
        >
          <p className="font-mono text-[11px] tracking-wide text-muted-foreground">
            if
          </p>
          <h3 className="mt-2 text-base font-medium tracking-tight">
            {outcome.condition}
          </h3>
          <p className="mt-3 flex-1 text-[13px] leading-relaxed text-muted-foreground">
            {outcome.consequence}
          </p>
          <p
            className={cn(
              "mt-5 border-t border-border/70 pt-4 text-[13px] leading-relaxed",
              outcome.fired
                ? "font-medium text-foreground"
                : "text-muted-foreground",
            )}
          >
            <span
              className={cn(
                "mr-2 font-mono text-[11px]",
                outcome.fired ? "text-brand" : "text-muted-foreground",
              )}
            >
              {outcome.fired ? "fired" : "did not fire"}
            </span>
            {outcome.actual}
          </p>
        </li>
      ))}
    </ol>
  );
}
