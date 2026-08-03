---
name: bitrix24-partner-style
description: >-
  The Bitrix24 PARTNER brand style (партнёрский фирменный стиль / фирстиль
  партнёров) — the official Bitrix24 Partners visual identity, as a content
  generator. Use it to design, lay out, build, or export any material in the
  Partner brand style: A4 PDF guides, brochures, one-pagers, sales playbooks and
  comparison sheets (portrait or landscape), LinkedIn square carousels/galleries
  (1080×1080), and Instagram Stories (1080×1920). Trigger whenever the user asks
  for the "partner brand style", "партнёрский фирстиль", "Bitrix24 Partners"
  materials, or any Bitrix24 partner marketing / sales creative — even if they
  don't name the design system explicitly. This is specifically the PARTNER
  identity; other Bitrix24 brand styles are separate skills, so don't use this
  one for non-partner (e.g. corporate Bitrix24) styling. Bundles the partner
  brand kit — Montserrat font, official Partner logos, colors, components, plus
  cutout-people photos and branded icons — so every output is consistent and
  print/social-ready.
---

# Bitrix24 Partner Brand Style

Build documents and social creatives in the Bitrix24 Partners visual language,
then render them to PDF (print) or PNG (social). Everything you need is bundled
in this skill — kit CSS, the component template, official logos, and the
Montserrat font — so output is fully self-contained and offline.

## Bundled assets (in `assets/`)
- **`DESIGN_SYSTEM.md`** — the full spec: colors, typography, components, logo
  rules, and format presets. **Read it before building** — it is the source of
  truth. Start with §3 (color), §5–5a (layout + formats), §6 (components),
  §9 (logo).
- **`bitrix24-kit.css`** — design tokens + every component class. Linked
  automatically by the render script.
- **`bitrix24-template.html`** — living styleguide. **Copy component blocks from
  here** and swap the text; don't hand-write components from scratch.
- **`bitrix24-logo/`**, **`Montserrat (1)/`** — official logos + brand font.
- **`bitrix24-images/`** — real brand imagery: `people/` (transparent cutout-people
  photos, clean names like `woman-laptop.png`, `man-asian-suit.png`) and `icons/`
  (branded product SVGs in navy + `-white` twins: `ai`, `crm`, `calendar`,
  `funnel`, `messenger`, `person`, `cart`). This is the curated set that ships
  with the skill; the full raw libraries live in the design-system source repo.

## Formats

| Want | Format flag | Canvas | `.page` class | Output |
|---|---|---|---|---|
| Guide / brochure / playbook | `a4` | 210×297 mm | `.page` | multi-page PDF |
| Wide handout / slide-style | `a4-land` | 297×210 mm | `.page--a4-land` | multi-page PDF |
| LinkedIn carousel / gallery | `li` | 1080×1080 | `.page--li` | one PNG per slide |
| Instagram Story | `story` | 1080×1920 | `.page--story` | one PNG per slide |

The palette classes still apply on top: `.page--sky` (Partners light) and
`.page--partner-navy` (deep navy for covers/CTA). Social presets carry a larger
type scale automatically.

## Workflow

1. **Read `assets/DESIGN_SYSTEM.md`** (at least §5a, §6, §9) and open
   `assets/bitrix24-template.html` for exact component markup.
2. **Pick the format** from the table above based on what the user is making.
3. **Author the HTML.** Write a normal HTML document whose body is a stack of
   `<section class="page …">` blocks — one per printed page or per social slide.
   You do **not** need to link the stylesheet or set `@page`; the render script
   injects the kit, the font/logo paths, and the correct page size for you.
   - **For social carousels, put one slide (`.page`) per HTML file** so each
     exports to its own cleanly-named PNG. (A4 docs stack all pages in one file.)
4. **Render** with `scripts/render.py` (see below), then **look at the output**
   and check it against the rules below. Fix and re-render until clean.

## Rendering

```bash
# A4 guide (portrait) -> guide.pdf
python3 scripts/render.py guide.html --format a4

# A4 landscape handout -> handout.pdf
python3 scripts/render.py handout.html --format a4-land

# LinkedIn square slide -> slide-01.png (2160×2160 at scale 2)
python3 scripts/render.py slide1.html --format li

# Instagram story -> story-01.png ; --scale 1 for exactly 1080×1920
python3 scripts/render.py story.html --format story --scale 2
```

Requires **Google Chrome/Chromium** (any recent version). PNG export also needs
**PyMuPDF** (`pip install pymupdf`) or **poppler** (`pdftoppm`) — the script
falls back automatically and tells you if something's missing.

**Cross-platform:** the script auto-detects Chrome on macOS, Linux and Windows.
On **Windows** run it with `python` (not `python3`) and use the Windows path to
the skill, e.g. `python "%USERPROFILE%\.claude\skills\bitrix24-partner-style\scripts\render.py" doc.html --format a4`.

