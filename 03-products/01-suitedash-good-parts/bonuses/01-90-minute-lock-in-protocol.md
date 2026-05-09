# Bonus 1 — The 90-Minute SuiteDash Lock-In Protocol

A printable implementation checklist for turning the core PDF into one focused setup session.

## How to use this

Do not open SuiteDash and wander. Open this checklist, pick one workflow, and stop when the first client path is usable.

Recommended workflow for v1:

Client record → intake form → portal access → project template → file/document request → invoice/payment → status/update notification.

---

## Before you start: choose the workflow

- [ ] I picked one workflow to deploy first.
- [ ] I can describe the trigger in one sentence.
- [ ] I can describe the client-visible outcome in one sentence.
- [ ] I know who owns the workflow internally.
- [ ] I know what “done” means for the client.

If you cannot check these five boxes, do not configure features yet. Write the workflow first.

---

## Minute 0-10: Define the first workflow

Write one sentence for each:

- Trigger: `______________________________`
- Client next step: `______________________________`
- Internal next step: `______________________________`
- Evidence of completion: `______________________________`

Choose one workflow spine:

- [ ] Lead-to-client conversion.
- [ ] Paid client onboarding.
- [ ] Project/status visibility.
- [ ] Support/escalation intake.
- [ ] Other: `______________________________`

Recommended v1 spine: paid client onboarding + status visibility.

---

## Minute 10-20: Configure the client record

Minimum fields:

- [ ] Contact/company name standard chosen.
- [ ] Client status field exists.
- [ ] Owner/assignee field exists.
- [ ] Primary service/package field exists.
- [ ] Source or referral field exists.
- [ ] Next milestone / next step field exists.

Optional only if useful now:

- [ ] Budget authority.
- [ ] Implementation timeline.
- [ ] Primary pain point.
- [ ] Lead score.
- [ ] Payment status.

Stop rule: if a field will not change routing, status, reporting, or client experience, skip it for v1.

---

## Minute 20-35: Build the intake form

- [ ] Form has a clear name.
- [ ] Form captures the minimum data needed to begin work.
- [ ] Every required field maps to a contact/project decision.
- [ ] No “nice to know” questions added.
- [ ] Submission creates or updates the right client record.
- [ ] Submission notifies the internal owner.

Recommended v1 fields:

1. Name.
2. Email.
3. Company.
4. Service/package purchased.
5. Desired outcome.
6. Deadline or target launch date.
7. Files/assets needed.
8. Best contact method.
9. Anything blocking kickoff.

---

## Minute 35-50: Build the portal shell

- [ ] Logo/brand basics added.
- [ ] Client has one obvious home/start page.
- [ ] Portal explains what to do next.
- [ ] Files/documents are easy to find.
- [ ] Invoice/payment location is clear.
- [ ] Project/status area is visible if used.

Do not spend more than 15 minutes on design in v1. Your first portal needs clarity, not beauty.

---

## Minute 50-65: Build the project template

- [ ] Project template has 3-5 phases max.
- [ ] Each phase has owner, due date logic, and definition of done.
- [ ] Client-visible tasks are separated from internal tasks.
- [ ] File/request tasks have clear evidence requirements.
- [ ] QA/review task exists before delivery is marked complete.

Suggested phases:

1. Kickoff / access.
2. Intake / asset collection.
3. Setup / implementation.
4. Review / approval.
5. Delivery / follow-up.

---

## Minute 65-80: Add one automation

Pick one automation only.

Option A — Intake submitted:

- [ ] Create/update contact.
- [ ] Assign project template or task.
- [ ] Notify internal owner.
- [ ] Send client confirmation.

Option B — Invoice paid:

- [ ] Update client status.
- [ ] Send welcome/access email.
- [ ] Assign onboarding task/project.
- [ ] Notify owner.

Option C — Milestone changed:

- [ ] Update status.
- [ ] Notify client or internal owner.
- [ ] Create follow-up if blocked.

Stop rule: one working automation beats five half-configured automations.

---

## Minute 80-90: QA with a fake client

Run a test client through the flow.

- [ ] Contact/company record is created or updated correctly.
- [ ] Intake answers land where you expect.
- [ ] Portal access and next step are clear.
- [ ] Project template creates the right tasks.
- [ ] Notification/automation fires once, not zero or twice.
- [ ] Invoice/payment/file path is understandable.
- [ ] Internal owner knows what to do next.
- [ ] Client knows what to do next.

---

## Completion criteria

Your first SuiteDash deployment is “locked in” when:

- [ ] One client workflow can run from beginning to end.
- [ ] The client has one place to go for the next step.
- [ ] The internal owner has one source of truth.
- [ ] At least one repeated handoff is automated.
- [ ] Nothing outside the workflow was configured “just in case.”

## What to do next

If the workflow works, use it with one real client before expanding. If it breaks, fix the weakest handoff before adding features.