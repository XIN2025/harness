"use client";

import Link from "next/link";
import { usePathname } from "next/navigation";

import { cn } from "@/lib/utils";

const NAV = [
  { href: "/", label: "Finding" },
  { href: "/method", label: "Method" },
  { href: "/results", label: "Results" },
  { href: "/explorer", label: "Explorer" },
  { href: "/limits", label: "Limits" },
] as const;

export function SiteHeader({ split }: { split: string }) {
  const pathname = usePathname();

  return (
    <header className="sticky top-0 z-50 border-b border-border/70 bg-background/72 backdrop-blur-xl backdrop-saturate-150">
      <div className="mx-auto flex h-12 w-full max-w-5xl items-center justify-between gap-4 px-6">
        <Link
          href="/"
          className="shrink-0 font-mono text-sm font-medium tracking-tight"
        >
          oracle-eval
        </Link>

        <nav className="flex min-w-0 items-center gap-4 sm:gap-6">
          <ul className="no-scrollbar flex min-w-0 items-center gap-4 overflow-x-auto sm:gap-6">
            {NAV.map((item) => {
              const active =
                item.href === "/"
                  ? pathname === "/"
                  : pathname.startsWith(item.href);
              return (
                <li key={item.href}>
                  <Link
                    href={item.href}
                    aria-current={active ? "page" : undefined}
                    className={cn(
                      "text-xs whitespace-nowrap transition-colors hover:text-foreground",
                      active ? "text-foreground" : "text-muted-foreground",
                    )}
                  >
                    {item.label}
                  </Link>
                </li>
              );
            })}
          </ul>
          <span className="hidden shrink-0 rounded-full bg-secondary px-2.5 py-1 font-mono text-[11px] text-muted-foreground md:inline">
            {split} split
          </span>
        </nav>
      </div>
    </header>
  );
}
