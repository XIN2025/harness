import type { ReactNode } from "react";

import { cn } from "@/lib/utils";

function Chevron() {
  return (
    <svg
      viewBox="0 0 12 12"
      aria-hidden
      className="mt-[3px] size-3 shrink-0 text-muted-foreground transition-transform duration-200 group-open:rotate-90"
    >
      <path
        d="M4 2.5 L8 6 L4 9.5"
        fill="none"
        stroke="currentColor"
        strokeWidth="1.5"
        strokeLinecap="round"
        strokeLinejoin="round"
      />
    </svg>
  );
}

export function Disclosure({
  title,
  label,
  aside,
  children,
  className,
}: {
  title: string;
  label?: string;
  aside?: string;
  children: ReactNode;
  className?: string;
}) {
  return (
    <details
      className={cn(
        "group border-b border-border/60 last:border-b-0",
        className,
      )}
    >
      <summary className="flex cursor-pointer list-none items-start gap-3 py-4 transition-colors hover:text-foreground [&::-webkit-details-marker]:hidden">
        <Chevron />
        {label ? (
          <span className="mt-px font-mono text-[11px] text-muted-foreground tabular">
            {label}
          </span>
        ) : null}
        <span className="min-w-0 flex-1 text-sm font-medium">{title}</span>
        {aside ? (
          <span className="mt-px hidden shrink-0 font-mono text-[11px] text-muted-foreground sm:block">
            {aside}
          </span>
        ) : null}
      </summary>
      <div className="max-w-2xl pr-2 pb-5 pl-6 text-sm leading-relaxed text-muted-foreground">
        {children}
      </div>
    </details>
  );
}

export function DisclosureGroup({
  children,
  className,
}: {
  children: ReactNode;
  className?: string;
}) {
  return (
    <div
      className={cn(
        "rounded-3xl border border-border/70 px-5 sm:px-6",
        className,
      )}
    >
      {children}
    </div>
  );
}

export function DisclosureList({
  notes,
  className,
}: {
  notes: readonly {
    title: string;
    body: string;
    id?: string;
    aside?: string;
  }[];
  className?: string;
}) {
  return (
    <DisclosureGroup className={className}>
      {notes.map((note) => (
        <Disclosure
          key={note.title}
          title={note.title}
          label={note.id}
          aside={note.aside}
        >
          {note.body}
        </Disclosure>
      ))}
    </DisclosureGroup>
  );
}
