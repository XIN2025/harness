import {
  DiagramArrow,
  DiagramFrame,
  DiagramLane,
  DiagramNode,
} from "@/components/oracle-eval/diagram";

const TRUTH_Y = 36;
const WORK_Y = 198;
const ROW_H = 66;
const TRUTH_W = 150;
const WORK_W = 118;
const WORK_GAP = 25;
const WORK_X0 = 12;

function workX(index: number): number {
  return WORK_X0 + index * (WORK_W + WORK_GAP);
}

const SCORER_INDEX = 3;
const SPINE_X = workX(SCORER_INDEX) + WORK_W / 2;

export function PipelineDiagram({
  repo,
  devFiles,
  testFiles,
  oracleEdges,
  models,
  prompts,
}: {
  repo: string;
  devFiles: number;
  testFiles: number;
  oracleEdges: number;
  models: number;
  prompts: number;
}) {
  const truth: readonly { title: string; lines: readonly string[] }[] = [
    { title: repo, lines: ["real tsconfig"] },
    { title: "ts-morph", lines: ["compiler API"] },
    {
      title: "oracle",
      lines: [`${oracleEdges} edges`, "22/22 checked"],
    },
  ];

  const work: readonly { title: string; lines: readonly string[] }[] = [
    { title: "corpus", lines: [`${devFiles} dev`, `${testFiles} test`] },
    { title: "runner", lines: [`${models} models`, `${prompts} prompts`] },
    { title: "cache", lines: ["immutable", "on disk"] },
    { title: "scorer", lines: ["P/R/F1 + CI"] },
    { title: "results", lines: ["JSON", "per-edge diff"] },
    { title: "export", lines: ["one JSON"] },
    { title: "dashboard", lines: ["reads results"] },
  ];

  const truthX = (index: number) =>
    SPINE_X + TRUTH_W / 2 - (truth.length - index) * (TRUTH_W + 30) + 30;

  return (
    <DiagramFrame
      viewBox="0 0 1000 292"
      minWidth={780}
      label={`The oracle-eval pipeline. ${repo} is read by a ts-morph extractor to produce the oracle, and separately a frozen corpus of ${devFiles} development files runs through the arms, a content-addressed cache, the scorer and the exporter to reach this dashboard. The oracle enters only at the scorer.`}
      caption={
        <>
          Two paths, one junction. The oracle is built by the TypeScript
          compiler from the repository&apos;s own{" "}
          <span className="font-mono">tsconfig</span>; the arms never see it.
          They meet once, at the scorer, and every number on this site is a
          comparison made at that junction.
        </>
      }
    >
      <DiagramLane x={12} y={22} text="ground truth · no model" />
      {truth.map((node, index) => (
        <DiagramNode
          key={node.title}
          x={truthX(index)}
          y={TRUTH_Y}
          width={TRUTH_W}
          height={ROW_H}
          title={node.title}
          lines={node.lines}
          tone={index === truth.length - 1 ? "truth" : "default"}
        />
      ))}
      {truth.slice(0, -1).map((node, index) => (
        <DiagramArrow
          key={node.title}
          from={[truthX(index) + TRUTH_W, TRUTH_Y + ROW_H / 2]}
          to={[truthX(index + 1), TRUTH_Y + ROW_H / 2]}
        />
      ))}

      <DiagramArrow
        from={[SPINE_X, TRUTH_Y + ROW_H]}
        to={[SPINE_X, WORK_Y]}
        label="ground truth"
        labelSide="right"
      />

      <DiagramLane x={12} y={184} text="measurement · frozen before use" />
      {work.map((node, index) => (
        <DiagramNode
          key={node.title}
          x={workX(index)}
          y={WORK_Y}
          width={WORK_W}
          height={ROW_H}
          title={node.title}
          lines={node.lines}
          tone={index === work.length - 1 ? "brand" : "default"}
        />
      ))}
      {work.slice(0, -1).map((node, index) => (
        <DiagramArrow
          key={node.title}
          from={[workX(index) + WORK_W, WORK_Y + ROW_H / 2]}
          to={[workX(index + 1), WORK_Y + ROW_H / 2]}
        />
      ))}
    </DiagramFrame>
  );
}
