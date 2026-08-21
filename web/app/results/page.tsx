import type { Metadata } from "next";
import Link from "next/link";

import { HeadroomBars } from "@/components/oracle-eval/headroom-bars";
import { MetricPlot } from "@/components/oracle-eval/metric-plot";
import { OverlapCheck } from "@/components/oracle-eval/overlap-check";
import { PrecisionRecallPlane } from "@/components/oracle-eval/pr-plane";
import { ResultsTable } from "@/components/oracle-eval/results-table";
import { Disclosure, DisclosureGroup } from "@/components/site/disclosure";
import { PageHeader, Section } from "@/components/site/section";
import { Separator } from "@/components/ui/separator";
import {
  SOURCE,
  baselines,
  bySource,
  curve,
  headroom,
  hybrid,
  overlap,
} from "@/lib/oracle-eval/data";
import { pct } from "@/lib/oracle-eval/format";

export const metadata: Metadata = {
  title: "Results",
  description:
    "Every arm, every round, the replication across five repositories, the registered null, and the headroom that bounds all of it.",
};

export default function ResultsPage() {
  const parserPrimary = bySource(curve, SOURCE.parserPrimary);
  const parserFull = bySource(hybrid, SOURCE.parserFull);
  const agreementRound1 = bySource(hybrid, SOURCE.agreementRound1);
  const agreementRound2 = bySource(hybrid, SOURCE.agreementRound2);
  const round2Overlap = overlap.find((row) => row.ensemble_dropped);

  return (
    <>
      <PageHeader
        eyebrow="Results · dev split"
        title="Every number, and what bounds it"
        lede={
          <>
            Each row names the file in the harness it was copied from. Summary
            figures are copied out of published results rather than recomputed
            here, so nothing on this page can show a number that was never
            written to disk.
          </>
        }
      />

      <Section
        id="headroom"
        title="Read this first: how much room there was"
        lede="A model can only add edges the parser is blind to, so that blindness is the ceiling on what any of this is worth. It is measurable for free before any model runs, and it varies by an order of magnitude between repositories."
      >
        <div className="mt-8">
          <HeadroomBars headroom={headroom} />
        </div>
        <p className="mt-8 max-w-2xl text-sm leading-relaxed text-muted-foreground">
          The scored repository was selected before any of this was known, and
          it turned out to be the corpus where the phenomenon exists. So the
          headline may be a fact about functional TypeScript rather than about
          TypeScript.
        </p>
      </Section>

      <Separator />

      <Section
        id="hybrid"
        title="Where the models contribute"
        lede={
          <>
            The wide cut, {parserFull.counts.tp + parserFull.counts.fn} edges. A
            row is coloured only if it clears the overlap rule against the
            parser, so colour here is derived from the statistics rather than
            chosen.
          </>
        }
      >
        <div className="mt-8">
          <MetricPlot rows={hybrid} baseline={parserFull} />
        </div>

        <div className="mt-14">
          <PrecisionRecallPlane
            cut="full"
            points={[
              { row: parserFull },
              { row: bySource(hybrid, SOURCE.qwenUnion) },
              { row: bySource(hybrid, SOURCE.llamaUnion) },
              { row: agreementRound1, emphasis: true },
              { row: agreementRound2 },
            ]}
            caption={
              <>
                What a single F1 figure cannot show: both union arms buy recall
                by giving up precision, while requiring agreement moves up and
                right of all of them instead of trading along the same contour.
                Whiskers are the bootstrap intervals.
              </>
            }
          />
        </div>
      </Section>

      <Separator />

      <Section
        id="null"
        title="Round 2: a registered null, and a kill-switch that fired"
        lede={
          <>
            Round 2 targeted the two measured Round 1 failure classes, and was
            registered with its falsification condition before any Round 2
            response existed. It worked on the individual arms and the
            combination did not move: {pct(agreementRound1.metrics.f1.point)} to{" "}
            {pct(agreementRound2.metrics.f1.point)}, intervals almost entirely
            overlapping.
          </>
        }
      >
        <div className="mt-10">
          <OverlapCheck rows={overlap} />
        </div>

        <p className="mt-8 max-w-2xl text-sm leading-relaxed text-muted-foreground">
          Applying the same constraint to both prompts made the two models fail
          in the same places, destroying the disagreement the combination
          depended on.{" "}
          {round2Overlap ? (
            <>
              At {pct(round2Overlap.max)} against a{" "}
              {pct(round2Overlap.limit, 0)} limit, that ensemble was dropped
              rather than reported.
            </>
          ) : null}{" "}
          There was no Round 3: a null is reported as a null.
        </p>
      </Section>

      <Separator />

      <Section
        id="prompt-curve"
        title="The prompt curve"
        lede={
          <>
            The primary cut, {parserPrimary.counts.tp + parserPrimary.counts.fn}{" "}
            edges, same {parserPrimary.counts.files} files. The first row is a
            free tree-sitter parser, and it is the point: prompt work moved a
            1.5B model tenfold and left it far below a program with no model in
            it.{" "}
            <span className="text-foreground">
              On this cut the result is the gap, not the climb.
            </span>
          </>
        }
      >
        <div className="mt-8">
          <MetricPlot rows={curve} baseline={parserPrimary} />
        </div>
      </Section>

      <Separator />

      <Section
        id="replication"
        title="Is that floor a quirk of one library?"
        lede={
          <>
            No. Four more repositories, each with its own frozen corpus and its
            own independently built oracle, scored with the same parser. On all
            four it reproduces the oracle exactly: zero spurious, zero missed.
            The primary cut is a syntactic question, and syntax answers it.
          </>
        }
      >
        <div className="mt-8">
          <MetricPlot rows={baselines} />
        </div>
      </Section>

      <Separator />

      <Section
        id="tables"
        title="Every plotted number, as text"
        lede={
          <>
            The plots are the argument; this is the audit. Nothing on this site
            is reachable only through colour or position, and every row names
            its artefact. Per-file classifications for any of these are in the{" "}
            <Link
              href="/explorer"
              className="text-foreground underline underline-offset-4"
            >
              explorer
            </Link>
            .
          </>
        }
      >
        <DisclosureGroup className="mt-8">
          {[
            {
              rows: hybrid,
              title: "Hybrid",
              caption: "Hybrid · dev split · full cut",
            },
            {
              rows: curve,
              title: "Prompt curve",
              caption: "Prompt curve · dev split · calls_only cut",
            },
            {
              rows: baselines,
              title: "Parser replication",
              caption:
                "Parser replication · five repositories · calls_only cut",
            },
          ].map((table) => (
            <Disclosure
              key={table.title}
              title={table.title}
              aside={`${table.rows.length} rows`}
            >
              <div className="max-w-none">
                <ResultsTable rows={table.rows} caption={table.caption} />
              </div>
            </Disclosure>
          ))}
        </DisclosureGroup>
      </Section>
    </>
  );
}
