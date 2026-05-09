# Manual Actions Ledger

This is the complete list of work that still requires the operator rather than Hermes/Paperclip alone.

## How to send things back

- Non-secret URLs, labels, timestamps, product names, and approvals:
  - safe to place in repo docs, GitHub issues, or chat
- Secrets, API keys, OTPs, session cookies, and passwords:
  - do not put in Git, chat, screenshots, or shared docs
  - preferred path is `C:\Users\ohu00\Documents\.env` plus rerunning `.\ops\paperclip\enable-operator-mode.ps1 -EnableStrictMode`
- Browser-only access:
  - use a dedicated logged-in browser profile on the workstation
  - if MFA is required, complete it in the dedicated browser session
- Proof assets, testimonials, screenshots, PDFs, and launch media:
  - preferred path is the shared Google Drive project folder

## Launch-truth reconciliation

The manual-action ledger is the human/operator side of the launch gate. It should stay aligned with:

- `governance/release-state.json` for machine-readable blocked checks;
- `06-launch-playbooks/by-product/01-suitedash-good-parts-dig33-shipped-gate.md` for the DIG-33 ROADMAP DoD ledger;
- `ROADMAP.md` for the Shipped Catalog and product Definition of Done.

Current truth: repo deliverables and the Vercel staging page are ready for review, but production launch is not ready. The operator actions below are the external blockers that keep `releaseReadiness.*` false and keep DIG-33 blocked.

## Highest-priority launch actions

| Priority | Manual action | Why it matters | Where to source it | How to get it to me |
|---:|---|---|---|---|
| 1 | Pick the real SuiteDash tenant and provide browser/session access plus one matching `X-Public-ID` for an existing secure key | Biggest product-domain unlock; enables authenticated SuiteDash inspection | SuiteDash tenant admin, browser profile, Integrations/Secure API area | Put non-secret tenant label in repo/chat; keep Public ID and secret material in secure env/session path |
| 2 | Provide live Gumroad product URL and checkout URL | Converts staging offer into a real sellable flow | Gumroad dashboard | Safe to place in repo docs/chat |
| 3 | Provide 3 real testimonials or equivalent proof | Required for honest public launch | Customer emails, screenshots, docs, or approved case notes | Preferred in Google Drive or repo-safe sanitized markdown |
| 4 | Confirm domain/storefront linkage details for `ikeohu.com` and sitemap/storefront placement | Needed for real discoverability and post-launch truth | Domain/DNS, storefront plan, Vercel/Gumroad linkage notes | Safe to place in repo docs/chat |
| 5 | Confirm live post-purchase and abandoned-cart workflow target behavior | Needed before production launch can be called complete | Gumroad, Emailit, n8n, or related workflow design | Safe behavior notes in repo; keep live credentials in secure env |
| 6 | Record the real founding-window timestamp and public launch timing | Needed for launch copy, price logic, and proof | Your launch plan | Safe to place in repo docs/chat |

## AppSumo and operator-surface unblockers

| Priority | Tool | Manual action | Where to source it | How to get it to me |
|---:|---|---|---|---|
| 1 | KonnectzIT | Provide a valid browser session or confirmed login path | `https://app.konnectzit.com/` | Dedicated logged-in browser profile |
| 2 | Boost.space | Provide exact tenant base URL | Browser address bar after login or account settings | Safe in repo/chat |
| 3 | Flowlu | Provide exact workspace subdomain | Browser address bar after login or API settings | Safe in repo/chat |
| 4 | AgenticFlow | Provide correct workspace UUID and project UUID, or dedicated automation key | AgenticFlow app and API settings | Non-secret IDs safe in repo/chat; keys in secure env |
| 5 | WbizTool | Provide `WBIZTOOL_CLIENT_ID`; optionally `WBIZTOOL_WHATSAPP_CLIENT_ID` | WbizTool API and WhatsApp settings pages | Secure env for sensitive values; labels safe in docs |
| 6 | SMS-iT CRM | Provide working browser session or exact API base/auth/account context | SMS-iT dashboard and docs | Session in browser; non-secret base/context in docs |
| 7 | Procesio | Provide the API key name that pairs with the existing key value, plus workspace context if required | Procesio API settings | Non-secret key name/workspace safe in docs; values stay in secure env |
| 8 | CallScaler | Provide fresh working API key or browser session to API settings page | CallScaler v3 settings/API keys | Key via secure env; session via browser |
| 9 | Dadan | Provide one approved non-sensitive request code | Dadan admin/request area | Safe in secure doc or chat if non-sensitive |

## Automation-credential hardening actions

These are not required to continue read-only discovery, but they are required before scheduled or production automation should be enabled.

| Tool | Manual action | Where to source it | Delivery path |
|---|---|---|---|
| AITable | Provide a dedicated automation-owned key if scheduled checks will be enabled | AITable admin/API settings | Secure env |
| Agiled | Provide a dedicated automation-owned key before long-running schedules | Agiled API settings | Secure env |
| Emailit | Provide a dedicated automation-owned key | Emailit dashboard | Secure env |
| Certopus | Provide a dedicated automation-owned key | Certopus API settings | Secure env |
| Late/Zernio | Provide a dedicated automation-owned key | Zernio/Late API settings | Secure env |
| Formaloo | Provide dedicated automation key + secret | Formaloo API settings | Secure env |
| Flotiq | Provide dedicated automation token if scheduled CMS checks will be enabled | Flotiq API settings | Secure env |

## Governance and approval actions

| Manual action | Why | Delivery path |
|---|---|---|
| Approve any live write, send, spend, billing, or destructive workflow before activation | Keeps high-risk actions under explicit human authority | Chat/repo note for the approval plus secure runtime access if needed |
| Confirm whether the current release policy should block production on exactly 3 testimonials or a different proof threshold | Prevents governance from guessing your public standard | Safe in repo/chat |
| Decide whether the preview site should remain `noindex` until Gumroad and proof are live | Avoids accidental public launch drift | Safe in repo/chat |
