# oracle-eval, the site

Presents the measured results from the harness in the repository root. Reads
`data/oracle-eval.json`, which `harness export demo` writes; nothing here
recomputes a summary metric, and no figure is typed in by hand.

```bash
pnpm install
pnpm dev          # http://localhost:3000
pnpm verify       # typecheck, lint, format check, build
```

Regenerate the data after a new scoring run:

```bash
cd .. && ./.venv/Scripts/python.exe -m oracle_eval.cli export demo
```