## Authoring rules that keep it on-brand

Full detail is in `DESIGN_SYSTEM.md`; these are the ones that matter most.

- **Compose from tokens and components only.** No raw hex or off-scale px — reuse
  the kit's classes, colors (`--b24-*`), and spacing scale (`--b24-s*`). If
  something's missing, prefer an existing component over a one-off.
- **★ Use the signature partner gradient on every dark sheet.** The recognizable
  partner look is a **vivid azure glow fading to deep navy** — it comes free with
  `.page--partner-navy` (covers, section dividers, closing CTA) and with the navy
  tiles / table headers. Do **NOT** flat-fill a navy background or replace it with
  a subtle mono gradient — that is the #1 thing that makes partner materials look
  off-brand. Reach for `.page--partner-navy` (not a hand-set background) whenever
  you want a dark sheet, and the gradient is applied for you.
- **Partner logo = official lockup files only.** Use
  `<img class="b24-plogo b24-plogo--foot|--cover" src="bitrix24-logo/logo-partner-h.png">`
  (dark, for light pages) or `logo-partner-h-white.png` (for navy pages);
  stacked variants are `logo-partner-v[-white].png`. **Never** rebuild the logo
  from the wordmark + a separate "Partners" word — it mismatches the font.
- **Green `#BDF300` is accent/background only.** Never green text on white. Text
  on a green surface is deep partner-navy (the kit handles this automatically on
  `.page--sky` / `.page--partner-navy`). Highlight words with `.b24-hl` only on
  navy; on light pages emphasize with `<strong>` or a green pill.
- **CTA "Become a Partner"** is always a real link, centered, sized up:
  `<div class="b24-btn-center"><a class="b24-btn b24-btn--lg" href="https://partners.bitrix24.com/">Become a Partner <span class="b24-btn__arrow">→</span></a></div>`
- **Use real imagery where it adds life.** Prefer the bundled assets over emoji/placeholders:
  - **Cutout people** (`bitrix24-images/people/*.png`, transparent) on covers, heroes, closing
    pages — as a floating `<img class="b24-cutout b24-cutout--shadow" …>` (position with inline
    `height` + `right`/`bottom`, keep text in `.b24-content-z`), or as a `.b24-photo > img` band.
    Don't put one on every page; pick a person whose pose/prop fits the topic.
  - **Brand icons** (`bitrix24-images/icons/*.svg`) instead of emoji for Bitrix24 tools: white
    icon inside a navy `.b24-tile`, or navy icon inline via `.b24-ic`. Use the `-white.svg` twin on
    any navy surface, the plain (navy) file on light pages.
- **★ Never use ✅ / ❌ emoji, or emoji as checkmarks/numbers** — they instantly read as
  "AI-generated". Use the official badges (`bitrix24-images/icons/`, `-onnavy` twin on navy pages):
  - **Checklists / to-do / do-lists** → `.b24-checklist` with `.is-yes` / `.is-no`; the kit draws
    the `badge-check` / cross for you.
  - **Numbered steps or ranked cards** → the number badges `badge-1.svg` / `badge-2.svg` /
    `badge-3.svg` (signature-gradient circle), not a hand-made number square.
- **One `.b24-display` per document** (the cover/opening slide).
- **A4 pages are fixed-height with `overflow:hidden`** — content that overruns is
  clipped, not reflowed. Keep each page within one sheet; split into more pages
  rather than overpacking. Decorative tetris/stars bleeding off the edge is fine.
- **Instagram stories:** wrap slide content in `<div class="b24-safe">…</div>` so
  it clears the ~240px the app overlays top (avatar) and bottom (reply/CTA bar).

## Verifying the output

Rendering silently is not enough — **look at what you made**:
- Rasterize a PDF page (or open the PNG) and eyeball it. For A4, confirm no text
  is clipped at the page edge (fixed-height pages). For stories, confirm nothing
  important sits in the top/bottom ~240px.
- Check contrast (white on navy, deep-navy on green) and that the logo used the
  official lockup file, not a composite.
- One quick way to catch A4 clipping programmatically: in a browser, compare each
  `.page`'s `scrollHeight` to `clientHeight` — a positive delta means overflow
  (decoration bleeding off-edge is expected; body text overflow is not).

## Tip: PDF viewers and shadows
The kit's cards/tiles use soft CSS `box-shadow`. Some PDF viewers (macOS Preview /
Quick Look) rasterize a blurred shadow as a hard grey rectangle. If a document is
mainly going to be viewed there and the shadows look boxy, swap them for a hairline
border in the document's own `<style>`:
`.b24-card--white,.b24-table-wrap{box-shadow:none;border:1px solid var(--b24-line)}`.
