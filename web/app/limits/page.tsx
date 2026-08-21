import type { Metadata } from "next";
import Link from "next/link";

import {
  Disclosure,
  DisclosureGroup,
  DisclosureList,
} from "@/components/site/disclosure";
import { PageHeader, Section } from "@/components/site/section";
import { Separator } from "@/components/ui/separator";
import { meta } from "@/lib/oracle-eval/data";
import {
  CLAIMED,
  FAILURES,
  LIMITS,
  NEXT,
  QUALIFIED,
} from "@/lib/oracle-eval/narrative";

export const metadata: Metadata = {
  title: "Limits",
  description:
    "What this study does not show, what went wrong while building it, and the exact boundary of what is claimed.",
};

export default function LimitsPage() {
  return (
    <>
      <PageHeader
        eyebrow="Limits"
        title="What this does not show"
        lede={`${LIMITS.length} of them, stated rather than left to be discovered. A weakness a reader finds for themselves is the objection that ends the conversation.`}
      />

      <Section id="not-shown">
        <DisclosureList notes={LIMITS} />
      </Section>

      <Separator />

      <Section
        id="not-claimed"
        title="Not claimed, in the harness's own words"
        lede="These lines are written by the exporter, not by this page. They travel with the data rather than with the presentation, so a redesign cannot drop them."
      >
        <ul className="mt-8 max-w-3xl space-y-4">
          {meta.not_claimed.map((claim) => (
            <li
              key={claim}
              className="border-l border-border pl-5 text-sm leading-relaxed text-muted-foreground"
            >
              {claim}
            </li>
          ))}
        </ul>
      </Section>

      <Separator />

      <Section
        id="boundary"
        title="The claim boundary"
        lede="Written out in both directions, so anything said about this work out loud has a line it does not cross."
      >
        <div className="mt-8 grid gap-6 md:grid-cols-2">
          <div className="rounded-2xl border border-border/70 p-6">
            <h3 className="text-sm font-medium">Claimed</h3>
            <ul className="mt-4 space-y-2.5 text-sm leading-relaxed text-muted-foreground">
              {CLAIMED.map((claim) => (
                <li key={claim}>{claim}</li>
              ))}
            </ul>
            <h3 className="mt-8 text-sm font-medium">
              Claimed with a qualifier
            </h3>
            <ul className="mt-4 space-y-2.5 text-sm leading-relaxed text-muted-foreground">
              {QUALIFIED.map((claim) => (
                <li key={claim}>{claim}</li>
              ))}
            </ul>
          </div>

          <div className="rounded-2xl border border-border/70 p-6">
            <h3 className="text-sm font-medium">Not claimed anywhere</h3>
            <ul className="mt-4 space-y-2.5 text-sm leading-relaxed text-muted-foreground">
              <li>That anything here was trained or fine-tuned.</li>
              <li>That this is a graph engine or a code property graph.</li>
              <li>That any slice is sound or complete.</li>
              <li>
                That these results transfer to other languages or other idioms.
              </li>
              <li>Any number without its confidence interval.</li>
              <li>
                Any comparison to another system&apos;s published figures.
              </li>
            </ul>

            <div className="mt-6 border-t border-border/60 pt-2">
              <Disclosure title="Why no comparison, ever">
                On this repository alone, &ldquo;call edge&rdquo; resolves to
                counts two orders of magnitude apart depending on the unit: call
                sites or unique pairs, resolved or textual, cross-file edges
                once or once per site. Two F1 figures on denominators that
                differ by that much are unrelated quantities that share a
                percent sign. The only honest route to a comparison is running
                the other extractor as an arm inside this harness, and that has
                not been done.
              </Disclosure>
            </div>
          </div>
        </div>
      </Section>

      <Separator />

      <Section
        id="failures"
        title="What went wrong"
        lede={`The pattern across all ${FAILURES.length}: most were caught by reading real output next to real source, not by a test going red.`}
      >
        <DisclosureGroup className="mt-8">
          {FAILURES.map((failure) => (
            <Disclosure
              key={failure.id}
              label={failure.id}
              title={failure.title}
            >
              <p>{failure.body}</p>
              <p className="mt-2">
                <span className="text-foreground">What it teaches.</span>{" "}
                {failure.lesson}
              </p>
            </Disclosure>
          ))}
        </DisclosureGroup>
      </Section>

      <Separator />

      <Section
        id="next"
        title="What I would do next, in order"
        lede="The first is reading rather than engineering, and everything else is downstream of it. None of it needs a new model run."
      >
        <ol className="mt-8 max-w-3xl space-y-7">
          {NEXT.map((step, index) => (
            <li key={step.title} className="flex gap-5">
              <span className="mt-0.5 font-mono text-xs text-muted-foreground tabular">
                {String(index + 1).padStart(2, "0")}
              </span>
              <div>
                <h3 className="text-sm font-medium">{step.title}</h3>
                <p className="mt-2 text-sm leading-relaxed text-muted-foreground">
                  {step.body}
                </p>
              </div>
            </li>
          ))}
        </ol>

        <p className="mt-10 max-w-2xl text-sm leading-relaxed text-muted-foreground">
          The measurements those steps would refine are on the{" "}
          <Link
            href="/results"
            className="text-foreground underline underline-offset-4"
          >
            results page
          </Link>
          , and the instrument that produced them is described in the{" "}
          <Link
            href="/method"
            className="text-foreground underline underline-offset-4"
          >
            method
          </Link>
          .
        </p>
      </Section>
    </>
  );
}
