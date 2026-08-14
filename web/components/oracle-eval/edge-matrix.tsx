import { edgeKey } from "@/lib/oracle-eval/analysis";
import { allEdges, edgeClass, statusByEdge } from "@/lib/oracle-eval/graph";
import type { FileEntry } from "@/lib/oracle-eval/types";

export function EdgeMatrix({ file }: { file: FileEntry }) {
  const truth = new Set(file.truth.map(edgeKey));
  const arms = Object.keys(file.panels);
  const statuses = new Map(
    arms.map((arm) => [arm, statusByEdge(file.panels[arm])] as const),
  );

  const rows = [...allEdges(file)]
    .map((edge) => ({
      edge,
      key: edgeKey(edge),
      inOracle: truth.has(edgeKey(edge)),
    }))
    .sort(
      (a, b) =>
        Number(b.inOracle) - Number(a.inOracle) || a.key.localeCompare(b.key),
    );

  return (
    <div className="overflow-x-auto">
      <table className="w-full min-w-[620px] border-collapse text-[13px]">
        <caption className="caption-bottom pt-4 text-left text-xs leading-relaxed text-muted-foreground">
          Oracle edges first, then edges no oracle entry exists for. A blank
          cell means the arm never named that edge and the oracle does not have
          it, which is not the same as a miss.
        </caption>
        <thead>
          <tr className="border-b border-border text-left">
            <th className="py-2 pr-4 font-medium">Edge</th>
            <th className="py-2 pr-4 text-center font-medium">Oracle</th>
            {arms.map((arm) => (
              <th
                key={arm}
                className="py-2 pr-4 text-center font-mono text-[11px] font-medium last:pr-0"
              >
                {arm}
              </th>
            ))}
          </tr>
        </thead>
        <tbody>
          {rows.map(({ edge, key, inOracle }) => (
            <tr key={key} className="border-b border-border/60">
              <td className="py-2 pr-4 font-mono text-[11px]">
                <span className="text-foreground">{edge[0]}</span>
                <span className="mx-1.5 text-muted-foreground">→</span>
                <span className="text-foreground">{edge[1]}</span>
              </td>
              <td className="py-2 pr-4 text-center">
                {inOracle ? (
                  <span className="text-truth" title="The oracle has this edge">
                    ●<span className="sr-only"> in the oracle</span>
                  </span>
                ) : (
                  <span
                    className="text-muted-foreground/50"
                    aria-label="not in the oracle"
                  >
                    ·
                  </span>
                )}
              </td>
              {arms.map((arm) => {
                const status = statuses.get(arm)?.get(key);
                if (!status) {
                  return (
                    <td
                      key={arm}
                      className="py-2 pr-4 text-center text-muted-foreground/40 last:pr-0"
                    >
                      <span aria-label={`${arm}: not named`}>·</span>
                    </td>
                  );
                }
                const { colour, mark, label } = edgeClass(status);
                return (
                  <td key={arm} className="py-2 pr-4 text-center last:pr-0">
                    <span style={{ color: colour }} title={`${arm}: ${label}`}>
                      {mark}
                      <span className="sr-only"> {label}</span>
                    </span>
                  </td>
                );
              })}
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
}
