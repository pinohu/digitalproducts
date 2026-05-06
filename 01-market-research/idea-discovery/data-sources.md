# Data Sources

The exhaustive list of places to mine for digital product ideas. Quality-rated. Use the highest-rated sources first.

## Tier 1: High Signal, Audience-Aligned

These sources match the Dynasty Empire avatar (technical operators) and reliably produce 1-3 strong candidates per mining pass.

| Source | Why It's Tier 1 | Mining Tool / Method |
|---|---|---|
| **Email replies from your own audience** | Highest-signal data on Earth. Direct from buyers and prospects. | Manual review, weekly. Tag patterns in [`mining-prompts/audience-reply-mining.md`](./mining-prompts/audience-reply-mining.md). |
| **r/SaaS, r/SmallBusiness, r/Solopreneur** | High pain-density, B2B audience, technical buyers | `tools/reddit_miner.py`, see [`mining-prompts/reddit-mining.md`](./mining-prompts/reddit-mining.md) |
| **Indie Hackers forum + interviews** | Pre-vetted creator/operator audience, problems are explicit | Manual + Claude analysis |
| **Comments on niche LinkedIn posts** | Direct B2B avatar, complaint patterns | LinkedIn search + Claude analysis, see [`mining-prompts/linkedin-mining.md`](./mining-prompts/linkedin-mining.md) |
| **AppSumo product Q&A sections** | Explicit feature requests = explicit unmet needs | Manual review of top 20 products in target niche |
| **Gumroad / ThriveCart bestseller lists** | Proven categories with revenue data | Manual review monthly, see [`mining-prompts/gumroad-bestseller-analysis.md`](./mining-prompts/gumroad-bestseller-analysis.md) |

## Tier 2: Good Signal, Wider Audience

Useful but more noise. Use after Tier 1 is exhausted.

| Source | Why It's Tier 2 | Mining Tool / Method |
|---|---|---|
| **r/Entrepreneur, r/freelance, niche subreddits** | Higher noise than r/SaaS, but more reach | `tools/reddit_miner.py` with niche subreddit list |
| **X/Twitter complaint threads** | Real-time pain, but harder to filter from venting | Twitter search + Claude analysis, see [`mining-prompts/twitter-mining.md`](./mining-prompts/twitter-mining.md) |
| **Product Hunt launches + comments** | What's being built right now, what's missing | Weekly skim of Product Hunt |
| **Google Trends rising queries** | Quantitative trend signal | `tools/trends_checker.py` |
| **Exploding Topics** | Curated emerging-trend list | Manual review of category pages |
| **YouTube tutorial comments** | "I'm stuck at this part" = pain-point gold | Search + Claude analysis on transcripts |
| **Hacker News "Ask HN" threads** | High-quality questions from technical audience | Manual review, weekly |

## Tier 3: Inspirational, Low Signal

Use sparingly. These give context but rarely surface direct ideas.

| Source | Why It's Tier 3 | Mining Tool / Method |
|---|---|---|
| **Newsletter "what I'm thinking about" sections** | Mostly opinion, occasionally a missed opportunity | Read top 5 newsletters in space weekly |
| **Podcast episode descriptions** | What hosts think their audience wants to know | Skim Spotify/Apple Podcasts category pages |
| **Industry reports / annual surveys** | Macro signals, slow-moving | Quarterly review |
| **Competitor sales page FAQs** | What competitors think their buyers ask | Reverse-engineer competitor offers |

## Don't Mine

These sources reliably generate bad ideas:

- ❌ **General Twitter / X feed** — too much noise, too many performative complaints
- ❌ **TikTok / Instagram** — wrong audience for technical/B2B products
- ❌ **Quora** — quality has degraded, mostly SEO-bait
- ❌ **Random Slack communities you don't already participate in** — you can't tell signal from noise without context
- ❌ **AI-generated trend reports** — they hallucinate, especially on niche markets

## How Often to Mine Each Source

| Cadence | Sources |
|---|---|
| **Daily** (5 min) | Email replies (already in your inbox) |
| **Weekly** (15 min) | Tier 1 Reddit, AppSumo Q&A, IndieHackers |
| **Monthly** (60 min) | All of Tier 1 + Tier 2 + Gumroad bestsellers + Google Trends sweep |
| **Quarterly** (2 hours) | Full Tier 1 + 2 + 3 sweep, recalibrate scoring rubric, archive stale ideas |

## What to Mine For (Pattern Library)

Across all sources, these linguistic patterns are the strongest signals:

| Pattern | Example | What It Signals |
|---|---|---|
| **"I wish there was..."** | "I wish there was a tool that..." | Unmet need, often willing to pay |
| **"How do I..." (repeated)** | Same question across many threads | Generic problem, mass demand |
| **"Best way to..." with no clear answer** | "Best way to [X]" with conflicting replies | Genuine confusion, framework opportunity |
| **"I keep doing this manually..."** | "Every Monday I have to..." | Automation opportunity |
| **"Has anyone tried..."** | "Has anyone tried [tool X] for [niche Y]?" | Niche-specific demand without clear product |
| **Specific dollar costs of pain** | "I'm losing $X per month because..." | High purchasing power signal |
| **Time-related complaints** | "It takes me 4 hours to..." | Time-savings opportunity |
| **"Spreadsheet hell"** | Anything mentioning a manual spreadsheet | Tool/template opportunity |
| **Repeated complaint about a specific tool** | "[Big tool X] doesn't do [thing Y]" | Companion / wrapper / alternative opportunity |

The mining prompts in [`mining-prompts/`](./mining-prompts/) are pre-written to find these patterns systematically.

## Output Format

Every mining session produces a list of candidate ideas in this format:

```
### [Candidate Idea Name]

- **Source:** [URL or description]
- **Pattern:** [which signal pattern triggered this]
- **Quote:** [exact verbatim quote from source if applicable]
- **Initial guess:** [one-sentence guess at what the product would be]
- **Pre-score:** [rough 1-10 on each rubric dimension; full scoring happens later]
```

These get appended to [`idea-backlog.md`](./idea-backlog.md) for full scoring.
