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
- **`industry-guide-template.html`** — living reference for the **Industry Guide**
  direction (the `guide` format): a full 5-page vertical guide (cover → pain→tools→
  outcome pages → key-value close). Copy from here when building an industry guide.
- **`success-story-pdf-template.html` / `success-story-posts-template.html`** (Askarasoft) + **`success-story-pdf-template-reyada.html`** (Reyada — extended §15.x layouts: fact-pills, certificate card, check-pill band, emblem) + **`success-story-pdf-template-hugo.html`** (Bit24 / Hugo — §15.x5 text patterns, navy-disc cut-out avatar, hero cover) —
  living references for the **Success Story** direction: a partner testimonial
  shipped as BOTH a multi-page A4 **PDF** and a series of 1080×1350 **LinkedIn
  JPEG posts** from the same narrative. Filled with the Askarasoft example; copy
  a page/post and swap the text. Blank starters: `success-story-pdf-skeleton.html`
  and `success-story-posts-skeleton.html`. See §"Success Story" below.
- **`LOCALIZATION.md`** — how to ship a guide per market: the tool-link glossary
  (EN/ES/PL) and the domain-swap URL rule. Read it whenever links or localization
  are involved.
- **`PEOPLE.md`** — the **industry-people** feature: how to swap the cover/closing
  figures to match a guide's industry (attire, always holding a device) — pick from
  the library or generate a transparent cutout. Read it whenever building a guide.
- **`ICONS.md`** — the **icon base for all PDFs**: the full catalog of the official
  Bitrix24 icon library (every icon + meaning + Figma node id) and the rule — default
  **Solid**, Outline Bold only on request, **one style per file**, pick by **meaning**,
  recolour per the design system. **Fetch on demand:** per document, look up only the
  few icons it needs, export just those node ids from Figma (check the
  `icons-solid/` cache first), and prep with `scripts/prep_icon.py` — never bulk-download.
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
| **Industry Guide** (vertical) | `guide` | 1080×1350 | `.page--guide` | **multi-page PDF** |
| **Success Stories / История успеха** — PDF | `a4` | 210×297 mm | `.page` + `.b24-ss-*` | multi-page PDF |
| **Success Story** — posts | `post` | 1080×1350 | `.page--post` | one **JPEG** per post |
| LinkedIn carousel / gallery | `li` | 1080×1080 | `.page--li` | one PNG per slide |
| Instagram Story | `story` | 1080×1920 | `.page--story` | one PNG per slide |

The palette classes still apply on top: `.page--sky` (Partners light) and
`.page--partner-navy` (deep navy for covers/CTA). Social presets carry a larger
type scale automatically.

### Industry Guide (the `guide` format)
A **1080×1350 vertical, multi-page PDF** — Bitrix24's per-industry quick guides
(Construction, Digital Marketing, …). Unlike the social presets, all
`.page--guide` sheets stack into **one PDF**. **Bitrix24 corporate** format with
a **locked palette**: background `#F5FAFF`; all dark surfaces (icon tiles, cover
person/title plates, closing band, headings) share one gradient `var(--b24-ig-navy)`;
large content cards are `#01447B` at alternating 4 %/10 %; body text `#002153` @ 80 %.
Mono-ink `logo-ink.svg` (`#012254`) + green "Quick Guide" pill; headings are Bold
(700); **do not** add `.page--sky` / `.page--partner-navy`. The cover person floats
**on top** of its plate (not clipped, head at the logo line); the closing page does
the same. **Match the cover/closing people to the guide's industry** (attire + a
device) — see `PEOPLE.md`. To stress part of a phrase, use bold same-size green/white
(`.b24-em--green` / `.b24-em--white`), never a coloured underline. Content pages end
in a **centered logo** (no line, no "Page N") except first and last. Structure,
components and localization are in
`industry-guide-template.html`, `DESIGN_SYSTEM.md §5b`, and `LOCALIZATION.md`.
Its signature page is the **pain → Bitrix24 Tools → Practical Outcome** card,
where every tool is a **real, localizable link** (see below).

### Success Stories · «История успеха» (PDF) — one common template

