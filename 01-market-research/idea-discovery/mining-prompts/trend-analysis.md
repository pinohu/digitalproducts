# Trend Analysis Prompt

Synthesizes growth signals across Google Trends, Exploding Topics, community size data, and search volume to validate the "Growing Market" dimension of the scoring rubric.

## When to Use

Once an idea has scored 6+ on Pain, Power, Target, and Fit but you're unsure about Growth (Dimension 4). Run this prompt with quantitative trend data to settle the question.

## The Prompt (Copy-Paste into Claude)

```
You are analyzing market trend signals to determine whether a candidate
digital product idea is targeting a growing, stable, or shrinking market.

Input: Trend data and supporting context for a candidate idea.

The candidate idea: [PASTE THE ONE-SENTENCE PITCH]

Trend data (paste any/all of the following):
- Google Trends data for the primary keyword(s) over the last 24 months
- Exploding Topics rating
- Subreddit / community member count change
- Industry report data (search volume, market size growth)
- AppSumo or Product Hunt category trajectory
- Any other quantitative signal

Output:

## Trend Verdict: [GROWING / STABLE / DECLINING / MIXED SIGNALS / INSUFFICIENT DATA]

## Growth Score (0-10)
With justification. Reference the rubric:
- 10: 30%+ growth in last 24 months across multiple metrics, accelerating
- 8: Clear upward trajectory, well-documented
- 6: Stable, not declining
- 4: Mixed signals
- 2: Flat or slightly declining
- 0: Demonstrably shrinking

## Evidence
List 3-5 specific data points. Quote numbers. Specify time windows.

## Confidence Level
- HIGH: 3+ independent quantitative sources agree
- MEDIUM: 2 sources agree
- LOW: 1 source or all sources are qualitative

## Confounders
What might make this trend reading misleading?
- Seasonality (e.g., "tax software" peaks Q1)
- Hype cycles (e.g., crypto / Web3 / AI tooling all had inflation periods)
- Tool-specific trends vs. category trends (e.g., specific SaaS tool grew, but
  the underlying problem may have shrunk because tool consolidated demand)
- Geographic effects (US trends vs. global)

## Recommendation
- [BUILD: Growth score 8+, high confidence] → Move idea forward
- [VALIDATE FURTHER: Growth score 6-7] → Pre-sale or waitlist before sprinting
- [PARK: Growth score 4-5] → Keep in backlog, re-score in 90 days
- [KILL: Growth score 0-3] → Mark as killed in backlog, document reason

Hard rules:
- Don't manufacture optimism. If the data says flat or declining, say so.
- Don't extrapolate one strong data point. A single 200% growth metric in
  one source might be noise; require corroboration.
- Time windows matter. 24 months is the default lookback. 12 months is too
  short (can be hype). 5 years is too long (markets shift).
```

## Free Tools to Pull Trend Data

| Tool | What It Gives You | Cost |
|---|---|---|
| **Google Trends** | Search volume trajectory by keyword + region | Free |
| **Exploding Topics** | Curated emerging-trend list with ratings | Free tier (limited) |
| **Reddit subreddit metrics** | Member count + growth via subredditstats.com | Free |
| **Indie Hackers** | Product revenue and growth (when shared by creators) | Free |
| **Crunchbase** | Funding and revenue signals for adjacent SaaS | Free tier (limited) |
| **SimilarWeb** | Traffic to competitor sites (rough) | Free tier |
| **SEMrush / Ahrefs** | Keyword search volume + competition | Paid |
| **GitHub stars** | For dev-tool adjacent ideas, star growth on related repos | Free |
| **Awario / Brand24** | Mention-volume tracking | Paid |

For a typical idea, pull data from Google Trends + Exploding Topics + the relevant community member count. That trio is usually enough.

## What This Prompt Catches That Manual Analysis Misses

- **Inflated optimism:** Humans want their idea to be growing; this prompt forces evidence
- **Confounders:** Seasonality, hype cycles, geographic effects often hide in trend data
- **Confidence calibration:** Single-source data points often look stronger than they are
- **Decision linkage:** The output explicitly maps to the build/validate/park/kill decision in the scoring rubric
