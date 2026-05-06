# Idea Backlog

The running list of digital product candidates, ordered by total score (highest first). New ideas enter via mining sessions; ideas exit when they get promoted to a sprint, killed, or auto-archived after 90 days at <25.

## Backlog Status

| | Count |
|---|---|
| Active sprint candidates (40+) | 0 |
| Strong (30-39) | 0 |
| Backlog (25-29) | 0 |
| Weak (15-24) | 0 |
| Killed / archived | 0 |
| **Total scored ideas** | **0** |

_First mining pass pending. Run `python tools/reddit_miner.py` and complete a Reddit + AppSumo Q&A sweep to populate._

---

## Active Sprint Candidates (Score 40+)

_(highest-scoring ideas, ready for validation worksheet)_

| # | Idea | Score | Date Scored | Source | Notes |
|---|---|---|---|---|---|
| | | | | | |

---

## Strong (Score 30–39)

_(validate with pre-sale or waitlist before promoting)_

| # | Idea | Score | Date Scored | Source | Notes |
|---|---|---|---|---|---|
| | | | | | |

---

## Backlog (Score 25–29)

_(hold; re-score quarterly; build only if higher options dry up)_

| # | Idea | Score | Date Scored | Source | Notes |
|---|---|---|---|---|---|
| | | | | | |

---

## Weak (Score 15–24)

_(park here; only promote if a path to fixing weak dimensions emerges)_

| # | Idea | Score | Date Scored | Source | Path to Fix |
|---|---|---|---|---|---|
| | | | | | |

---

## Killed (Score 0–14 or Strategic Kill)

| # | Idea | Score | Date | Reason |
|---|---|---|---|---|
| | | | | |

---

## Detailed Idea Records

_Each idea promoted into the backlog gets a fuller record below with all 5 dimension scores, justifications, and a 1-paragraph synthesis. Use the template below._

### Template

```
## [Idea N] — [Idea Name]

**Date scored:** YYYY-MM-DD
**Source:** [URL or description]
**Status:** [Active candidate / Strong / Backlog / Weak / Killed]

**Scoring (out of 50):**
- Massive Pain: X/10 — [one-sentence justification]
- Purchasing Power: X/10 — [one-sentence justification]
- Easy to Target: X/10 — [one-sentence justification]
- Growing Market: X/10 — [one-sentence justification]
- Personal Fit: X/10 — [one-sentence justification]
- **Total: XX/50**

**One-sentence pitch:**
> *I help [avatar] solve [problem] without [common objection].*

**Initial format guess:**
[PDF / template / mini-course / etc.]

**Initial price guess:**
$XX

**Watering holes:**
1.
2.
3.

**Verbatim pain-point quotes:**
> *"[quote 1 from source]"*
> *"[quote 2 from source]"*

**Decision:** [What's the next step? Validation worksheet, kill, hold for re-score]

**Notes:**
[Free-form context]
```

---

## How Ideas Move Through This File

```
[Mining session output]
       ↓
[Top section: Detailed Idea Records — full scoring entered]
       ↓
[Decision threshold determines bucket: Active/Strong/Backlog/Weak/Killed]
       ↓
[Idea reference added to the appropriate bucket table at the top of this file]
       ↓
(Quarterly) [Re-scored, may move buckets or get killed]
       ↓
(When sprint slot opens) [Highest-scored candidate gets promoted to validation]
       ↓
[Validation worksheet at /01-market-research/by-product/<slug>/validation.md]
       ↓
[If validation passes: ROADMAP.md "Active Sprint" + /10-execution-sprints/current-sprint.md]
       ↓
[Sprint runs; product ships]
       ↓
[Idea's record is archived to /10-execution-sprints/completed-sprints/]
```