**Registered template — “Success Stories” / «История успеха ПДФ».** It is a SINGLE common A4 PDF template, filled per partner. `success-story-pdf-template.html` (Askarasoft), `success-story-pdf-template-reyada.html` (Reyada) and `success-story-pdf-template-hugo.html` (Bit24 / Hugo Miranda) are **interchangeable examples of the same template** — identical `.page` + `.b24-ss-*` system; only the partner’s copy, photos and blocks change. Start a new story by copying either example and swapping the content. Every cover carries the **“Success Stories”** eyebrow plaque.

A **partner testimonial** produced as **two deliverables from one narrative** — a
multi-page **PDF** and a series of **LinkedIn JPEG posts**. **Living references:**
`success-story-pdf-template.html` / `success-story-pdf-template-reyada.html` / `success-story-pdf-template-hugo.html` (A4, `--format a4`), the text-pattern demo `success-story-pdf-patterns-demo.html`, and
`success-story-posts-template.html` (1080×1350 posts, `--format post`); blank
starters `success-story-*-skeleton.html`. Full spec: `DESIGN_SYSTEM.md §5c`.

**★ PDF vs LinkedIn — two media, not one file resized.** The **PDF** is one
multi-page, downloadable/printable document: denser (several Q&A per page), a
partner runhead + page number on every sheet, and a **real clickable** "Sign up"
link on the CTA. The **posts** are a **series of separate JPEGs**, **one idea per
slide**, bigger type, the speaker facts on the cover, and a CTA that says **"use
the link in the description"** — a social post has no clickable button. Author two
HTML files; they share every `.b24-ss-*` component. **One `.page--post` per post**
(the render script writes one JPEG per page).

**★ Cover photo workflow.** The partner sends a **raw photo (with background,
unprocessed)** in the task — you process it, you don't paste it in. Run
the photo is placed over the navy gradient with **`mix-blend-mode: overlay`** —
the brand-navy tone comes from the BLEND, not from recolouring the image (exactly
like Figma). `scripts/prep_cover_photo.py PHOTO.jpg --name <slug>` just removes the
background (a clean cutout blends best; `--keep-bg` to keep it) and cuts an avatar; then place
`<img class="b24-ss-photo …">` and **choose the framing that suits that photo** —
`--right` / `--top` / `--bottom` / `--wide`. The **cover person should be LARGE and prominent** — the hero of the page. Size the cutout so it runs close to the full page height (e.g. widen `.b24-ss-photo--right` to ~80%+), the face high and clearly visible, body bleeding off the bottom/right; the title sits over the lower body in white. Don't leave the person small in a corner. The cover's edge-fade blends it into
the signature azure→navy gradient. Match the layout to the photo; don't force it. The photo is the **person from the brief (ТЗ)** — use the SAME person on the **cover** and in the **round avatar** of the speaker card; an extra placement is a **city/buildings image with the person laid on top** (the page-7 band) when the brief provides such a shot.

**★ Uploaded partner photos → remove background → use in the PDF.** Every photo the partner uploads is **background-removed first**, then used as a transparent cutout — never placed with its original backdrop. Run `python3 scripts/prep_cover_photo.py PHOTO.jpg --name <slug>` (cutout via `rembg` u2net; install once: `pip install "rembg[cpu]" onnxruntime`). The cutout is then reused across the story: the **cover** person (dropped over the navy gradient — the `mix-blend-mode: overlay` tints it into the brand navy), the **round speaker avatar on page 3** — which is **not** a plain cropped photo dropped on a coloured circle. Build it as a **dark brand-navy disc** (azure core → deep navy edge radial, the brand gradient) with the person's **background-removed head-and-shoulders cut-out composited on top**, so the face reads as literally cut out and sitting on the navy brand backdrop. Frame it with the **whole face visible and a little headroom** — anchor the top of the head a few percent below the disc's top so the crown is **never clipped**; the shoulders may run off the bottom. Verify on the rendered page 3 that the face isn't cut at the top. `prep_cover_photo.py` gives the cutout; compose it onto the navy disc rather than masking a rectangular photo. And, when supplied, the **person on the page-7 city band**. Use `--keep-bg` only when the backdrop is meant to stay.

