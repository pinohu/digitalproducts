# Competitor Gap Analysis Prompt

Different from "competitor analysis" (which validates a niche has competitors). This prompt finds the *gaps in existing competitor offers* that become your positioning advantage.

## When to Use

Once you've identified 3-5 direct competitors for a candidate idea (via `01-market-research/competitor-analysis-template.md`), run this prompt to find the structural gaps.

## The Prompt (Copy-Paste into Claude)

```
You are doing a structured gap analysis on existing competitor offers in a niche.

Input: 3-5 competitor sales pages, with their headline, pricing, key promises,
bonuses, and (where visible) reviews/testimonials.

Output 4 sections:

SECTION 1: Format Map
What format is each competitor using? (PDF / video course / template / etc.)
Is there a format gap?

SECTION 2: Audience Map
Who is each competitor targeting? (beginner / intermediate / expert; consumer /
B2B; specific job role)
Is there an audience gap?

SECTION 3: Depth Map
What aspects does each competitor cover deeply? What aspects do they cover
poorly or skip entirely? Is there a depth/specificity gap?

SECTION 4: Positioning Synthesis
Based on the above, what's the single most defensible positioning for a new
entrant? Fill in:

> Unlike [competitor pattern], our product [unique angle], for [specific buyer],
> who wants [specific outcome] without [common pain in this space].

Then give 2-3 alternative positioning angles, ranked by defensibility.

For each angle:
- Why it's defensible (what makes it hard for competitors to copy quickly)
- What the headline + sub-headline would look like
- What 1 unique bonus would amplify this positioning

Hard rules:
- Don't recommend "be cheaper" as positioning. That's a race to the bottom.
- Don't recommend "be slightly better" — no one switches for slightly better.
- Recommend angles that involve a real, defensible differentiator: format,
  audience specificity, depth on a specific aspect, or unfair advantage of the creator.

Now analyze:

[PASTE COMPETITOR SALES PAGES / DATA]
```

## What Makes a Good Gap

| Gap Type | Strength | Example |
|---|---|---|
| Format gap | Strong | Everyone has video courses; you ship a printable + Notion template combo |
| Specificity gap | Strongest | Everyone targets "founders"; you target "solo SaaS founders at $5K-$20K MRR" |
| Depth gap | Strong | Everyone covers 50 topics shallowly; you cover 1 topic exhaustively |
| Audience gap | Strong | Everyone targets beginners; you target experienced operators (and vice versa) |
| Price gap | Weak alone | Cheaper isn't a strategy; cheaper + clearer scope can be |
| Brand gap | Weak alone | "More approachable" / "more professional" rarely converts on its own |

The best positioning combines 2-3 gap types. "Specificity gap (solo SaaS at $5K-$20K MRR) + depth gap (one specific stage of growth) + format gap (template + walkthrough)" is much stronger than any single gap.

## What This Prompt Avoids

- Cataloging features (boring, not actionable)
- Listing what competitors "do well" (you don't need to copy their wins)
- Generic "be different" advice (define HOW)
