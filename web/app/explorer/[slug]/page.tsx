import type { Metadata } from "next";
import Link from "next/link";
import { notFound } from "next/navigation";

import { EdgeGraph, EdgeLegend } from "@/components/oracle-eval/edge-graph";
import { EdgeMatrix } from "@/components/oracle-eval/edge-matrix";
import { Section } from "@/components/site/section";
import { Separator } from "@/components/ui/separator";
import { fileSlug, pathFromSlug } from "@/lib/oracle-eval/analysis";
import { fileByPath, filesWorstFirst, meta } from "@/lib/oracle-eval/data";
import { graphLayout } from "@/lib/oracle-eval/graph";

export function generateStaticParams() {
  return filesWorstFirst().map((file) => ({ slug: fileSlug(file.path) }));
}

export async function generateMetadata({
  params,
}: {
  params: Promise<{ slug: string }>;
}): Promise<Metadata> {
  const { slug } = await params;
  return { title: pathFromSlug(slug) };
}

export default async function FilePage({
  params,
}: {
  params: Promise<{ slug: string }>;
}) {
  const { slug } = await params;
  const path = pathFromSlug(slug);
  const file = fileByPath(path);
  if (!file) notFound();

  const ordered = filesWorstFirst();
  const index = ordered.findIndex((candidate) => candidate.path === path);
  const previous = index > 0 ? ordered[index - 1] : undefined;
  const next = index < ordered.length - 1 ? ordered[index + 1] : undefined;

  const layout = graphLayout(file);

  return (
    <>
      <header className="mx-auto w-full max-w-5xl px-6 pt-12 pb-8 md:pt-16">
        <Link
          href="/explorer"
          className="font-mono text-xs text-muted-foreground underline-offset-4 hover:text-foreground hover:underline"
        >
          ← all {meta.corpus.files} files
        </Link>
        <h1 className="mt-5 font-mono text-2xl font-semibold tracking-tight break-all md:text-3xl">
          {file.path}
        </h1>
        <dl className="mt-6 flex flex-wrap gap-x-8 gap-y-2 font-mono text-xs">
          <div className="flex gap-2">
            <dt className="text-muted-foreground">lines</dt>
            <dd className="tabular">{file.lines}</dd>
          </div>
          <div className="flex gap-2">
            <dt className="text-muted-foreground">oracle edges</dt>
            <dd className="tabular">{file.truth.length}</dd>
          </div>
          <div className="flex gap-2">
            <dt className="text-muted-foreground">cut</dt>
            <dd>{meta.explorer_cut}</dd>
          </div>
          <div className="flex gap-2">
            <dt className="text-muted-foreground">rank</dt>
            <dd className="tabular">
              {index + 1} of {ordered.length} by disagreement
            </dd>
          </div>
        </dl>
      </header>

      <Section
        title="Each arm's answer"
        lede="Callers on the left, callees on the right. Node positions are identical across the four panels, so the only thing that changes between them is which edges exist."
      >
        <div className="mt-6">
          <EdgeLegend />
        </div>

        <div className="mt-10 grid gap-10 lg:grid-cols-2">
          {meta.explorer_panels.map((arm) => {
            const panel = file.panels[arm];
            if (!panel) return null;
            return (
              <EdgeGraph
                key={arm}
                panel={panel}
                layout={layout}
                title={arm}
                subtitle={`${panel.matched.length} matched · ${panel.spurious.length} spurious · ${panel.missed.length} missed`}
              />
            );
          })}
        </div>
      </Section>

      <Separator />

      <Section
        title="The same file, as an audit"
        lede="Every edge any arm named or the oracle holds, and what each arm did with it."
      >
        <div className="mt-8">
          <EdgeMatrix file={file} />
        </div>
      </Section>

      <Separator />

      <nav className="mx-auto flex w-full max-w-5xl flex-wrap justify-between gap-4 px-6 py-10">
        {previous ? (
          <Link
            href={`/explorer/${fileSlug(previous.path)}`}
            className="max-w-[45%] text-sm underline-offset-4 hover:underline"
          >
            <span className="block text-xs text-muted-foreground">
              More disagreement
            </span>
            <span className="font-mono text-xs break-all">{previous.path}</span>
          </Link>
        ) : (
          <span />
        )}
        {next ? (
          <Link
            href={`/explorer/${fileSlug(next.path)}`}
            className="max-w-[45%] text-right text-sm underline-offset-4 hover:underline"
          >
            <span className="block text-xs text-muted-foreground">
              Less disagreement
            </span>
            <span className="font-mono text-xs break-all">{next.path}</span>
          </Link>
        ) : (
          <span />
        )}
      </nav>
    </>
  );
}
