import type { Metadata } from "next";
import { Geist, Geist_Mono } from "next/font/google";

import { SiteFooter } from "@/components/site/site-footer";
import { SiteHeader } from "@/components/site/site-header";
import { meta as projectMeta } from "@/lib/oracle-eval/data";
import { Providers } from "./providers";
import "./globals.css";

const geistSans = Geist({ variable: "--font-sans", subsets: ["latin"] });
const geistMono = Geist_Mono({ variable: "--font-mono", subsets: ["latin"] });

export const metadata: Metadata = {
  title: {
    default: "oracle-eval",
    template: "%s · oracle-eval",
  },
  description:
    "An eval harness measuring how far prompt-only optimisation can push off-the-shelf models on code-structure extraction, scored against a compiler-accurate oracle.",
};

export default function RootLayout({
  children,
}: Readonly<{ children: React.ReactNode }>) {
  return (
    <html
      lang="en"
      className={`${geistSans.variable} ${geistMono.variable} h-full`}
    >
      <body className="flex min-h-full flex-col font-sans antialiased">
        <Providers>
          <SiteHeader split={projectMeta.split} />
          <main className="flex-1">{children}</main>
          <SiteFooter meta={projectMeta} />
        </Providers>
      </body>
    </html>
  );
}
