import Link from "next/link";

import { CutDiagram } from "@/components/oracle-eval/cut-diagram";
import { MetricPlot } from "@/components/oracle-eval/metric-plot";
import { RegisteredOutcomes } from "@/components/oracle-eval/registered-outcomes";
import { type Stat, StatRow } from "@/components/oracle-eval/stat-row";
import { PageHeader, Section } from "@/components/site/section";
import { Separator } from "@/components/ui/separator";
import { cutBreakdown } from "@/lib/oracle-eval/analysis";
import { SOURCE, bySource, curve, hybrid, meta } from "@/lib/oracle-eval/data";
import { pct } from "@/lib/oracle-eval/format";

export default function Home() {
  const theirPrompt = bySource(curve, SOURCE.theirPrompt);
  const qwenPrompted = bySource(curve, SOURCE.qwenPrompted);
  const parserPrimary = bySource(curve, SOURCE.parserPrimary);
  const parser = bySource(hybrid, SOURCE.parserFull);
  const agreement = bySource(hybrid, SOURCE.agreementRound1);
  const breakdown = cutBreakdown(parserPrimary, parser, agreement);

  const stats: readonly Stat[] = [
    {
      from: pct(parser.metrics.f1.point),
      value: pct(agreement.metrics.f1.point),
      label: "The one measured gain",
      detail:
        "F1 on the wide cut, parser alone against the parser plus two models that must agree. The intervals do not overlap, which is the only reason this is stated as a gain at all.",
    },
    {
      from: pct(theirPrompt.metrics.f1.point),
      value: pct(qwenPrompted.metrics.f1.point),
      label: "Prompt work alone",
      detail: `The same 1.5B model on the same files, nothing changed but the prompt. On that cut a free parser scores ${pct(parserPrimary.metrics.f1.point)}, so the climb is not the story.`,
    },
    {
      value: "0",
      label: "Weights changed",
      detail:
        "No fine-tuning anywhere in the project. Every gain here comes from a prompt or from a combination rule.",
    },
  ];

  return (
    <>
      <PageHeader
        eyebrow={`Eval harness · ${meta.corpus.repo} · ${meta.corpus.files} files · ${meta.corpus.oracle_edges} oracle edges`}
        title="Where a language model is the wrong tool, and where it is the only tool"
        lede={
          <>
            Small models are asked to extract the call graph of a TypeScript
            file and scored against the compiler&apos;s own answer. A free
            parser wins most of that task outright. The interesting part is the
            slice it cannot see at all.
          </>
        }
      >
        <StatRow stats={stats} className="mt-10" />

        <div className="mt-6 flex flex-wrap items-center gap-x-6 gap-y-2">
          {meta.models.map((model) => (
            <div key={model.arm} className="flex items-baseline gap-2">
              <span className="font-mono text-xs">{model.model}</span>
              <span className="text-xs text-muted-foreground">
                {model.params} · {model.lab}
              </span>
            </div>
          ))}
        </div>
      </PageHeader>

      <Separator />

      <Section
        id="result"
        title="The result"
        lede={
          <>
            On the wide cut, the one that includes functions passed as values, a
            tree-sitter parser reaches {breakdown.parserReached} of{" "}
            {breakdown.fullEdges} edges with perfect precision and cannot see
            the rest. Adding one model recovers most of them and floods the
            graph with false ones. Requiring{" "}
            <em>two models from different labs</em> to name the same edge is the
            only construct here that clears the overlap rule against the parser.
          </>
        }
      >
        <div className="mt-8">
          <MetricPlot rows={hybrid} baseline={parser} />
        </div>
      </Section>

      <Section
        id="mechanism"
        title="Why it works"
        lede="Not a mystery, and not a property of these two models. The oracle's edges divide into a class syntax resolves exactly and a class syntax cannot resolve at all."
      >
        <div className="mt-8">
          <CutDiagram breakdown={breakdown} />
        </div>
      </Section>

      <Separator />

      <Section
        id="registered"
        title="This outcome was written down before any model ran"
        lede={
          <>
            Three results were registered in advance, each with the consequence
            that would follow from it. The third is what arrived, so the project
            did not need rescuing, a reframe after the fact, or a change of
            metric. Following the branch that fired is what produced the
            measurement above.
          </>
        }
      >
        <div className="mt-8">
          <RegisteredOutcomes />
        </div>
      </Section>

      <Separator />

      <Section
        title="Read on"
        lede="Every number on this site names the file in the harness it was copied from, and every per-file panel is recomputed by the harness's own scorer rather than by this app."
      >
        <ul className="mt-8 grid gap-px overflow-hidden rounded-3xl border border-border/70 bg-border/70 sm:grid-cols-3">
          {[
            {
              href: "/method",
              title: "Method",
              detail:
                "The instrument: how ground truth is built, what was frozen before use, and the five properties that make the numbers mean anything.",
            },
            {
              href: "/results",
              title: "Results",
              detail:
                "Every arm, every round, the replication across five repositories, the registered null, and the headroom limit on all of it.",
            },
            {
              href: "/explorer",
              title: "Explorer",
              detail: `All ${meta.corpus.files} scored files, edge by edge. Each arm's answer beside the oracle's, with the disagreements first.`,
            },
          ].map((card) => (
            <li key={card.href} className="bg-background">
              <Link
                href={card.href}
                className="flex h-full flex-col p-6 transition-colors hover:bg-accent"
              >
                <span className="text-base font-medium tracking-tight">
                  {card.title}
                </span>
                <span className="mt-3 text-[13px] leading-relaxed text-muted-foreground">
                  {card.detail}
                </span>
              </Link>
            </li>
          ))}
        </ul>

        <p className="mt-8 max-w-2xl text-sm leading-relaxed text-muted-foreground">
          The scope, stated once here and in full on the{" "}
          <Link
            href="/limits"
            className="text-foreground underline underline-offset-4"
          >
            limits page
          </Link>
          : one language, one repository for the model arms, off-the-shelf small
          models under a no-budget constraint, dev split only. Nothing here is
          compared to any other system&apos;s published figures, for a reason
          that is also on that page.
        </p>
      </Section>
    </>
  );
}
