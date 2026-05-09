# Vercel Ops

Helpers for deploying isolated Vercel surfaces from this repo.

## Current helper

- `deploy-suitedash-preview.ps1` - redeploys the SuiteDash staging page from `08-platforms/vercel-sites/suitedash-good-parts-preview`

## Usage

```powershell
cd "C:\Users\ohu00\Desktop\digitalproducts"
.\ops\vercel\deploy-suitedash-preview.ps1
```

Optional production promotion:

```powershell
.\ops\vercel\deploy-suitedash-preview.ps1 -Prod
```

Behavior note:

- default runs create a Vercel preview deployment, which may require Vercel authentication for direct browser access
- `-Prod` is the deliberate public-alias promotion path once the page is ready to be the canonical public surface

The helper expects:

- `tools/.env` to contain `VERCEL_TOKEN`
- the preview folder to already be linked locally to the intended Vercel project via `.vercel/project.json`
