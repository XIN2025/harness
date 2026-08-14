import type { Meta } from "@/lib/oracle-eval/types";

export function SiteFooter({ meta }: { meta: Meta }) {
  const { counts, digest } = meta.corpus.manifest;

  return (
    <footer className="border-t border-border/70">
      <div className="mx-auto flex w-full max-w-5xl flex-wrap items-baseline justify-between gap-x-6 gap-y-3 px-6 py-8">
        <p className="font-mono text-xs text-muted-foreground">
          {meta.project} · {meta.corpus.repo} · {meta.split} split ·{" "}
          {counts.dev} of {counts.total} files
        </p>
        <p className="text-xs text-muted-foreground">
          The {counts.test}-file test split and the held-out repository have
          never been scored.
        </p>
        <p className="w-full font-mono text-[11px] break-all text-muted-foreground/70">
          corpus digest {digest}
        </p>
      </div>
    </footer>
  );
}
