# Idea Discovery

The system for systematically generating digital product ideas that meet the four starving-crowd criteria. Replaces "what should I make?" guessing with a repeatable mining + scoring + prioritization pipeline.

## The Problem This Solves

Most creators pick product ideas based on:
- What they personally find interesting
- What they happened to read about that week
- What a friend suggested
- What feels safe / familiar

That's why most digital products fail. They're solving problems the creator likes, not problems a starving crowd is willing to pay to solve.

This system flips it: **mine the world for pain points, score each candidate against four hard criteria, prioritize ruthlessly, and only build what passes.**

## The Pipeline

```
Data Sources              Mining                    Scoring                    Backlog
──────────────            ───────                   ───────                    ─────────
Reddit (PRAW)        →    pain-point extraction →    50-point rubric    →     idea-backlog.md
X/Twitter            →    "I wish" / "how do I"      (5 dims × 10 pts)         (ordered by score)
LinkedIn comments    →    "looking for tool"         + personal fit                  ↓
Indie Hackers        →    "best way to..."           + scoring rationale       Sprint candidate
YouTube comments     →    complaint clustering                                       ↓
AppSumo Q&A          →    feature gap analysis                              Validation worksheet
Gumroad bestsellers  →    proven category mining                                     ↓
Google Trends        →    rising-interest signals                            Pre-sale or beta
Email replies        →    direct buyer feedback                                      ↓
                                                                              Sprint slot
```

## Files in this folder

- [`README.md`](./README.md) — this file
- [`data-sources.md`](./data-sources.md) — exhaustive list of where to mine, with quality ratings
- [`scoring-rubric.md`](./scoring-rubric.md) — the 50-point scoring system, dimension by dimension
- [`idea-backlog.md`](./idea-backlog.md) — the running, ordered list of ideas with scores
- [`mining-prompts/`](./mining-prompts/) — Claude prompts for analyzing each data source

## How to Use This System

### Weekly cadence (15 min)

1. Run the Reddit miner: `python tools/reddit_miner.py` (see [`tools/README.md`](../../tools/README.md))
2. Skim raw output, copy the top 5 candidates
3. For each candidate, run through the [`scoring-rubric.md`](./scoring-rubric.md) — takes ~3 min per idea
4. Add ideas scoring 25+ to [`idea-backlog.md`](./idea-backlog.md)

### Monthly cadence (60 min)

1. Re-mine all data sources (Reddit, X, LinkedIn, Gumroad bestsellers, Google Trends)
2. Re-score top 20 backlog ideas in light of new data
3. Promote highest-scorer to "next sprint candidate" in [`/ROADMAP.md`](../../ROADMAP.md)
4. Archive ideas that haven't moved above 25/50 in 90 days

### Per-sprint (1 hour, on the day a sprint slot opens)

1. Pull the highest-scored backlog idea
2. Open [`/01-market-research/niche-validation-template.md`](../niche-validation-template.md), copy to `/01-market-research/by-product/<slug>/validation.md`, fill it in
3. Run [`/01-market-research/competitor-analysis-template.md`](../competitor-analysis-template.md)
4. Pre-sell signal check (waitlist, landing page, or direct outreach)
5. If still passes: promote to active sprint. Open [`/10-execution-sprints/current-sprint.md`](../../10-execution-sprints/current-sprint.md)

## Anti-Patterns

- ❌ **Mining once and using forever.** Trends shift quarterly. Re-mine.
- ❌ **Ignoring low-scoring ideas because you "feel" they could work.** The score is the score. If you keep overriding it, recalibrate the rubric — don't override the rubric.
- ❌ **Building from the top of the backlog without re-validating.** Ideas at the top might have been mined 6 months ago. Re-validate before sprinting.
- ❌ **Mining data sources that don't match the avatar.** If your audience is on LinkedIn, mining Instagram comments is theater.
- ❌ **Scoring inflation.** If everything scores 35+, the rubric is broken. Recalibrate so the median idea sits at 20-25.

## What "Automation" Means Here

This system is *augmented*, not fully autonomous. The mining is automated. The scoring rubric is structured. But human judgment still sets the priority, decides which mining outputs are real signal vs. noise, and makes the build/kill calls.

Total time per week with this system fully running: ~30 min for ongoing mining + scoring. Total time for fully manual idea generation without this system: ~5-10 hours of unfocused thinking that usually produces a worse result anyway.
