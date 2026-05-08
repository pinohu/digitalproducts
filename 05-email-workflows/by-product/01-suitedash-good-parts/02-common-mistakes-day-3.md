# Email 3 — Day 3: Common Mistakes

**Trigger:** 3 days after purchase
**Send time:** Same time of day as the welcome email

---

## Subject Line (Primary)

Stuck? Here's why.

## Subject Line (Alt 1)

The 3 walls most people hit on Day 3

## Subject Line (Alt 2)

If your automation isn't firing, read this

---

## Preheader

Most operators hit one of these three walls. None of them mean you're failing.

---

## Body

> Hey [first name],
>
> By now you've probably hit a wall somewhere. Most operators hit one of these three on Day 3:
>
> **Mistake #1: The form post-submit action isn't mapped.**
> Symptom: form submissions land in the submission table, but no contact gets created and no automation fires. Fix: `Forms > [your form] > Settings > Post-submit actions > Create or update contact`. Map every form field to its CRM custom field. The default is "no action" — most operators miss this and assume the form is broken.
>
> **Mistake #2: The automation has the right trigger but the wrong condition.**
> Symptom: automation runs, but the project doesn't spawn for some submissions. Fix: check that `service_tier` is *required* on the form. If it's optional and a submission skips it, the conditional logic falls through silently.
>
> **Mistake #3: Welcome email goes out with empty portal credentials.**
> Symptom: client receives the welcome email but the portal URL or login fields are blank. Fix: add a 30-second `Wait` action between the portal-provisioning step and the email-send step. SuiteDash merge tags evaluate at action-fire time, not flow-end time. The wait fixes the race condition.
>
> If you're hitting one of these, you're normal. If you're hitting none of these and breezing through, ignore this email.
>
> Either way — reply if you hit something I didn't cover. Genuinely want to know.
>
> — Ike

---

## Why This Works

- Pre-empts the three highest-frequency stuck-points (pulled from the PDF Chapter 5 "four mistakes" + recipe-level common failures)
- Normalizes friction = lowers self-blame, lowers refund risk
- Reply ask continues the feedback loop
- Concrete fixes = if buyer is stuck on one of these three, this email is worth $49 by itself
