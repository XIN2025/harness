from __future__ import annotations

import typer

from oracle_eval.commands.arms import arm_app
from oracle_eval.commands.corpus import corpus_app
from oracle_eval.commands.ensemble import ensemble_app
from oracle_eval.commands.export import export_app
from oracle_eval.commands.hybrid import hybrid_app
from oracle_eval.commands.oracle import oracle_app
from oracle_eval.commands.score import score_app
from oracle_eval.console import harden_stdout

app = typer.Typer(
    add_completion=False,
    help="Eval harness: prompt-only optimisation on code-structure extraction.",
)

for sub_app, name in (
    (oracle_app, "oracle"),
    (corpus_app, "corpus"),
    (score_app, "score"),
    (arm_app, "arm"),
    (ensemble_app, "ensemble"),
    (hybrid_app, "hybrid"),
    (export_app, "export"),
):
    app.add_typer(sub_app, name=name)


def main() -> None:
    harden_stdout()
    app()


if __name__ == "__main__":
    main()
