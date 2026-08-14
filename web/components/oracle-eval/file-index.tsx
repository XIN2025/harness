"use client";

import Link from "next/link";
import { useMemo, useState } from "react";

import { Input } from "@/components/ui/input";
import type { FileSummary } from "@/lib/oracle-eval/data";

function Triple({
  panel,
}: {
  panel?: { matched: number; spurious: number; missed: number };
}) {
  if (!panel) return <span className="text-muted-foreground/50">·</span>;
  return (
    <span className="font-mono text-[11px] tabular">
      <span className="text-matched">{panel.matched}</span>
      <span className="text-muted-foreground"> · </span>
      <span
        className={
          panel.spurious > 0 ? "text-spurious" : "text-muted-foreground"
        }
      >
        {panel.spurious}
      </span>
      <span className="text-muted-foreground"> · </span>
      <span
        className={
          panel.missed > 0 ? "text-foreground" : "text-muted-foreground"
        }
      >
        {panel.missed}
      </span>
    </span>
  );
}

export function FileIndex({
  summaries,
  base,
  hybrid,
}: {
  summaries: readonly FileSummary[];
  base: string;
  hybrid: string;
}) {
  const [query, setQuery] = useState("");

  const shown = useMemo(() => {
    const needle = query.trim().toLowerCase();
    if (!needle) return summaries;
    return summaries.filter((file) => file.path.toLowerCase().includes(needle));
  }, [query, summaries]);

  return (
    <div>
      <div className="flex flex-wrap items-center justify-between gap-4">
        <label className="w-full max-w-xs">
          <span className="sr-only">Filter files by path</span>
          <Input
            type="search"
            value={query}
            onChange={(event) => setQuery(event.target.value)}
            placeholder="Filter by path…"
          />
        </label>
        <p className="font-mono text-xs text-muted-foreground tabular">
          {shown.length} of {summaries.length} files
        </p>
      </div>

      <div className="mt-6 overflow-x-auto">
        <table className="w-full min-w-[640px] border-collapse text-[13px]">
          <caption className="caption-bottom pt-4 text-left text-xs text-muted-foreground">
            Sorted by how loudly the arms disagree. Each triple is{" "}
            <span className="text-matched">matched</span> ·{" "}
            <span className="text-spurious">spurious</span> · missed, against
            the oracle for that file.
          </caption>
          <thead>
            <tr className="border-b border-border text-left">
              <th className="py-2 pr-4 font-medium">File</th>
              <th className="py-2 pr-4 text-right font-medium">Lines</th>
              <th className="py-2 pr-4 text-right font-medium">Oracle</th>
              <th className="py-2 pr-4 text-right font-medium whitespace-nowrap">
                tree-sitter
              </th>
              <th className="py-2 text-right font-medium">hybrid</th>
            </tr>
          </thead>
          <tbody>
            {shown.map((file) => (
              <tr
                key={file.path}
                className="border-b border-border/60 transition-colors hover:bg-accent"
              >
                <td className="py-2 pr-4">
                  <Link
                    href={`/explorer/${file.slug}`}
                    className="font-mono text-[12px] underline-offset-4 hover:underline"
                  >
                    {file.path}
                  </Link>
                </td>
                <td className="py-2 pr-4 text-right font-mono text-[11px] text-muted-foreground tabular">
                  {file.lines}
                </td>
                <td className="py-2 pr-4 text-right font-mono text-[11px] tabular">
                  {file.truth}
                </td>
                <td className="py-2 pr-4 text-right">
                  <Triple panel={file.panels[base]} />
                </td>
                <td className="py-2 text-right">
                  <Triple panel={file.panels[hybrid]} />
                </td>
              </tr>
            ))}
          </tbody>
        </table>
      </div>

      {shown.length === 0 ? (
        <p className="mt-6 text-sm text-muted-foreground">
          No file in the frozen corpus matches that path.
        </p>
      ) : null}
    </div>
  );
}
