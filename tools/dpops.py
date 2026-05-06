#!/usr/bin/env python3
"""
dpops.py — Unified entrypoint for the digital products toolset.

Subcommands delegate to the individual scripts:

    dpops score       -> idea_scorer.py
    dpops mine        -> reddit_miner.py
    dpops trends      -> trends_checker.py
    dpops bootstrap   -> product_bootstrapper.py

All flags after the subcommand are passed through to the underlying script
unchanged, so existing per-tool documentation continues to apply.

Examples:
    python tools/dpops.py score
    python tools/dpops.py mine --subreddits SaaS,Solopreneur --dry-run
    python tools/dpops.py trends "newsletter monetization"
    python tools/dpops.py bootstrap --slug 02-newsletter-monetization \\
        --title "Newsletter Monetization Playbook"
"""

from __future__ import annotations

import sys


SUBCOMMANDS = {
    "score": ("idea_scorer", "Score an idea (delegates to idea_scorer.py)."),
    "mine": ("reddit_miner", "Mine Reddit for candidate ideas (delegates to reddit_miner.py)."),
    "trends": ("trends_checker", "Check Google Trends growth signal (delegates to trends_checker.py)."),
    "bootstrap": ("product_bootstrapper", "Scaffold a new product (delegates to product_bootstrapper.py)."),
}


def _delegate(module_name: str, args: list[str]) -> None:
    """Run a delegated script's main() with sys.argv replaced by `args`."""
    import importlib

    module = importlib.import_module(module_name)
    if not hasattr(module, "main"):
        print(f"Module {module_name} has no main() function.", file=sys.stderr)
        sys.exit(1)
    original = sys.argv[:]
    try:
        sys.argv = [module_name] + list(args)
        module.main()
    finally:
        sys.argv = original


def _build_cli():
    """Build the click CLI lazily (only when click is installed)."""
    import click

    @click.group(
        context_settings={
            "help_option_names": ["-h", "--help"],
            "ignore_unknown_options": True,
        }
    )
    def cli() -> None:
        """Digital Products Ops — unified CLI for the tools/ scripts."""

    def _make_subcommand(name: str, module_name: str, help_text: str):
        @cli.command(
            name=name,
            help=help_text,
            context_settings={
                "ignore_unknown_options": True,
                "allow_extra_args": True,
            },
        )
        @click.pass_context
        def _cmd(ctx: click.Context) -> None:
            _delegate(module_name, list(ctx.args))

        return _cmd

    for name, (module_name, help_text) in SUBCOMMANDS.items():
        _make_subcommand(name, module_name, help_text)

    return cli


def main() -> None:
    try:
        import click  # noqa: F401
    except ImportError:
        print(
            "Missing 'click'. Run: pip install -r requirements.txt",
            file=sys.stderr,
        )
        sys.exit(1)
    cli = _build_cli()
    cli(standalone_mode=True)


if __name__ == "__main__":
    main()
