#!/usr/bin/env python3
"""Export Gumroad-ready SuiteDash v1 PDFs and lightweight launch assets."""
from __future__ import annotations

import html
import re
import textwrap
import zipfile
from pathlib import Path

import markdown
from PIL import Image, ImageDraw, ImageFont
from weasyprint import HTML

ROOT = Path(__file__).resolve().parents[1]
PRODUCT = ROOT / "03-products" / "01-suitedash-good-parts"
DELIVERABLES = PRODUCT / "deliverables"
ASSETS = PRODUCT / "assets"
MANUSCRIPT = PRODUCT / "manuscript" / "02-v1-manuscript.md"
BONUSES = PRODUCT / "bonuses"

EXPORTS = [
    (MANUSCRIPT, "The-Good-Parts-of-SuiteDash.pdf", "The Good Parts of SuiteDash", "The 90-minute operator path through the 20% of SuiteDash that creates 80% of the client-ops value.", "Core Guide"),
    (BONUSES / "01-90-minute-lock-in-protocol.md", "90-Minute-SuiteDash-Lock-In-Protocol.pdf", "90-Minute SuiteDash Lock-In Protocol", "A printable implementation checklist for one focused setup session.", "Bonus 1"),
    (BONUSES / "02-automation-recipes.md", "7-SuiteDash-Automation-Recipes.pdf", "7 SuiteDash Automation Recipes", "Production-minded automation patterns; not verified import files.", "Bonus 2"),
    (BONUSES / "03-kill-list.md", "SuiteDash-Kill-List.pdf", "SuiteDash Kill List", "12 SuiteDash features to ignore until later.", "Bonus 3"),
]

CSS = """
@page {
  size: Letter;
  margin: 0.65in;
  @bottom-right { content: counter(page); color: #64748b; font-size: 9px; }
}
@page:first { margin: 0; @bottom-right { content: ""; } }
body { font-family: Inter, Arial, sans-serif; color: #0f172a; font-size: 10.8pt; line-height: 1.48; }
.cover { page-break-after: always; min-height: 10.9in; padding: 0.75in; box-sizing: border-box; background: linear-gradient(135deg, #020617 0%, #0f172a 55%, #064e3b 100%); color: #f8fafc; position: relative; overflow: hidden; }
.cover:before { content: ""; position: absolute; inset: 0; background-image: linear-gradient(rgba(148,163,184,.11) 1px, transparent 1px), linear-gradient(90deg, rgba(148,163,184,.11) 1px, transparent 1px); background-size: 42px 42px; }
.cover-inner { position: relative; z-index: 1; height: 9.3in; border: 1px solid rgba(34,211,238,.45); border-radius: 18px; padding: 0.48in; }
.badge { display: inline-block; border: 1px solid #22d3ee; color: #67e8f9; border-radius: 999px; padding: 7px 12px; font-size: 10px; letter-spacing: .14em; text-transform: uppercase; }
h1.cover-title { margin: 1.05in 0 0.2in; max-width: 6.6in; font-size: 44px; line-height: 0.98; color: white; letter-spacing: -0.04em; }
.cover-subtitle { max-width: 5.9in; font-size: 17px; line-height: 1.35; color: #cbd5e1; }
.route { position: absolute; left: .48in; right: .48in; bottom: .75in; display: grid; grid-template-columns: repeat(7, 1fr); gap: 8px; }
.tile { min-height: 54px; border: 1px solid rgba(52,211,153,.75); border-radius: 10px; background: rgba(6,78,59,.34); color: #d1fae5; display: flex; align-items: center; justify-content: center; text-align: center; font-size: 10px; font-weight: 700; }
.skipline { position: absolute; right: .62in; top: 1.1in; color: rgba(251,191,36,.75); font-size: 12px; }
h1 { color: #0f172a; font-size: 25px; line-height: 1.12; margin: 0 0 14px; page-break-after: avoid; }
h2 { color: #075985; margin: 28px 0 10px; padding-bottom: 4px; border-bottom: 1px solid #bae6fd; page-break-after: avoid; }
h3 { color: #0f766e; margin: 18px 0 8px; page-break-after: avoid; }
p, li { orphans: 3; widows: 3; }
ul, ol { padding-left: 22px; }
blockquote { border-left: 4px solid #22d3ee; margin: 16px 0; padding: 8px 14px; background: #f0f9ff; color: #0f172a; }
code { background: #f1f5f9; padding: 1px 4px; border-radius: 4px; font-family: ui-monospace, SFMono-Regular, Menlo, monospace; font-size: 90%; }
hr { border: 0; border-top: 1px solid #cbd5e1; margin: 22px 0; }
table { width: 100%; border-collapse: collapse; margin: 14px 0; font-size: 9.5pt; }
th { background: #e0f2fe; text-align: left; }
th, td { border: 1px solid #cbd5e1; padding: 6px 7px; vertical-align: top; }
.footer-note { margin-top: 34px; padding: 12px 14px; background: #f8fafc; border: 1px solid #cbd5e1; border-radius: 8px; font-size: 9.5pt; color: #475569; }
"""

