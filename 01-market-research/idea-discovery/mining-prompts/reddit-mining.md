# Reddit Mining Prompt

Use this prompt with Claude or any LLM to extract digital product candidates from Reddit thread dumps.

## When to Use

After running `tools/reddit_miner.py` (or manually pulling threads from r/SaaS, r/Solopreneur, r/Entrepreneur, r/SmallBusiness, or any niche subreddit). The script outputs raw thread text; this prompt extracts structured candidates.

## The Prompt (Copy-Paste into Claude)

```
You are mining Reddit threads for digital product opportunities.

Goal: Extract candidate digital product ideas that meet starving-crowd criteria
(massive pain, purchasing power, easy to target, growing market).

Input: A dump of Reddit posts and comments below.

For each candidate idea you identify, output ONE record in this exact format:

### Candidate: [Concise idea name, ~5-8 words]

- Source: [URL of the Reddit thread]
- Subreddit: r/[name]
- Pattern matched: [one of: "I wish there was..." / "How do I..." / "Best way to..."
  / "I keep doing X manually" / "Has anyone tried..." / "Specific dollar/time cost"
  / "Spreadsheet hell" / "Tool X doesn't do Y"]
- Verbatim quote: "[copy exact words from the thread, no paraphrasing]"
- One-sentence pitch: I help [specific person] solve [specific problem] without [common objection].
- Pre-score (rough, 1-10 each): Pain X, Power X, Target X, Growth X, Fit X
- Format guess: [PDF / template / mini-course / Notion template / spreadsheet / etc.]
- Price guess: $XX
- Watering holes (3+ specific places this audience also gathers):
  1.
  2.
  3.
- Notes: [1-2 sentences of context]

Hard rules:
- Only include candidates where you found at least one verbatim pain-point quote.
  No quote = not a candidate.
- Only include candidates where you can name a specific avatar (not "small business
  owners" — use "Shopify store owners doing $20K-$50K/mo who handle their own
  fulfillment" or similar specificity).
- Skip threads that are pure venting with no actionable problem.
- Skip threads that are about consumer/B2C topics (cooking, fitness, dating)
  unless the avatar is a professional in that space.
- If the same problem appears in multiple threads, consolidate into ONE candidate
  and note the recurrence ("Pattern appears in 3+ threads").
- Limit output to the top 5 candidates per session. Don't dilute with weaker ideas.

If no strong candidates are present in the input, return:
"No candidates meeting threshold. Patterns observed: [list patterns that were
present but didn't reach the bar]."

Now process the following Reddit data:

[PASTE REDDIT DATA HERE]
```

## Tips for Better Output

- **Pre-filter your input.** Don't paste 200 threads. Paste 20-30 high-engagement threads from a single subreddit at a time. Quality > quantity.
- **Run separate sessions per subreddit.** A r/SaaS session and a r/Solopreneur session produce different patterns; mixing them dilutes the analysis.
- **Re-run quarterly on the same subreddits.** Pain points evolve. The candidate from Q1 may have been solved by Q3.

## Common Failure Modes

- ❌ **Generic outputs.** If the candidate avatar is "entrepreneurs," the prompt failed. Force specificity: re-run with "Be specific about avatar — name a job title, revenue range, and tool stack."
- ❌ **Theoretical pain.** If the verbatim quote is mild ("would be nice if..."), the pain score is ≤ 4. Don't promote weak signals.
- ❌ **One-thread wonders.** A pattern in only one thread might be one person's idiosyncratic problem. Cross-check by searching the subreddit for the same pattern before promoting.

## Scaling Up

Once this prompt produces consistent good output, the same prompt can be run automatically inside an n8n workflow:

1. n8n triggers weekly
2. Reddit API pulls top threads from configured subreddits
3. Threads → Claude API with this prompt
4. Output appended to `idea-backlog.md` via Git commit
5. Notification fires when new high-score candidates appear

See [`automation/n8n-workflows/idea-discovery-pipeline.md`](../../../automation/n8n-workflows/idea-discovery-pipeline.md) for the full automation spec.
