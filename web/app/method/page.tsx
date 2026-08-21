import type { Metadata } from "next";

import { PipelineDiagram } from "@/components/oracle-eval/pipeline-diagram";
import {
  Disclosure,
  DisclosureGroup,
  DisclosureList,
} from "@/components/site/disclosure";
import { PageHeader, Section } from "@/components/site/section";
import { Separator } from "@/components/ui/separator";
import { cutBreakdown } from "@/lib/oracle-eval/analysis";
import { SOURCE, bySource, curve, hybrid, meta } from "@/lib/oracle-eval/data";
import {
  CONSTRAINTS,
  DECISIONS,
  PROPERTIES,
} from "@/lib/oracle-eval/narrative";

export const metadata: Metadata = {
  title: "Method",
  description:
    "How the oracle is built, what was frozen before use, and the decisions the results turned on.",
};

function humanise(key: string): string {
  return key.replace(/_/g, " ");
}

const COMMANDS = [
  {
    command: "score selfcheck",
    detail: "Scores the oracle against itself. Must print exactly 1.000.",
  },
  {
    command: "score run treesitter --cut calls_only",
    detail: "Reproduces the parser floor, with no model and no network.",
  },
  {
    command: "oracle blindspots",
    detail: "Reports what the oracle itself cannot see, per file.",
  },
  {
    command: "export demo",
    detail:
      "Rebuilds the JSON this site renders. Fails if any row's file count disagrees with the corpus.",
  },
];

export default function MethodPage() {
  const parserPrimary = bySource(curve, SOURCE.parserPrimary);
  const parserFull = bySource(hybrid, SOURCE.parserFull);
  const agreement = bySource(hybrid, SOURCE.agreementRound1);
  const breakdown = cutBreakdown(parserPrimary, parserFull, agreement);
  const { manifest } = meta.corpus;

  return (
    <>
      <PageHeader
        eyebrow="Method"
        title="The instrument"
        lede="For a language with a type checker, a free and exact oracle for this task already exists. That is why the task was chosen: the ground truth is not negotiable, and anyone with the repository can re-derive it."
      />

      <Section id="pipeline" title="How it fits together">
        <div className="mt-8">
          <PipelineDiagram
            repo={meta.corpus.repo}
            devFiles={manifest.counts.dev}
            testFiles={manifest.counts.test}
            oracleEdges={meta.corpus.oracle_edges}
            models={meta.models.length}
            prompts={meta.prompts}
          />
        </div>
      </Section>

      <Separator />

      <Section
        id="properties"
        title="Five properties that make the numbers mean something"
        lede="Each exists for a stated reason, and each cost something to keep. Open one for the reason."
      >
        <DisclosureList notes={PROPERTIES} className="mt-8" />
      </Section>

      <Separator />

      <Section
        id="corpus"
        title="The corpus, frozen before anything ran"
        lede="The selection rule was preregistered and applied before any arm had run. The split is keyed on the hash of each file's path, so it correlates with neither filename nor size."
      >
        <div className="mt-8 grid gap-6 md:grid-cols-2">
          <div className="rounded-2xl border border-border/70 p-6">
            <h3 className="text-sm font-medium">Split</h3>
            <dl className="mt-4 space-y-2 font-mono text-xs tabular">
              {Object.entries(manifest.counts).map(([name, count]) => (
                <div key={name} className="flex justify-between gap-4">
                  <dt className="text-muted-foreground">{name}</dt>
                  <dd>{count}</dd>
                </div>
              ))}
            </dl>
            <p className="mt-4 text-xs leading-relaxed text-muted-foreground">
              Only the development split has ever been scored. The test split is
              spendable exactly once, and spending it is not what this site
              reports.
            </p>
          </div>

          <div className="rounded-2xl border border-border/70 p-6">
            <h3 className="text-sm font-medium">Selection rule</h3>
            <dl className="mt-4 space-y-2 font-mono text-xs">
              {Object.entries(manifest.rule).map(([name, value]) => (
                <div key={name} className="flex justify-between gap-4">
                  <dt className="text-muted-foreground">{humanise(name)}</dt>
                  <dd className="text-right break-all">{value}</dd>
                </div>
              ))}
            </dl>
          </div>
        </div>

        <p className="mt-4 font-mono text-[11px] break-all text-muted-foreground">
          {manifest.path} · digest {manifest.digest}
        </p>
      </Section>

      <Separator />

      <Section
        id="cuts"
        title="Two cuts, and which one carries information"
        lede="A cut is which classes of edge a score is taken over. Both were defined before any model ran, and neither was redefined afterwards."
      >
        <dl className="mt-8 grid gap-6 md:grid-cols-2">
          <div className="rounded-2xl border border-border/70 p-6">
            <dt className="font-mono text-sm font-medium">calls_only</dt>
            <dd className="mt-3 text-sm leading-relaxed text-muted-foreground">
              Invocations: {breakdown.invocations} edges. The callee is what the
              syntax tree literally says, so this cut cannot discriminate
              between models at all. That is a critique of its design, not a
              triumph of tree-sitter.
            </dd>
          </div>
          <div className="rounded-2xl border border-border/70 p-6">
            <dt className="font-mono text-sm font-medium">full</dt>
            <dd className="mt-3 text-sm leading-relaxed text-muted-foreground">
              The above plus {breakdown.refs} callable references: functions
              passed as values, never invoked where they appear, invisible to
              syntax. Every claim about models is made on this cut.
            </dd>
          </div>
        </dl>
      </Section>

      <Separator />

      <Section
        id="constraints"
        title="The constraints every number was produced under"
        lede="They bound every figure on this site, and several design decisions only make sense in light of them."
      >
        <DisclosureList notes={CONSTRAINTS} className="mt-8" />
      </Section>

      <Separator />

      <Section
        id="decisions"
        title="The decisions the results turned on"
        lede="Each is recorded with what it was for at the time it was made, not with what it turned out to be good for."
      >
        <DisclosureGroup className="mt-8">
          {DECISIONS.map((decision) => (
            <Disclosure
              key={decision.id}
              label={decision.id}
              title={decision.title}
            >
              <p>
                <span className="text-foreground">Intent.</span>{" "}
                {decision.intent}
              </p>
              <p className="mt-2">{decision.body}</p>
            </Disclosure>
          ))}
        </DisclosureGroup>
      </Section>

      <Separator />

      <Section
        id="reproduce"
        title="Run it yourself"
        lede="Four commands, none of which touches a network or a model. The first is the one that matters: if the scorer cannot reproduce the oracle from the oracle, nothing downstream of it means anything."
      >
        <dl className="mt-8 max-w-3xl space-y-4">
          {COMMANDS.map((entry) => (
            <div
              key={entry.command}
              className="rounded-2xl border border-border/70 p-5"
            >
              <dt className="overflow-x-auto font-mono text-xs whitespace-pre">
                <span className="text-muted-foreground">oracle_eval.cli </span>
                {entry.command}
              </dt>
              <dd className="mt-2 text-xs leading-relaxed text-muted-foreground">
                {entry.detail}
              </dd>
            </div>
          ))}
        </dl>
      </Section>
    </>
  );
}
