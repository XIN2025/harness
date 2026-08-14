import { writeFileSync } from "node:fs";
import { relative, resolve } from "node:path";
import { extractCallableRefs } from "../../slm/src/label/callable-refs.ts";
import { createProject, extractStructure } from "../../slm/src/label/extract.ts";
import { functionScopes } from "../../slm/src/label/scope.ts";

const [, , tsConfigArg, srcDirArg, outArg] = process.argv;

if (!tsConfigArg || !srcDirArg || !outArg) {
	console.error("usage: tsx extract_corpus.ts <tsconfig.json> <srcDir> <out.jsonl>");
	process.exit(1);
}

const tsConfigPath = resolve(tsConfigArg);
const srcDir = resolve(srcDirArg);
const projectRoot = resolve(tsConfigPath, "..");

const project = createProject(tsConfigPath);

const sourceFiles = project
	.getSourceFiles()
	.filter((f) => resolve(f.getFilePath()).startsWith(srcDir));

console.error(`extracting ${sourceFiles.length} files from ${srcDir}`);

const lines: string[] = [];
let failures = 0;

for (const sourceFile of sourceFiles) {
	const relativePath = relative(projectRoot, sourceFile.getFilePath()).split("\\").join("/");
	try {
		lines.push(
			JSON.stringify({
				relative_path: relativePath,
				line_count: sourceFile.getEndLineNumber(),
				...extractStructure(sourceFile),
				callable_refs: extractCallableRefs(sourceFile),
				function_scopes: functionScopes(sourceFile),
			}),
		);
	} catch (error) {
		failures += 1;
		lines.push(
			JSON.stringify({
				relative_path: relativePath,
				error: error instanceof Error ? error.message : String(error),
			}),
		);
	}
}

writeFileSync(resolve(outArg), `${lines.join("\n")}\n`, "utf8");
console.error(`wrote ${lines.length} files (${failures} failed) -> ${outArg}`);
