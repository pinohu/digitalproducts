# Bonus 3 — The Skip-This List

*12 SuiteDash features to ignore. Standalone value: $97.*

Each entry: feature name, why it's tempting, why you should skip it, and what to use instead.

---

## 1. Estimates / Proposals Module

**Why it's tempting:** It's right there in your sidebar. You can build a proposal, email it, get an e-signature, and convert it into an invoice — all in one place.

**Why skip:** The proposal builder is brittle, the templates feel dated, and the e-signature flow has historically had reliability complaints. More importantly, proposals are a *brand surface* — they're how prospects experience your professionalism before they pay. SuiteDash's output looks like SuiteDash. Yours should look like you.

**Use instead:** PandaDoc, Better Proposals, Proposify, or a Google Doc with a HelloSign embed. If you already have a proposal flow that works, do not migrate it into SuiteDash.

---

## 2. Invoicing / Subscription Billing

**Why it's tempting:** You can connect Stripe and have SuiteDash handle invoicing, recurring billing, and dunning. One less subscription to manage.

**Why skip:** SuiteDash's billing layer is a thin wrapper over Stripe. The reporting, reconciliation, tax handling, and accountant-export flows are all worse than going to Stripe directly. If you ever switch off SuiteDash, your billing data is harder to extract.

**Use instead:** Stripe Billing or Stripe Invoicing directly. Connect to QuickBooks or Xero for accountant-friendly reporting. Use SuiteDash only for the *display* of invoices to clients (pull them in via Stripe webhook), not the source of truth.

---

## 3. Learning Management System (LMS)

**Why it's tempting:** "I could host my course inside the same platform my clients already log into. One login, one experience."

**Why skip:** SuiteDash's LMS is a worse Teachable. Drip scheduling is rudimentary, video hosting requires bringing your own (Vimeo, Wistia), and the student experience is utility-grade where Teachable/Thinkific/Kajabi are polished. Course buyers expect course-platform polish; SuiteDash will undermine your premium positioning.

**Use instead:** If you teach courses for revenue: Teachable, Thinkific, or Kajabi. If you don't teach courses, ignore this module forever.

---

## 4. Marketing Campaigns / Email Blasts

**Why it's tempting:** "I have a CRM, I have an email tool, why pay separately for ConvertKit?"

**Why skip:** SuiteDash's marketing email is built on shared sending infrastructure with no domain-warming, mediocre deliverability tracking, no advanced segmentation, and a 2017-era editor. Your open rates from SuiteDash will be 30–40% lower than from a real ESP. Marketing email is the wrong place to economize.

**Use instead:** ConvertKit, Beehiiv, MailerLite, or Brevo. Use SuiteDash automations only for transactional and portal-related emails (welcome, status updates, invoice notifications).

---

## 5. Appointment Scheduling / Booking

**Why it's tempting:** "Clients can book me from inside their portal, no Calendly redirect."

**Why skip:** Clients don't care that the calendar is in their portal. They care that booking is friction-free. Your existing Calendly link is a 1-click add-to-calendar. SuiteDash's booking flow is 3–4 clicks deeper because of the portal navigation. The "everything in one place" gain is theoretical; the friction is real.

**Use instead:** Calendly, Cal.com, or SavvyCal. Embed the booking link inside the client portal as a link if you want to keep them in-portal.

---

## 6. Affiliate Manager

**Why it's tempting:** Free affiliate program inside the platform you're already paying for.

**Why skip:** It tracks referrals, but the dashboard, reporting, and payout management are minimal. If you're seriously running an affiliate program (hundreds of affiliates, real reporting needs, real payout volume), you'll outgrow it within 3 months and have to migrate.

**Use instead:** Rewardful or FirstPromoter (cheapest), PartnerStack (most polished), or Stripe + a custom referral link tracker (cheapest at scale). Skip SuiteDash's version unless you've genuinely tested those alternatives and rejected them.

---

## 7. AI Assistant / AI Features

