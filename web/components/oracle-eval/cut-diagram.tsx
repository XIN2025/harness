import {
  DiagramArrow,
  DiagramFrame,
  DiagramNode,
} from "@/components/oracle-eval/diagram";
import type { CutBreakdown } from "@/lib/oracle-eval/analysis";

export function CutDiagram({ breakdown }: { breakdown: CutBreakdown }) {
  const {
    invocations,
    refs,
    fullEdges,
    parserReached,
    parserMissedInvocations,
    agreementAdded,
    agreementFalse,
  } = breakdown;

  return (
    <DiagramFrame
      viewBox="0 0 1000 330"
      minWidth={820}
      label={`The oracle's ${fullEdges} full-cut edges split into ${invocations} invocations, which a tree-sitter parser reaches ${parserReached} of, and ${refs} callable references, which syntax cannot see at all and which two models in agreement recover ${agreementAdded} of.`}
      caption={
        <>
          The parser is not merely worse on the second class. It is structurally
          incapable of it, and it is near-perfect on the first. That asymmetry
          is the finding: spend the deterministic tool where it is exact, and
          spend the models only on what is left.
        </>
      }
    >
      <rect
        x={200}
        y={20}
        width={600}
        height={118}
        rx={14}
        fill="none"
        stroke="var(--border)"
        strokeDasharray="5 4"
      />
      <text
        x={216}
        y={42}
        fill="var(--muted-foreground)"
        fontSize={10.5}
        fontFamily="var(--font-mono)"
      >
        oracle · full cut · {fullEdges} edges
      </text>

      <DiagramNode
        x={220}
        y={54}
        width={270}
        height={66}
        title={`invocations · ${invocations}`}
        lines={["what the AST literally says"]}
        tone="truth"
      />
      <DiagramNode
        x={510}
        y={54}
        width={270}
        height={66}
        title={`callable references · ${refs}`}
        lines={["passed as values, never called"]}
        tone="truth"
      />

      <DiagramArrow
        from={[330, 120]}
        to={[250, 232]}
        label={`${parserReached} of ${invocations}`}
      />
      <DiagramArrow
        from={[610, 120]}
        to={[330, 232]}
        dashed
        label="0 · structurally blind"
        labelSide="below"
      />
      <DiagramArrow
        from={[700, 120]}
        to={[770, 232]}
        label="the residue"
        labelSide="right"
      />

      <DiagramNode
        x={150}
        y={232}
        width={230}
        height={70}
        title="tree-sitter, no model"
        lines={[
          "precision 100%",
          `${parserMissedInvocations} missed of ${invocations}`,
        ]}
      />
      <DiagramNode
        x={640}
        y={232}
        width={260}
        height={70}
        title="two models, must agree"
        lines={[`+${agreementAdded} true`, `+${agreementFalse} false`]}
        tone="brand"
      />
    </DiagramFrame>
  );
}
