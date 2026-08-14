import type { ReactNode } from "react";

import { cn } from "@/lib/utils";

export function PageHeader({
  eyebrow,
  title,
  lede,
  children,
}: {
  eyebrow?: ReactNode;
  title: string;
  lede?: ReactNode;
  children?: ReactNode;
}) {
  return (
    <header className="mx-auto w-full max-w-5xl px-6 pt-12 pb-8 md:pt-16 md:pb-10">
      {eyebrow ? (
        <p className="font-mono text-xs tracking-wide text-muted-foreground">
          {eyebrow}
        </p>
      ) : null}
      <h1 className="mt-4 max-w-3xl text-[clamp(1.875rem,4.5vw,3rem)] leading-[1.08] font-semibold tracking-[-0.03em] text-balance">
        {title}
      </h1>
      {lede ? (
        <p className="mt-5 max-w-2xl text-lg leading-relaxed text-muted-foreground">
          {lede}
        </p>
      ) : null}
      {children}
    </header>
  );
}

export function Section({
  id,
  title,
  lede,
  children,
  className,
}: {
  id?: string;
  title?: string;
  lede?: ReactNode;
  children: ReactNode;
  className?: string;
}) {
  return (
    <section
      id={id}
      className={cn(
        "mx-auto w-full max-w-5xl scroll-mt-14 px-6 py-12 md:py-16",
        className,
      )}
    >
      {title ? (
        <h2 className="text-xl font-semibold tracking-tight md:text-2xl">
          {title}
        </h2>
      ) : null}
      {lede ? (
        <div className="mt-3 max-w-2xl leading-relaxed text-muted-foreground">
          {lede}
        </div>
      ) : null}
      {children}
    </section>
  );
}