def md_to_html(path: Path, title: str, subtitle: str, badge: str) -> str:
    source = path.read_text(encoding="utf-8")
    body = markdown.markdown(source, extensions=["extra", "sane_lists", "tables"])
    cover_tiles = "".join(f'<div class="tile">{label}</div>' for label in ["CRM", "Intake", "Portal", "Projects", "Files", "Billing", "Automation"])
    return f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<title>{html.escape(title)}</title>
<style>{CSS}</style>
</head>
<body>
<section class="cover">
  <div class="cover-inner">
    <div class="badge">{html.escape(badge)} • Operator Cut</div>
    <div class="skipline">Skip the feature maze. Ship one useful workflow.</div>
    <h1 class="cover-title">{html.escape(title)}</h1>
    <div class="cover-subtitle">{html.escape(subtitle)}</div>
    <div class="route">{cover_tiles}</div>
  </div>
</section>
<main>{body}</main>
<div class="footer-note">Version: v1 operator edition. SuiteDash is referenced as the product subject; this package is not official SuiteDash documentation or a replacement for SuiteDash support.</div>
</body>
</html>"""

def export_pdf(src: Path, filename: str, title: str, subtitle: str, badge: str) -> None:
    out = DELIVERABLES / filename
    HTML(string=md_to_html(src, title, subtitle, badge), base_url=str(src.parent)).write_pdf(out)
    print(f"wrote {out.relative_to(ROOT)}")

def font(size: int, bold: bool = False) -> ImageFont.FreeTypeFont | ImageFont.ImageFont:
    candidates = [
        "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf" if bold else "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf",
        "/usr/share/fonts/truetype/liberation2/LiberationSans-Bold.ttf" if bold else "/usr/share/fonts/truetype/liberation2/LiberationSans-Regular.ttf",
    ]
    for c in candidates:
        try:
            return ImageFont.truetype(c, size)
        except OSError:
            pass
    return ImageFont.load_default()

def wrapped(draw: ImageDraw.ImageDraw, text: str, xy: tuple[int, int], width: int, fnt, fill: str, spacing: int = 8) -> int:
    words = text.split()
    lines = []
    line = ""
    for word in words:
        test = (line + " " + word).strip()
        if draw.textbbox((0, 0), test, font=fnt)[2] <= width:
            line = test
        else:
            lines.append(line)
            line = word
    if line:
        lines.append(line)
    x, y = xy
    for line in lines:
        draw.text((x, y), line, font=fnt, fill=fill)
        y += draw.textbbox((0, 0), line, font=fnt)[3] + spacing
    return y

def make_asset(size: tuple[int, int], filename: str, variant: str) -> None:
    w, h = size
    img = Image.new("RGB", size, "#020617")
    d = ImageDraw.Draw(img)
    for x in range(0, w, 48):
        d.line([(x, 0), (x, h)], fill="#102033", width=1)
    for y in range(0, h, 48):
        d.line([(0, y), (w, y)], fill="#102033", width=1)
    # route background
    d.rounded_rectangle((int(w*.06), int(h*.10), int(w*.94), int(h*.90)), radius=28, outline="#22d3ee", width=3, fill="#07111f")
    d.text((int(w*.10), int(h*.16)), "OPERATOR CUT", font=font(max(16, w//58), True), fill="#67e8f9")
    title = "The Good Parts of SuiteDash"
    subtitle = "Stop wandering through SuiteDash. Configure the good parts first."
    if variant == "cover":
        title_size, sub_size = 86, 38
        y = int(h*.28)
        y = wrapped(d, title, (int(w*.10), y), int(w*.70), font(title_size, True), "#f8fafc", 12)
        wrapped(d, "The 90-minute operator path through the 20% that creates 80% of the client-ops value.", (int(w*.10), y+24), int(w*.72), font(sub_size), "#cbd5e1", 10)
    else:
        title_size, sub_size = max(44, w//17), max(22, w//40)
        y = int(h*.26)
        y = wrapped(d, title, (int(w*.10), y), int(w*.63), font(title_size, True), "#f8fafc", 8)
        wrapped(d, subtitle, (int(w*.10), y+16), int(w*.58), font(sub_size), "#cbd5e1", 6)
    labels = ["CRM", "Intake", "Portal", "Projects", "Files", "Billing", "Automation"]
    tile_w = int(w*.11)
    tile_h = int(h*.09)
    start_x = int(w*.10)
    y_tile = int(h*.72)
    gap = int(w*.012)
    for idx, label in enumerate(labels):
        x = start_x + idx * (tile_w + gap)
        d.rounded_rectangle((x, y_tile, x+tile_w, y_tile+tile_h), radius=12, outline="#34d399", width=2, fill="#064e3b")
        bbox = d.textbbox((0,0), label, font=font(max(14, w//70), True))
        d.text((x + (tile_w-(bbox[2]-bbox[0]))//2, y_tile + (tile_h-(bbox[3]-bbox[1]))//2), label, font=font(max(14, w//70), True), fill="#d1fae5")
        if idx < len(labels)-1:
            d.line((x+tile_w, y_tile+tile_h//2, x+tile_w+gap, y_tile+tile_h//2), fill="#22d3ee", width=3)
    d.text((int(w*.10), int(h*.86)), "PDF + 3 bonuses • Founding $29 / Public $49", font=font(max(18, w//55), True), fill="#fbbf24")
    img.save(DELIVERABLES / filename, quality=95)
    print(f"wrote {(DELIVERABLES / filename).relative_to(ROOT)}")

def make_svg() -> None:
    svg = """<svg xmlns="http://www.w3.org/2000/svg" width="1280" height="720" viewBox="0 0 1280 720">
