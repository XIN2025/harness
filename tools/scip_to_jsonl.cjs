const fs = require("node:fs");
const { execSync } = require("node:child_process");

function resolveScipModule() {
  const root = execSync("npm root -g", { encoding: "utf8" }).trim();
  const candidate = `${root}/@sourcegraph/scip-typescript/dist/src/scip.js`;
  if (!fs.existsSync(candidate)) {
    throw new Error(
      `scip decoder not found at ${candidate}\n` +
        "Run: npm install -g @sourcegraph/scip-typescript",
    );
  }
  return candidate;
}

function normaliseRange(r) {
  if (!r || r.length === 0) return null;
  if (r.length === 3) return [r[0], r[1], r[0], r[2]];
  if (r.length === 4) return [r[0], r[1], r[2], r[3]];
  throw new Error(`unexpected range arity ${r.length}: ${JSON.stringify(r)}`);
}

function main() {
  const [, , inPath, outPath] = process.argv;
  if (!inPath || !outPath) {
    console.error("usage: node scip_to_jsonl.cjs <index.scip> <out.jsonl>");
    process.exit(2);
  }

  const { scip } = require(resolveScipModule());
  const index = scip.Index.deserializeBinary(fs.readFileSync(inPath));

  const out = fs.createWriteStream(outPath, { encoding: "utf8" });
  const meta = index.metadata;
  out.write(
    JSON.stringify({
      _meta: {
        tool: meta?.tool_info?.name ?? null,
        tool_version: meta?.tool_info?.version ?? null,
        project_root: meta?.project_root ?? null,
        document_count: index.documents.length,
        external_symbol_count: index.external_symbols.length,
      },
    }) + "\n",
  );

  let occTotal = 0;
  for (const doc of index.documents) {
    const occurrences = doc.occurrences.map((o) => {
      occTotal += 1;
      const rec = {
        range: normaliseRange(o.range),
        symbol: o.symbol,
        roles: o.symbol_roles,
      };
      const enc = normaliseRange(o.enclosing_range);
      if (enc) rec.enclosing_range = enc;
      if (o.syntax_kind) rec.syntax_kind = o.syntax_kind;
      return rec;
    });

    const symbols = doc.symbols.map((s) => {
      const rec = { symbol: s.symbol, kind: s.kind };
      if (s.display_name) rec.display_name = s.display_name;
      if (s.enclosing_symbol) rec.enclosing_symbol = s.enclosing_symbol;
      if (s.documentation?.length) rec.documentation = s.documentation;
      if (s.relationships?.length) {
        rec.relationships = s.relationships.map((r) => ({
          symbol: r.symbol,
          is_reference: r.is_reference,
          is_implementation: r.is_implementation,
          is_type_definition: r.is_type_definition,
          is_definition: r.is_definition,
        }));
      }
      return rec;
    });

    out.write(
      JSON.stringify({
        relative_path: doc.relative_path.split("\\").join("/"),
        language: doc.language,
        occurrences,
        symbols,
      }) + "\n",
    );
  }

  out.end();
  out.on("finish", () => {
    console.error(
      `wrote ${index.documents.length} documents, ${occTotal} occurrences -> ${outPath}`,
    );
  });
}

main();
