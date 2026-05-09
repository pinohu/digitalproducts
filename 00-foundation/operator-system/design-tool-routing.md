# Design Tool Routing

This file defines the default design-production stack for Hermes, Paperclip, and any managed agents working across the `digitalproducts` business factory.

The goal is to reduce tool sprawl, keep outputs consistent, and route each design task to the strongest owned surface first.

## Core Design Production System

These tools are the default first-choice stack unless a project-specific constraint overrides them:

- `Pixelied`
- `RelayThat`
- `SUPERMACHINE`
- `Pixso`
- `Claritee`
- `Boardmix`
- `Brizy Cloud`
- `Microthemer`
- `ElementsKit`
- `Publitio`
- `FlexClip`
- `InVideo Studio`
- `Zebracat`
- `Decktopus`

## Default Routing

| Work type | Use first | Support / fallback | Primary outcome |
|---|---|---|---|
| Everyday graphic design | `Pixelied` | `ContentPresso`, Canva template packs | Social posts, hero graphics, thumbnails, lead magnets |
| Brand-consistent campaigns | `RelayThat` | `Pixelied`, `Baseline`, `BrandBay` | Repeatable campaign graphics with strong visual consistency |
| AI image generation and enhancement | `SUPERMACHINE` | `Phygital+`, `Booltool`, `Img.Upscaler`, `MagicFit` | Product visuals, mockups, cleanups, upscales |
| UI/UX design | `Pixso` | `Fignel`, `UXR Kit` | App screens, interface comps, clickable design references |
| Wireframes and planning | `Claritee` | `Boardmix`, `Poda` | Site maps, wireframes, feature structure, page planning |
| Brainstorming and flows | `Boardmix` | `Claritee`, `Poda` | User journeys, systems maps, launch boards, strategy diagrams |
| Landing pages and microsites | `Brizy Cloud` | `GroovePages`, `Lindo AI`, `TeleportHQ` | Fast page production for offers, funnels, and launch surfaces |
| WordPress visual polish | `Microthemer` + `ElementsKit` + `Stackable` | `Nexter`, `Exclusive Addons` | Layout refinement, sections, CSS control, conversion polish |
| Directory design | `Brilliant Directories` | `Directorist`, `CubeWP`, `Stackable`, `Microthemer` | Directory homepages, listings, member profiles, dashboards |
| Video assets | `FlexClip` | `InVideo Studio`, `Zebracat`, `Minvo`, `Fliki` | Shorts, promos, explainers, captions, social video |
| Media storage and delivery | `Publitio` | `Gumlet Video`, `Sinosend` | Hosted graphics, videos, and reusable launch assets |
| Interactive conversion assets | `Formaloo` | `GoZen Forms.Ai`, `Meiro`, `Claspo`, `Twidget.io` | Forms, quizzes, calculators, popups, intake flows |
| Presentations and decks | `Decktopus` | `Komodo Decks`, `Power-User`, `Boardmix` | Pitch decks, sales decks, reports, training slides |
| SOPs and walkthroughs | `Guidejar` | `Stepsy`, `ScreenRun`, `FlowShare Express`, `Cloudshot` | Tutorials, demos, onboarding guides, browser workflows |

## Business Factory Flow

For directory, SaaS, automation, and info-product businesses, route work through this sequence:

1. Plan the experience with `Claritee` + `Boardmix` + `Poda`.
2. Design the interface with `Pixso` + `Fignel` + `UXR Kit`.
3. Create brand assets with `Pixelied` + `RelayThat` + `Baseline` + `BrandBay`.
4. Generate visuals with `SUPERMACHINE` + `Phygital+` + `Booltool` + `Img.Upscaler`.
5. Build the page with `Brizy Cloud` + `GroovePages` + `Lindo AI` + `TeleportHQ`.
6. Polish WordPress surfaces with `Microthemer` + `ElementsKit` + `Stackable` + `Nexter`.
7. Create video assets with `FlexClip` + `InVideo Studio` + `Zebracat` + `Minvo` + `Fliki`.
8. Store and deliver assets through `Publitio` + `Gumlet Video`.
9. Add conversion elements with `Formaloo` + `GoZen Forms.Ai` + `Meiro` + `Claspo` + `Twidget.io`.

## Decision Rules

- Start with the named primary tool for the category before reaching for a general-purpose fallback.
- Prefer tool reuse over novelty. A slightly less flashy output from the core stack is better than fragmented production spread across too many apps.
- For landing pages, use `Brizy Cloud` first when speed matters and no existing coded surface must be preserved.
- For UI-heavy product work, keep planning in `Claritee` or `Boardmix` and interface design in `Pixso`; do not collapse both concerns into a page builder too early.
- For WordPress projects, treat `Microthemer`, `ElementsKit`, and `Stackable` as the default polish layer before adding more plugins.
- Use `Publitio` as the default hosted media library for reusable campaign and product assets.
- Reserve secondary tools for edge cases, account-access constraints, or capabilities the primary tool clearly lacks.

## Current First-Choice Priorities

If the system has to choose quickly without more context, use this short list first:

- `Pixelied`
- `RelayThat`
- `SUPERMACHINE`
- `Pixso`
- `Claritee`
- `Boardmix`
- `Brizy Cloud`
- `Microthemer`
- `ElementsKit`
- `Publitio`
- `FlexClip`
- `InVideo Studio`
- `Zebracat`
- `Decktopus`

Everything else remains available as specialist support, not the default starting point.
