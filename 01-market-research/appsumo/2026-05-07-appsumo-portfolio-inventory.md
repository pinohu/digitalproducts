# AppSumo Portfolio Inventory

Snapshot date: 2026-05-07

## Primary sources

- Workbook: `C:\Users\ohu00\Downloads\appsumo_business_factory_os_map.xlsx`
- CSV export: `C:\Users\ohu00\Downloads\tigertail-product-list-07-05-2026.csv`
- Google Drive doc: `Comprehensive Analysis of AppSumo-Acquired Applications`
- Google Drive doc: `AppSumo Software Research Project - Todo List.md`
- Google Drive file: `real_software_list (2).txt`

## Current inventory snapshot

- Total CSV rows: 832
- Unique product names in current export: 309
- Rows marked `activated`: 160
- Rows marked `redeemed`: 544
- Rows marked `expired`: 128
- Products with at least one `activated` row: 137
- Products with at least one `redeemed` row: 91
- Products with only `expired` rows: 104

Note: this export does not expose a separate `unredeemed` status. It uses `activated`, `redeemed`, and `expired`.

## Existing Drive research corpus

Drive already contains a substantial AppSumo research base. The most useful items found so far are:

- `Comprehensive Analysis of AppSumo-Acquired Applications`
- `AppSumo Software Research Project - Todo List.md`
- Product-specific reports such as:
  - `Activepieces Research Report.md`
  - `Afforai (now Logically.app) Research Report.md`
  - `AffSync Research Report.md`
  - `albato_research.md`
  - `pixso_research.md`
  - multiple SuiteDash planning and implementation docs

The older Drive research project tracked 277 apps. The current 2026 export is larger and includes newer products, renamed products, and "Plus exclusive" variants.

## Web-enriched newer or newly relevant tools

These tools appear newer than the older Drive list or worth refreshing from current web sources:

- `Emailit`: developer- and marketer-focused email platform with sending APIs and SDKs. Source: `https://emailit.com/`
- `Lunacal`: branded scheduling and booking platform with calendar sync, payments, reminders, round-robin scheduling, and webhooks. Sources: `https://lunacal.ai/`, `https://help.lunacal.ai/`, `https://appsumo.com/products/lunacal`
- `MagicFit`: AI creative tool that turns product images or URLs into ads, videos, hooks, and social posts; integrates with Shopify. Source: `https://appsumo.com/products/magicfit/`
- `SMS-iT CRM`: AI-heavy CRM and ERP platform with omnichannel messaging, automation, and built-in agentic features. Sources: `https://www.smsit.ai/`, `https://appsumo.com/products/sms-it-crm/`
- `Switchboard Canvas`: image generation and templated visual automation platform with API and no-code workflows. Source: `https://www.switchboard.ai/`
- `NoCode-X`: secure no-code full-stack platform with integrated database, backend logic, auth, file storage, AI assistance, and docs. Sources: `https://www.nocode-x.com/nocode-platform/`, `https://docs.nocode-x.com/nocode-x-platform/`
- `WbizTool`: WhatsApp business automation platform with API, Excel integration, reminders, number verification, and group management. Sources: `https://wbiztool.com/`, `https://wbiztool.com/docs/`
- `Phygital+`: creative AI workspace bundling 30+ tools for image, video, and 3D generation in one collaborative canvas. Sources: `https://appsumo.com/products/phygital/`, `https://phygital.plus/`
- `Swft Connect`: digital business card and lead capture platform built around Apple Wallet and Google Wallet. Source: `https://swftconnect.com/`
- `Vocable AI`: AI content planner for generating 30-day multichannel content plans and editing output for blogs and socials. Source: `https://appsumo.com/products/vocable-ai/`
- `Late`: unified social posting and scheduling product with API-based multi-platform publishing. Sources: `https://appsumo.com/products/m/late/`, `https://getlate.dev/`
- `Dadan`: Loom-style screen/video recording, editing, and hosting platform. Source: `https://www.dadan.io/`
- `Nexter`: all-in-one WordPress toolkit with 90+ blocks, 50+ extensions, and 1,000+ templates. Source: `https://appsumo.com/products/nexter/`
- `Playzo`: gamified marketing and course engagement platform. Sources: `https://appsumo.com/products/m/playzo/`, `https://web.playzo.io/`
- `ResumeUp.AI`: AI resume builder and ATS optimization platform. Sources: `https://resumeup.ai/`, `https://appsumo.com/products/resumeupai/`

## Names that need manual validation

Some product names are generic, truncated, or variant-heavy, so exact mapping should be validated before building workflows around them:

- `Blue`
- `Late`
- `Tabby`
- `gini`
- `Power`
- `NoCode-X` vs older `NoCode`
- `Spoken (formerly Rumble Studio)`
- `CallScaler - Call Tracking Software` vs older `CallScaler`

## Highest-value tools for the current operating stack

For Hermes, Paperclip, and the `digitalproducts` production push, the strongest portfolio candidates appear to be:

- `Activepieces`
- `AgenticFlow`
- `Albato`
- `AITable.ai`
- `SuiteDash`
- `TaskMagic`
- `Lunacal`
- `Late`
- `SMS-iT CRM`
- `Swft Connect`
- `WbizTool`
- `Vocable AI`
- `Phygital+`
- `Switchboard Canvas`
- `Nexter`

## Practical next step

Convert this portfolio into a structured operating sheet with:

- product name
- status
- category
- API availability
- automation readiness
- business model fit
- current project fit
- source doc link
- external doc link

That would let Hermes and Paperclip route work toward the tools with the highest ROI instead of treating the AppSumo collection as a flat list.

Follow-on operator plan:

- `01-market-research/appsumo/2026-05-08-priority-access-plan.md` turns the inventory into a concrete access-verification sequence for the Browser Operations Lead, using secure credential sources plus the existing `.env` API vault without copying raw secrets into the repo.
- `01-market-research/appsumo/2026-05-08-appsumo-business-factory-map.md` turns the non-design stack into category routing, engine grouping, and operating-system priorities for Hermes and Paperclip.

Workbook-derived headline insight:

- The portfolio is most concentrated in `Client Portal & Service Delivery OS`, `Content Repurposing & Media OS`, `Micro-SaaS Launch OS`, `Sales Outreach & Campaign OS`, and `Authority Site & Affiliate OS`, which makes the stack especially strong for service businesses, directories, content businesses, and SaaS-like offers with automation behind them.
