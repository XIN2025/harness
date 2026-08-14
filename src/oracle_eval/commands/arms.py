from __future__ import annotations

from typing import Annotated

import typer

from oracle_eval.arms.provider import MAX_TOKENS
from oracle_eval.commands.options import (
    AllowDriftOption,
    LimitOption,
    ManifestOption,
    PredictionsOption,
    RepoOption,
    SpendTestSplitOption,
    SplitOption,
)
from oracle_eval.console import console
from oracle_eval.loading import corpus_for, require_sources
from oracle_eval.paths import (
    DEFAULT_MANIFEST,
    DEFAULT_REPO,
    PREDICTIONS_ROOT,
)

arm_app = typer.Typer(help="Run an arm and write its answers to disk.")


@arm_app.command("models")
def arm_models(
    provider: Annotated[str, typer.Argument(help="groq | gemini")],
) -> None:
    """List what a provider actually serves, so a model ID is pinned not guessed.

    An ID quoted from memory becomes a 404 mid-round.
    """
    from oracle_eval.arms.provider import PROVIDERS, list_models, load_env

    load_env()
    if provider not in PROVIDERS:
        console.print(f"[red]unknown provider[/red], try {', '.join(PROVIDERS)}")
        raise typer.Exit(1)

    chosen = PROVIDERS[provider]
    if chosen.api_key is None:
        console.print(
            f"\n[yellow]{chosen.api_key_env} is not set.[/yellow]  Copy .env.example to "
            f".env.local or .env and paste a key from {chosen.signup}.\n"
            "[dim]Both files are git-ignored. Keys belong there, nowhere else.[/dim]\n"
        )
        raise typer.Exit(1)

    served = list_models(chosen)
    console.print(f"\n[bold]{provider}[/bold]  ·  {len(served)} models\n")
    for model in served:
        console.print(f"  {model}")
    console.print()


