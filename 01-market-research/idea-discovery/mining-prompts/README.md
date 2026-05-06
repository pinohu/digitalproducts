# Mining Prompts

Pre-written Claude / LLM prompts for analyzing each data source. Each prompt is a self-contained instruction that takes raw text from a source and outputs candidate ideas in the standard format.

## How to Use

1. Pick the prompt matching your data source (`reddit-mining.md`, `twitter-mining.md`, etc.)
2. Paste the prompt's "system" section into Claude / your LLM
3. Paste the raw text data (Reddit thread dump, X thread, etc.) as the user message
4. Claude returns candidate ideas in the standard format
5. Append output to `../idea-backlog.md` Detailed Records section
6. Score each idea using `../scoring-rubric.md`

## Files

- [`reddit-mining.md`](./reddit-mining.md) — Pain-point extraction from Reddit threads
- [`twitter-mining.md`](./twitter-mining.md) — Complaint and "I wish" pattern extraction from X
- [`linkedin-mining.md`](./linkedin-mining.md) — B2B comment patterns on LinkedIn
- [`audience-reply-mining.md`](./audience-reply-mining.md) — Pattern extraction from your own audience replies
- [`gumroad-bestseller-analysis.md`](./gumroad-bestseller-analysis.md) — Reverse-engineering proven categories
- [`competitor-gap-analysis.md`](./competitor-gap-analysis.md) — Finding gaps in competitor offers
- [`trend-analysis.md`](./trend-analysis.md) — Synthesizing Google Trends + Exploding Topics + community size data

## Conventions

All prompts produce output in this format:

```
### Candidate: [Idea Name]

- Source: [URL or description]
- Pattern matched: [which signal pattern]
- Verbatim quote: "[exact words from the source]"
- One-sentence pitch: I help [avatar] solve [problem] without [objection].
- Pre-score (rough): Pain X/10, Power X/10, Target X/10, Growth X/10, Fit X/10
- Watering holes: [list]
```

This is intentionally identical to the format `tools/reddit_miner.py` outputs, so manual + automated mining produce compatible records.
