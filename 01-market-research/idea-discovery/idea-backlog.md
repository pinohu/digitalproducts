# Idea Backlog

The running list of digital product candidates, ordered by total score (highest first). New ideas enter via mining sessions; ideas exit when they get promoted to a sprint, killed, or auto-archived after 90 days at <25.

## Backlog Status

| | Count |
|---|---|
| Active sprint candidates (40+) | 1 |
| Strong (30-39) | 0 |
| Backlog (25-29) | 0 |
| Weak (15-24) | 0 |
| Killed / archived | 0 |
| **Total scored ideas** | **1** |

_First mining pass pending. Run `python tools/reddit_miner.py` and complete a Reddit + AppSumo Q&A sweep to populate._

---

## Active Sprint Candidates (Score 40+)

_(highest-scoring ideas, ready for validation worksheet)_

| # | Idea | Score | Date Scored | Source | Notes |
|---|---|---|---|---|---|
| 1 | The Good Parts of SuiteDash | 41 | 2026-05-07 | DIG-3 validation + external proof sweep | Active sprint; validation passed, but named audience quotes and paid beta/pre-order signal still needed. |

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

## Idea 1 — The Good Parts of SuiteDash

**Date scored:** 2026-05-07
**Source:** DIG-3 validation; SuiteDash official site/pricing/features, AppSumo listing, Reddit r/appsumo/rCRM signal.
**Status:** Active sprint candidate / in Sprint 1

**Scoring (out of 50):**
- Massive Pain: 8/10 — Client portals, invoicing, automations, and onboarding are revenue-operation problems; misconfiguration costs operators time and client delivery confidence.
- Purchasing Power: 9/10 — Buyers already pay for SuiteDash subscriptions/LTDs and can expense a $49 deployment guide.
- Easy to Target: 8/10 — AppSumo, SuiteDash community, r/appsumo, r/CRM, YouTube reviews, and LinkedIn agency/ops niches are clear watering holes.
- Growing Market: 7/10 — Client-ops consolidation is durable and SuiteDash has active 2026 public pricing/AppSumo metadata, though exact search-volume data still needs the tooling pass.
- Personal Fit: 9/10 — Dynasty’s unfair advantage is configured infrastructure for technical operators, and the repo already positions SuiteDash as part of the stack.
- **Total: 41/50**

**One-sentence pitch:**
> *I help technically capable SuiteDash LTD/subscription owners deploy the 20% of SuiteDash that creates 80% of client-ops value without spending 40+ hours decoding every module, upgrade email, and configuration path.*

**Initial format guess:**
PDF + checklist + automation recipe/template pack + skip list.

**Initial price guess:**
$29 founding / $49 public.

**Watering holes:**
1. AppSumo SuiteDash listing/reviews — https://appsumo.com/products/suitedash/
2. r/appsumo SuiteDash LTD/access and upgrade threads.
3. r/CRM client portal / document collection / workflow automation threads.
4. SuiteDash community — https://community.suitedash.com
5. SuiteDash YouTube/tutorial ecosystem — https://www.youtube.com/@suitedash
6. LinkedIn agency owner, client-ops, and technical operator niches.

**Verbatim pain-point quotes:**
> *"Does anyone still use SuiteDash... I keep getting emails asking me to upgrade or exchange my LTD for a different plan... I can't tell if it's a money grab or a worthwhile product?"* — Reddit r/appsumo.
> *"I'm not a plus member with AppSumo but would like to purchase SuiteDash. Do you know where I can get it from — the lifetime deal?"* — Reddit r/appsumo.

**Decision:** Proceed to offer construction and Sprint 1 execution; require named audience proof and paid beta/pre-order signal before launch.

**Notes:**
Full validation worksheet: `/01-market-research/by-product/01-suitedash-good-parts/validation.md`.

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
