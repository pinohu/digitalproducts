"""Unit tests for idea_scorer.IdeaScore and the backlog renderer."""

from __future__ import annotations

import datetime as dt

import pytest

from idea_scorer import DIMENSIONS, IdeaScore, render_backlog_entry


def _make_idea(scores: dict[str, int], **overrides) -> IdeaScore:
    """Helper to build a fully-populated IdeaScore for tests."""
    base_kwargs = dict(
        name="Test Idea",
        source="https://example.com/thread",
        avatar="Solo SaaS founders at $5K-$20K MRR",
        pitch="I help solo SaaS founders ship faster without burnout.",
        format_guess="PDF",
        price_guess=49,
        watering_holes=["r/SaaS", "Indie Hackers"],
        quotes=["I'd literally pay for this today."],
        scores=dict(scores),
        justifications={k: f"because {k}" for k in scores},
        notes="some notes",
    )
    base_kwargs.update(overrides)
    return IdeaScore(**base_kwargs)


# ---------------------------------------------------------------------------
# total
# ---------------------------------------------------------------------------


def test_total_sums_dimension_scores():
    idea = _make_idea({"pain": 8, "power": 7, "target": 6, "growth": 5, "fit": 4})
    assert idea.total == 30


def test_total_with_empty_scores_is_zero():
    idea = IdeaScore(name="Empty")
    assert idea.total == 0


# ---------------------------------------------------------------------------
# decision
# ---------------------------------------------------------------------------


@pytest.mark.parametrize(
    "scores,expected_substring",
    [
        ({"pain": 10, "power": 10, "target": 10, "growth": 10, "fit": 10}, "Active sprint"),
        ({"pain": 8, "power": 8, "target": 8, "growth": 8, "fit": 8}, "Active sprint"),
        ({"pain": 7, "power": 7, "target": 7, "growth": 6, "fit": 5}, "Strong"),
        ({"pain": 5, "power": 5, "target": 5, "growth": 5, "fit": 6}, "Backlog"),
        ({"pain": 4, "power": 4, "target": 4, "growth": 4, "fit": 4}, "Weak"),
        ({"pain": 1, "power": 1, "target": 1, "growth": 1, "fit": 1}, "Killed"),
    ],
)
def test_decision_matches_thresholds(scores, expected_substring):
    idea = _make_idea(scores)
    assert expected_substring.lower() in idea.decision.lower()


# ---------------------------------------------------------------------------
# status_bucket
# ---------------------------------------------------------------------------


@pytest.mark.parametrize(
    "total_target,expected",
    [
        (50, "Active Sprint Candidate"),
        (40, "Active Sprint Candidate"),
        (35, "Strong"),
        (30, "Strong"),
        (27, "Backlog"),
        (25, "Backlog"),
        (20, "Weak"),
        (15, "Weak"),
        (10, "Killed"),
        (0, "Killed"),
    ],
)
def test_status_bucket_matches_thresholds(total_target, expected):
    # Distribute the total roughly across 5 dims
    base = total_target // 5
    remainder = total_target - base * 5
    scores = {dim["key"]: base for dim in DIMENSIONS}
    # tack on remainder to first dim
    first_key = DIMENSIONS[0]["key"]
    scores[first_key] += remainder
    idea = _make_idea(scores)
    assert idea.total == total_target
    assert idea.status_bucket == expected


# ---------------------------------------------------------------------------
# render_backlog_entry
# ---------------------------------------------------------------------------


def test_render_backlog_entry_contains_expected_substrings():
    idea = _make_idea(
        {"pain": 8, "power": 7, "target": 7, "growth": 6, "fit": 5},
        name="Newsletter Monetization Playbook",
    )
    entry = render_backlog_entry(idea)

    assert "## Newsletter Monetization Playbook" in entry
    assert "**Date scored:**" in entry
    assert dt.date.today().isoformat() in entry
    assert "**Source:** https://example.com/thread" in entry
    assert "**Status:** Strong" in entry
    assert "Massive Pain: 8/10" in entry
    assert "Purchasing Power: 7/10" in entry
    assert "Easy to Target: 7/10" in entry
    assert "Growing Market: 6/10" in entry
    assert "Personal Fit: 5/10" in entry
    assert "**Total: 33/50**" in entry
    assert "**Decision:** Strong" in entry
    assert "Solo SaaS founders" in entry  # avatar
    assert "I'd literally pay for this today" in entry  # quote
    assert "r/SaaS" in entry  # watering hole


def test_render_backlog_entry_handles_missing_optional_fields():
    idea = IdeaScore(
        name="Bare Idea",
        source="(none)",
        avatar="(TBD)",
        pitch="(TBD)",
        scores={dim["key"]: 0 for dim in DIMENSIONS},
        justifications={dim["key"]: "unscored" for dim in DIMENSIONS},
    )
    entry = render_backlog_entry(idea)
    assert "## Bare Idea" in entry
    assert "(no verbatim quotes recorded)" in entry
    assert "(none recorded)" in entry
    assert "(no additional notes)" in entry
    assert "**Total: 0/50**" in entry


def test_panel_fallback_supports_constructor_and_fit(monkeypatch):
    """The no-rich fallback must mirror rich.Panel's constructor AND
    `Panel.fit(...)`. collect_idea_metadata calls Panel.fit; show_dimension
    calls Panel(...). Regression test for the AttributeError that occurred
    when the fallback was a plain function rather than a class."""
    import builtins
    import importlib
    import sys

    real_import = builtins.__import__

    def _block_rich(name, *args, **kwargs):
        if name == "rich" or name.startswith("rich."):
            raise ImportError(f"blocked for test: {name}")
        return real_import(name, *args, **kwargs)

    # Drop any cached rich + idea_scorer so the import goes through the patched
    # builtin and exercises the fallback branch.
    for mod in list(sys.modules):
        if mod == "idea_scorer" or mod == "rich" or mod.startswith("rich."):
            del sys.modules[mod]

    monkeypatch.setattr(builtins, "__import__", _block_rich)
    try:
        scorer_no_rich = importlib.import_module("idea_scorer")
    finally:
        # Drop the no-rich version so other tests get a clean import.
        sys.modules.pop("idea_scorer", None)

    Panel = scorer_no_rich.Panel
    p1 = Panel("hello", border_style="cyan")
    p2 = Panel.fit("world", border_style="cyan")
    assert "hello" in str(p1)
    assert "world" in str(p2)