<defs><pattern id="grid" width="48" height="48" patternUnits="userSpaceOnUse"><path d="M48 0H0V48" fill="none" stroke="#102033" stroke-width="1"/></pattern></defs>
<rect width="1280" height="720" fill="#020617"/><rect width="1280" height="720" fill="url(#grid)"/>
<rect x="70" y="70" width="1140" height="580" rx="28" fill="#07111f" stroke="#22d3ee" stroke-width="3"/>
<text x="130" y="145" font-family="DejaVu Sans, Arial" font-size="25" font-weight="700" fill="#67e8f9" letter-spacing="4">OPERATOR CUT</text>
<text x="130" y="265" font-family="DejaVu Sans, Arial" font-size="72" font-weight="700" fill="#f8fafc">The Good Parts</text>
<text x="130" y="345" font-family="DejaVu Sans, Arial" font-size="72" font-weight="700" fill="#f8fafc">of SuiteDash</text>
<text x="130" y="405" font-family="DejaVu Sans, Arial" font-size="30" fill="#cbd5e1">Configure the 20% that creates 80% of client-ops value.</text>
<g font-family="DejaVu Sans, Arial" font-size="19" font-weight="700" fill="#d1fae5" text-anchor="middle">
"""
    labels = ["CRM", "Intake", "Portal", "Projects", "Files", "Billing", "Automation"]
    x = 130
    for idx, label in enumerate(labels):
        svg += f'<rect x="{x}" y="510" width="130" height="68" rx="12" fill="#064e3b" stroke="#34d399" stroke-width="2"/><text x="{x+65}" y="552">{label}</text>'
        if idx < len(labels)-1:
            svg += f'<path d="M{x+130} 544H{x+146}" stroke="#22d3ee" stroke-width="4"/>'
        x += 146
    svg += """</g><text x="130" y="620" font-family="DejaVu Sans, Arial" font-size="24" font-weight="700" fill="#fbbf24">PDF + 3 bonuses • Founding $29 / Public $49</text></svg>"""
    (ASSETS / "suitedash-good-parts-hero.svg").write_text(svg, encoding="utf-8")
    print(f"wrote {(ASSETS / 'suitedash-good-parts-hero.svg').relative_to(ROOT)}")

def make_zips() -> None:
    bonus_zip = DELIVERABLES / "The-Good-Parts-of-SuiteDash-Bonus-Pack.zip"
    with zipfile.ZipFile(bonus_zip, "w", compression=zipfile.ZIP_DEFLATED) as z:
        for name in ["90-Minute-SuiteDash-Lock-In-Protocol.pdf", "7-SuiteDash-Automation-Recipes.pdf", "SuiteDash-Kill-List.pdf", "START-HERE.md"]:
            z.write(DELIVERABLES / name, arcname=name)
    print(f"wrote {bonus_zip.relative_to(ROOT)}")

    full_zip = DELIVERABLES / "The-Good-Parts-of-SuiteDash-Gumroad-Package.zip"
    with zipfile.ZipFile(full_zip, "w", compression=zipfile.ZIP_DEFLATED) as z:
        for name in [
            "The-Good-Parts-of-SuiteDash.pdf",
            "90-Minute-SuiteDash-Lock-In-Protocol.pdf",
            "7-SuiteDash-Automation-Recipes.pdf",
            "SuiteDash-Kill-List.pdf",
            "START-HERE.md",
            "suitedash-good-parts-gumroad-hero.png",
            "suitedash-good-parts-social-card.png",
            "suitedash-good-parts-cover.png",
            "suitedash-good-parts-square-thumbnail.png",
        ]:
            z.write(DELIVERABLES / name, arcname=name)
    print(f"wrote {full_zip.relative_to(ROOT)}")

def main() -> None:
    DELIVERABLES.mkdir(parents=True, exist_ok=True)
    ASSETS.mkdir(parents=True, exist_ok=True)
    for args in EXPORTS:
        export_pdf(*args)
    make_asset((1280, 720), "suitedash-good-parts-gumroad-hero.png", "hero")
    make_asset((1200, 630), "suitedash-good-parts-social-card.png", "social")
    make_asset((1600, 2400), "suitedash-good-parts-cover.png", "cover")
    make_asset((1080, 1080), "suitedash-good-parts-square-thumbnail.png", "social")
    make_svg()
    make_zips()

if __name__ == "__main__":
    main()
