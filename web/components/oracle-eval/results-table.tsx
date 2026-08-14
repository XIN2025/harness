import {
  Table,
  TableBody,
  TableCaption,
  TableCell,
  TableHead,
  TableHeader,
  TableRow,
} from "@/components/ui/table";
import { withInterval } from "@/lib/oracle-eval/format";
import type { MetricName, ResultRow } from "@/lib/oracle-eval/types";

const METRICS: readonly { key: MetricName; label: string }[] = [
  { key: "precision", label: "Precision" },
  { key: "recall", label: "Recall" },
  { key: "f1", label: "F1" },
];

function counts(row: ResultRow): string {
  return `${row.counts.tp} · ${row.counts.fp} · ${row.counts.fn}`;
}

export function ResultsTable({
  rows,
  caption,
}: {
  rows: readonly ResultRow[];
  caption: string;
}) {
  return (
    <div>
      <ul className="lg:hidden">
        {rows.map((row) => (
          <li
            key={row.source}
            className="border-b border-border py-4 first:pt-0"
          >
            <p className="text-[13px] font-medium">{row.label}</p>
            <p className="mt-0.5 font-mono text-[11px] break-all text-muted-foreground">
              {row.source}
            </p>
            <dl className="mt-3 grid grid-cols-[auto_1fr] gap-x-4 gap-y-1.5 font-mono text-[11px] tabular">
              {METRICS.map(({ key, label }) => (
                <div key={key} className="contents">
                  <dt className="text-muted-foreground">{label}</dt>
                  <dd className="text-right">
                    {withInterval(row.metrics[key])}
                  </dd>
                </div>
              ))}
              <div className="contents">
                <dt className="text-muted-foreground">tp · fp · fn</dt>
                <dd className="text-right">{counts(row)}</dd>
              </div>
            </dl>
          </li>
        ))}
      </ul>
      <p className="mt-4 text-xs text-muted-foreground lg:hidden">{caption}</p>

      <div className="hidden lg:block">
        <Table className="text-[13px]">
          <TableCaption className="text-left text-xs">{caption}</TableCaption>
          <TableHeader>
            <TableRow>
              <TableHead className="w-[38%]">Arm</TableHead>
              {METRICS.map(({ key, label }) => (
                <TableHead key={key} className="text-right">
                  {label}
                </TableHead>
              ))}
              <TableHead className="text-right whitespace-nowrap">
                tp · fp · fn
              </TableHead>
            </TableRow>
          </TableHeader>
          <TableBody>
            {rows.map((row) => (
              <TableRow key={row.source}>
                <TableCell className="py-3 align-top">
                  <span className="block font-medium">{row.label}</span>
                  <span className="mt-0.5 block font-mono text-[11px] break-all text-muted-foreground">
                    {row.source}
                  </span>
                </TableCell>
                {METRICS.map(({ key }) => (
                  <TableCell
                    key={key}
                    className="py-3 text-right align-top font-mono text-[11px] whitespace-nowrap tabular"
                  >
                    {withInterval(row.metrics[key])}
                  </TableCell>
                ))}
                <TableCell className="py-3 text-right align-top font-mono text-[11px] whitespace-nowrap tabular">
                  {counts(row)}
                </TableCell>
              </TableRow>
            ))}
          </TableBody>
        </Table>
      </div>
    </div>
  );
}
