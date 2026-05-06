# Prompt Library

Index of all Claude / LLM prompts used across the digital products system. Each entry links to the file containing the full prompt.

## Why This Index Exists

Prompts get reused, evolved, and copy-pasted across contexts. Without an index:
- Updates happen in one file but not others (drift)
- Operators forget which prompt exists for which task
- New prompts get reinvented instead of adapted from existing ones

The index keeps every prompt findable in <10 seconds.

## Idea Discovery Prompts

| Prompt | Purpose | File |
|---|---|---|
| Reddit mining | Extract candidates from Reddit thread dumps | [`/01-market-research/idea-discovery/mining-prompts/reddit-mining.md`](../01-market-research/idea-discovery/mining-prompts/reddit-mining.md) |
| Twitter/X mining | Extract candidates from X complaint threads | [`/01-market-research/idea-discovery/mining-prompts/twitter-mining.md`](../01-market-research/idea-discovery/mining-prompts/twitter-mining.md) |
| LinkedIn mining | Extract B2B candidates from LinkedIn comments | [`/01-market-research/idea-discovery/mining-prompts/linkedin-mining.md`](../01-market-research/idea-discovery/mining-prompts/linkedin-mining.md) |
| Audience reply mining | Extract candidates from your own audience replies | [`/01-market-research/idea-discovery/mining-prompts/audience-reply-mining.md`](../01-market-research/idea-discovery/mining-prompts/audience-reply-mining.md) |
| Gumroad bestseller analysis | Reverse-engineer proven categories | [`/01-market-research/idea-discovery/mining-prompts/gumroad-bestseller-analysis.md`](../01-market-research/idea-discovery/mining-prompts/gumroad-bestseller-analysis.md) |
| Competitor gap analysis | Find positioning gaps in competitor offers | [`/01-market-research/idea-discovery/mining-prompts/competitor-gap-analysis.md`](../01-market-research/idea-discovery/mining-prompts/competitor-gap-analysis.md) |
| Trend analysis | Synthesize quantitative growth signals | [`/01-market-research/idea-discovery/mining-prompts/trend-analysis.md`](../01-market-research/idea-discovery/mining-prompts/trend-analysis.md) |

## Claude Skill Prompts (Embedded in Skill Definitions)

| Skill | Purpose | File |
|---|---|---|
| dynasty-idea-validator | 50-point scoring + validation worksheet | [`/automation/claude-skills/idea-validator.md`](./claude-skills/idea-validator.md) |
| dynasty-offer-engineer | Build Grand Slam Offer from product brief | [`/automation/claude-skills/offer-engineer.md`](./claude-skills/offer-engineer.md) |
| dynasty-sales-page-writer | Generate 12-section sales page | [`/automation/claude-skills/sales-page-writer.md`](./claude-skills/sales-page-writer.md) |
| dynasty-launch-manager | Orchestrate launches + reviews | [`/automation/claude-skills/launch-manager.md`](./claude-skills/launch-manager.md) |

## Naming Convention

When adding a new prompt:

- **File name:** `<purpose>-<source-or-context>.md` (e.g., `reddit-mining.md`, `twitter-mining.md`)
- **Top of file:** A 1-sentence description and a "When to Use" section before the prompt itself
- **Prompt body:** Inside a code block with `\`\`\`` so it can be copy-pasted cleanly
- **End of file:** "Common Failure Modes" section with anti-patterns

## Versioning

When a prompt changes meaningfully (not minor wording), append a version note at the bottom of the file:

```
## Versions

- v1.0 (2026-05-06): Initial version
- v1.1 (2026-08-15): Added engagement signal weighting
- v2.0 (2026-11-01): Restructured around 5-dimensional scoring output
```

Don't keep multiple files for versions — the file is always the current version. Use git history if you need to recover an old version.

## Adding a New Prompt

1. Create file in the right folder (mining prompts in `01-market-research/idea-discovery/mining-prompts/`, others as appropriate)
2. Follow the format above
3. Add a row to this index
4. Test the prompt with at least 2 different inputs before considering it canonical

## Testing Prompts

Every new prompt should be tested against:
- A "happy path" input that should produce strong output
- An "edge case" input (sparse data, ambiguous patterns)
- A "negative case" input where the right answer is "no candidates" (to verify the prompt doesn't manufacture false positives)

If the prompt fails any of these, fix the prompt — don't ship it and hope.

## What This System Replaces

Without this library, prompt management looks like:
- Prompts living in browser tabs, lost on browser restart
- Slightly different versions of the same prompt across team members
- Operators reinventing prompts because they didn't know one existed
- No record of what changed in a prompt that suddenly stopped working

With this library: every prompt is findable, versioned, attributed to a purpose, and testable.