@arm_app.command("run")
def arm_run(
    arm: Annotated[str, typer.Argument(help="Directory name under data/predictions")],
    provider: Annotated[str, typer.Option("--provider")],
    model: Annotated[str, typer.Option("--model", help="Pin from `arm models`")],
    prompt_name: Annotated[
        str, typer.Option("--prompt", help="theirs | ours | calls | refs")
    ] = "theirs",
    max_tokens: Annotated[
        int, typer.Option("--max-tokens", help="Output ceiling; counts against Groq's TPM")
    ] = MAX_TOKENS,
    json_mode: Annotated[
        bool,
        typer.Option(
            "--json-mode",
            help="Constrain decoding to valid JSON. Recorded in prompt_version as +json",
        ),
    ] = False,
    split: SplitOption = "dev",
    limit: LimitOption = 0,
    dry_run: Annotated[
        bool, typer.Option("--dry-run", help="Report what would be called, spend nothing")
    ] = False,
    manifest_path: ManifestOption = DEFAULT_MANIFEST,
    repo_root: RepoOption = DEFAULT_REPO,
    root: PredictionsOption = PREDICTIONS_ROOT,
    allow_drift: AllowDriftOption = False,
    spend_test_split: SpendTestSplitOption = False,
) -> None:
    """Run one model arm over a split, through the cache, writing raw responses.

    Scores nothing; a result not re-derivable from a file is not a result.
    """
    from oracle_eval.arms.cache import ResponseCache, cache_key
    from oracle_eval.arms.prompts import SYSTEM, load_prompts
    from oracle_eval.arms.provider import PROVIDERS, Arm, complete, load_env
    from oracle_eval.score.run import write_predictions

    load_env()
    prompts = load_prompts()
    if provider not in PROVIDERS or prompt_name not in prompts:
        console.print(
            f"[red]provider must be one of {', '.join(PROVIDERS)}; "
            f"prompt one of {', '.join(prompts)}[/red]"
        )
        raise typer.Exit(1)

    require_sources(repo_root)
    prompt = prompts[prompt_name]
    version = f"{prompt.version}+json" if json_mode else prompt.version
    spec = Arm(arm, PROVIDERS[provider], model, version, max_tokens, json_mode)
    files = corpus_for(manifest_path, split, limit, repo_root, allow_drift, spend_test_split)
    cache = ResponseCache()

    keys = {f.path: cache_key(model, version, f.sha256, max_tokens) for f in files}
    cached = {path: cache.get(key) for path, key in keys.items()}
    todo = [f for f in files if cached[f.path] is None]

    console.print(
        f"\n[bold]{arm}[/bold]  ·  {provider}/{model}  ·  prompt={version}\n"
        f"  {len(files) - len(todo)} cached  ·  [bold]{len(todo)} calls needed[/bold]\n"
    )
    if dry_run:
        console.print("[dim]--dry-run: nothing called, nothing written.[/dim]\n")
        return
    if spec.provider.api_key is None:
        console.print(
            f"[yellow]{spec.provider.api_key_env} is not set.[/yellow]  Copy .env.example to "
            f".env.local or .env and paste a key from {spec.provider.signup}.\n"
        )
        raise typer.Exit(1)

    from oracle_eval.arms.provider import looks_truncated

    aborted: Exception | None = None
    for index, corpus_file in enumerate(todo, start=1):
        source = (repo_root / corpus_file.path).read_text(encoding="utf8")
        rendered = prompt.render(corpus_file.path, source)
        try:
            answer = complete(spec, SYSTEM, rendered)
            if looks_truncated(len(rendered), answer):
                raise RuntimeError(
                    f"prompt truncated by the server: {len(rendered):,} chars admitted as "
                    f"{answer.prompt_tokens:,} tokens "
                    f"({len(rendered) / answer.prompt_tokens:.1f} chars/token; "
                    "anything over 4.5 means clipping). Raise the model's context window."
                )
        except Exception as error:
            console.print(f"\n  [red]{type(error).__name__}[/red] at {corpus_file.path}\n  {error}")
            aborted = error
            break
        cache.put(
            key=keys[corpus_file.path],
            model=model,
            prompt_version=version,
            file_sha=corpus_file.sha256,
            relative_path=corpus_file.path,
            response=answer.text,
            finish_reason=answer.finish_reason,
            served_by=answer.served_by,
            prompt_tokens=answer.prompt_tokens,
            completion_tokens=answer.completion_tokens,
        )
        if index % 10 == 0 or index == len(todo):
            console.print(f"  [dim]{index}/{len(todo)}[/dim]")

    answers = [entry for f in files if (entry := cache.get(keys[f.path])) is not None]
    written = write_predictions(root, arm, {e.relative_path: e.response for e in answers})
    empty = sum(1 for e in answers if e.is_empty)
    truncated = sum(1 for e in answers if e.is_truncated)
    console.print(
        f"\nwrote [bold]{written}[/bold] responses to {root / arm}"
        f"{f'  ·  [red]{empty} empty[/red]' if empty else ''}"
        f"{f'  ·  [red]{truncated} truncated[/red]' if truncated else ''}"
    )
    if truncated:
        console.print(
            f"[yellow]{truncated} response(s) hit max_tokens={spec.max_tokens}.[/yellow]\n"
            "[dim]Check whether they are repetition loops BEFORE raising the ceiling. A loop is a\n"
            "model failure and a bigger ceiling only buys a longer loop; a genuinely long answer\n"
            "is our failure and the ceiling is the fix. Every truncated case measured on this\n"
            "corpus so far has been a loop, 249 call objects with 6 distinct values, in one.\n"
            "Tell them apart by the ratio of distinct to total emitted objects.[/dim]\n"
        )
    if aborted is not None:
        console.print(
            f"[yellow]incomplete[/yellow], {written}/{len(files)} files. Fix the error above and "
            "re-run the same command; cached files cost nothing.\n"
            "[dim]Do not score a partial arm: the missing files are not misses.[/dim]\n"
        )
        raise typer.Exit(2)
    console.print(f"[dim]score with: harness score run {arm}[/dim]\n")


from oracle_eval.commands import baseline as _baseline  # noqa: E402, F401