**Why it's tempting:** "Auto-generate task lists, auto-summarize messages — sounds great."

**Why skip:** Generic LLM wrappers, lagging the standalone tools (ChatGPT, Claude, Gemini) by 12+ months in capability and quality. The cost-of-quality-degradation if you build workflows on top of these features outweighs the convenience. You will be sad later.

**Use instead:** ChatGPT, Claude, or Gemini directly. Paste outputs into SuiteDash manually if you need them stored there.

---

## 8. White-Labeled Mobile App

**Why it's tempting:** Your own branded mobile app for clients. Sounds premium. Could justify a higher price point.

**Why skip:** It's a five-figure commitment in customization, certificate management, and ongoing maintenance — and almost no one in your $50K–$400K avatar revenue band needs it. Clients don't download apps for B2B service relationships; they bookmark URLs and check email. The mobile-app whitelabel solves a problem most operators don't have.

**Use instead:** Make sure your portal subdomain works well in mobile browsers. That's enough. Revisit the mobile-app question if and when you're at $1M+ revenue and selling enterprise.

---

## 9. Knowledge Base / FAQ Builder

**Why it's tempting:** "Centralize all my client docs in one place inside the portal."

**Why skip:** SuiteDash's KB is fine functionally, but it's invisible to Google (no SEO juice), inconvenient to share publicly, and locked behind portal access. A KB serves two audiences: clients (need it accessible) and prospects (need it indexable). SuiteDash's KB serves neither well.

**Use instead:** Notion (publish-as-site for public docs), GitBook for technical docs, or even a simple Google Doc index. Link to it from inside the portal if clients need it there too.

---

## 10. Internal Team Chat

**Why it's tempting:** "We could move team comms inside SuiteDash and reduce tool sprawl."

**Why skip:** Your team will not adopt it. They live in Slack, Teams, or Discord. Every time you try to push them into SuiteDash chat, the messages will be ignored or duplicated. This is a tool-adoption fight you cannot win and shouldn't try to win.

**Use instead:** Whatever your team already uses. Pipe SuiteDash events into that tool via webhook (e.g., "new client onboarded → Slack #wins channel"). One-way integration is better than two-way fragmentation.

---

## 11. Time Tracking

**Why it's tempting:** "Bill clients for hours tracked in the same tool where I manage their projects."

**Why skip:** SuiteDash's time tracker is functional but minimal — no integrations with accounting software, no idle detection, no reporting depth, no team-member time approval flows. If you genuinely bill hourly, the gap between SuiteDash's tracker and Harvest/Toggl is large and the missing reporting will cost you money in invoicing disputes.

**Use instead:** If you bill hourly: Harvest, Toggl, or Clockify (Harvest integrates cleanest with QuickBooks). If you bill flat-fee retainer: don't track time at all; track outcomes.

---

## 12. Custom Database / Secure Data Sharing

**Why it's tempting:** Build a custom record set, expose it to clients in their portal, control granular permissions. Sounds powerful.

**Why skip:** This is a power-user feature designed for a narrow case (custom internal tools where Airtable is too public and SuiteDash's standard modules don't fit). For 95% of operators, it's solving a problem they don't have. The configuration time is high and the maintenance burden is real — every schema change requires touching multiple permission grids.

**Use instead:** Airtable for internal data tools. Notion databases for shared knowledge. The standard SuiteDash modules (Contacts, Projects, Files) for everything client-facing. Revisit Custom Database only if you have a specific compliance or permissioning requirement those alternatives can't meet.

---

## The Pattern Across All 12

Every feature on this list shares one trait: **it competes with a purpose-built tool you probably already pay for**, and the configuration time to make it as good as the alternative exceeds what the alternative costs.

The skip is not "this feature is bad." The skip is "this feature is fine, but it's not where your leverage is at this stage."

Get the 7 modules that matter live first (per the main PDF and Bonus 1). Run a real client through them. Earn the right to add complexity by demonstrating you can extract value from simplicity.

Then, only then, revisit anything on this list.

— Ike