**★ Check every page for clipped text.** After rendering, look at each A4 page: no text may be cut off at the bottom edge. If a column overflows, move the overflowing block into the SECOND column and rebalance the spread — relocate blocks, resize a visual (e.g. shrink an orbit/photo), or tighten gaps — until everything fits with margin. Never let a page render with text running past the bottom.

**★ PDF content pages** take the real copy from the Figma "A4 - N" frames (text-heavy — reproduce it, don't invent). Layout: partner lockup top-LEFT (small), banner, then a TWO-COLUMN magazine grid with justified body text and the pull-quote inside a column (its text is **centre-aligned**, never flush-left or flush-right). NO runhead caption/line and NO footer/page number on these pages. Reusable questions + answers: `success-story-content.md`.

**★ Case-summary stat cards** (facts + 3 stat cards) use **small, light numbers** (the `.b24-ss-stat__num` — weight 600, not the old heavy 800) so the figure never shouts over the label. Their icons are **flat dark-navy SOLID glyphs with NO backing tile / подложка** — a bare silhouette in brand navy (`#063883`), never a white glyph on a navy square. Use the `bitrix24-images/icons-solid/*-navy.svg` set (recolour a `*-white.svg` glyph to navy; keep the shape a clean silhouette — rocket, people, check-badge — not a filled card). The **same solid navy icons are reused in the `.b24-ss-factpill` metric pills**, so stats and pills read as one system.

**★ Text-treatment patterns (kit §15.x5)** — reusable ways to lay out copy, generalised from the Figma library frames A4-38/63/84/98/106/135. Reach for them instead of flat paragraphs: **numbered steps** (`.b24-ss-steps` / `.b24-ss-step` — navy circle + white number, bold lead-in phrase then regular text) for advice/how-to; **check-bullet lists** (`.b24-ss-checklist` — navy circle-check badge as the marker, never a plain dot; `--2col` for two columns) for achievements/results; **icon feature cards** (`.b24-ss-iconcard` — white card, big dark-navy solid icon centred over a caption); **insight pills** (`.b24-ss-insight` — light-azure soft card, small navy icon badge + one line with a bold figure) for inline success numbers; **number-in-circle stat cards** (`.b24-ss-statdisc` — big navy disc holding the figure at left, label at right) as a calmer alternative to the vertical `.b24-ss-stat` trio; and **label pills** (`.b24-ss-advlabel` — navy pill sub-header like “Advice 1” before a paragraph). Markers are always circled numbers or check-badges; emphasis is **bold** for terms and figures and **bold-italic** for a standout line; icons stay flat dark-navy solid. Sizes follow the same Figma×1.334 scale as the templates. Live reference of all six: `assets/success-story-pdf-patterns-demo.html`. **Use these SELECTIVELY, not on every page.** They are variety tools: reach for one only when the copy genuinely fits its structure (a real step sequence, a list of wins, parallel short insights, headline figures) AND the spread needs breaking up. A page of ordinary Q&A prose should stay prose; forcing a pattern where the text doesn't fit, or repeating the same block page after page, reads worse than plain paragraphs. Aim for at most one or two of these accents per page, and let some pages carry none.

**★ Awards are OPTIONAL** and **partner-supplied** (a ready hexagon-badge image
you drop at `bitrix24-images/success-story/awards-<slug>.png`, placed in the
`.b24-ss-awards` block on the case-summary page/post). **Many stories have none —
delete that block then.** The **certificates** (`.b24-ss-certs`), the **emblem/seal** (`.b24-ss-emblem`) and the **check-band photo** (`.b24-ss-checkband`) work the same way — partner-supplied images/text, the kit only fixes the placement.

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
- **★ Industry Guide "Bitrix24 Tools" are real, localizable links.** In every
  pain→tools→outcome card, wrap each tool name in a real `<a href="…">` (deep-blue
  underlined) so the exported PDF is clickable — never plain text. To localize,
  translate the link text and swap only the domain (`.com`→`.es`→`.pl`), keeping
  the path. Glossary + rule: `assets/LOCALIZATION.md`. Keep the `guide` cover on
  the corporate `.page` palette with the two-tone `logo.svg` and a green
  "Quick Guide" pill — not the partner navy.
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
