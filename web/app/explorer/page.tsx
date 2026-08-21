import type { Metadata } from "next";

import { EdgeLegend } from "@/components/oracle-eval/edge-graph";
import { FileIndex } from "@/components/oracle-eval/file-index";
import { PageHeader, Section } from "@/components/site/section";
import { Separator } from "@/components/ui/separator";
import { fileSummaries, meta, reconciliation } from "@/lib/oracle-eval/data";
import { cn } from "@/lib/utils";

export const metadata: Metadata = {
  title: "Explorer",
  description: `All ${meta.corpus.files} scored files, edge by edge: each arm's answer beside the oracle's, with the loudest disagreements first.`,
};

export default function ExplorerPage() {
  const summaries = fileSummaries();
  const checks = reconciliation();
  const [base] = meta.explorer_panels;
  const hybridPanel =
    meta.explorer_panels[meta.explorer_panels.length - 1] ?? base;

  return (
    <>
      <PageHeader
        eyebrow={`Explorer · ${meta.explorer_cut} cut · ${meta.corpus.files} files`}
        title="Every score, down to the edge that produced it"
        lede={
          <>
            Summary metrics on this site are copied out of the harness&apos;s
            published results. The per-file classifications below are something
            else: they are <em>recomputed</em>, by calling the harness&apos;s
            own scoring functions on the same stored responses. So a number here
            can be walked back to a named caller and callee in a named file, and
            the two halves have to agree.
          </>
        }
      />

      <Section
        id="reconciliation"
        title="They agree"
        lede={`Summed over all ${meta.corpus.files} files, the recomputed panels against the published totals. If these ever disagreed, the explorer would be illustrating a claim rather than checking one.`}
      >
        <ul className="mt-8 grid gap-4 sm:grid-cols-2">
          {checks.map((check) => (
            <li
              key={check.arm}
              className="rounded-2xl border border-border/70 p-5"
            >
              <p className="text-sm font-medium">{check.label}</p>
              <dl className="mt-4 space-y-1.5 font-mono text-xs tabular">
                <div className="flex justify-between gap-4">
                  <dt className="text-muted-foreground">published</dt>
                  <dd>
                    {check.published.tp} · {check.published.fp} ·{" "}
                    {check.published.fn}
                  </dd>
                </div>
                <div className="flex justify-between gap-4">
                  <dt className="text-muted-foreground">recomputed here</dt>
                  <dd>
                    {check.recomputed.tp} · {check.recomputed.fp} ·{" "}
                    {check.recomputed.fn}
                  </dd>
                </div>
              </dl>
              <p
                className={cn(
                  "mt-4 text-xs",
                  check.agrees ? "text-matched" : "text-spurious",
                )}
              >
                {check.agrees
                  ? "Exact match, matched · spurious · missed."
                  : "These disagree. The export is broken, not the harness."}
              </p>
              <p className="mt-2 font-mono text-[11px] break-all text-muted-foreground">
                {check.source}
              </p>
            </li>
          ))}
        </ul>
      </Section>

      <Separator />

      <Section id="files" title="The files">
        <div className="mt-6">
          <EdgeLegend />
        </div>
        <div className="mt-8">
          <FileIndex summaries={summaries} base={base} hybrid={hybridPanel} />
        </div>
      </Section>
    </>
  );
}
