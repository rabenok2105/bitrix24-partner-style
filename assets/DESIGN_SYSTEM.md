# Bitrix24 Partner — Brand Style (Design System)

> **This is the Bitrix24 _Partner_ brand style** (партнёрский фирменный стиль) — the visual identity
> for Bitrix24 **Partner** materials. It is one of several Bitrix24 brand styles; other styles
> (e.g. corporate Bitrix24) are maintained as **separate** design systems / skills. When you need
> partner-branded content, this is the one. Delivered as a Claude Code skill named
> **`bitrix24-partner-style`** (invoke it by asking for the "partner brand style" / "партнёрский
> фирстиль", or `/bitrix24-partner-style`).

A design system for generating branded content — **A4 PDF** documents (guides, one-pagers, sales
playbooks, brochures; portrait or landscape), **LinkedIn** square carousels, and **Instagram
Stories** — in the Bitrix24 Partners visual language. Built from the official Bitrix24 Partner
Program Style Guide, the Montserrat brand font, official Partner logos, and the brand imagery
library (cutout people + icons).

**Hand this whole folder to Claude.** Ask Claude to build a document; it reads this spec,
copies component blocks from `bitrix24-template.html`, fills in your content, and renders to PDF.
See §11 "How to work with Claude" at the end.

### 📎 Using this in another chat
This system is self-contained in this folder. To use it in a **different Claude chat / project**,
give Claude these files together:
1. `DESIGN_SYSTEM.md` (this file — the rules) **and** `bitrix24-kit.css` (the actual styles) — both required.
2. `bitrix24-template.html` — the copy-paste component source.
3. The `bitrix24-logo/` folder and the `Montserrat (1)/` folder — so logos and fonts resolve.

Then prompt: *"Use this Bitrix24 PDF design system (DESIGN_SYSTEM.md + bitrix24-kit.css) to build
&lt;document&gt; as an A4 PDF."* Everything below is the single source of truth — if the kit and this
doc ever disagree, the kit wins; tell Claude to reconcile them.

---

## 1. Files in this system

| File | What it is |
|---|---|
| `DESIGN_SYSTEM.md` | This spec — rules, tokens, component catalog, prompting guide. |
| `bitrix24-kit.css` | All design tokens (CSS variables) + ready component classes. Link this in every document. |
| `bitrix24-template.html` | Living styleguide (Bitrix24 **Partners** style — the current default): cover, challenge cards, value list, table, comparison, CTA — as real A4 pages. Copy blocks from here. |
| `README.md` | Quick start + how to export a clean PDF. |
| `bitrix24-logo/` | Official logos. Bitrix24: `logo.svg` / `logo-white.svg` (+ png/jpg/ai). **Partners lockups:** `logo-partner-h.png` / `-h-white.png` (horizontal), `logo-partner-v.png` / `-v-white.png` (stacked). |
| `bitrix24-images/` | **Curated brand imagery.** `people/` — transparent cutout-people photos (clean names). `icons/` — branded product SVGs in navy + `-white` twins. See §8–§9. |
| `People/` · `Icons/` | Full raw asset libraries from Figma (many variants) — pull extra photos/icons here when the curated set isn't enough. |
| `Montserrat (1)/` | The brand font (embedded by the kit). |

**Golden rule:** never invent new colors, spacing, or fonts. Compose documents only from the
tokens and components below. If something is missing, extend the kit deliberately — don't inline
one-off values.

---

## 2. Brand & sub-brands

Two related identities share one system — **each has its own palette** (see §3):

- **Bitrix24** — product guides, industry playbooks. Uses the **corporate palette** (cyan/blue/
  deep + green). Page background pale cool blue (`--b24-page-cool`, the default `.page`). Two-tone
  logo (`logo.svg`). Covers pair a cutout photo with a deep-blue title card and a green
  "Quick Guide" pill.
- **Bitrix24 Partners** — partner enablement / sales material. Uses the **Partner Program palette**
  (deep navy `#063883` + pale blue + green). Two page styles: light (`.page--sky`) and deep-navy
  (`.page--partner-navy`, for covers/dividers). **Monochrome** logo lockup (deep-blue or white),
  horizontal or stacked. Signature devices: **Tetris-style rounded blocks**, dashed frames, and
  comparison tables. Both palettes are applied automatically by the page class — you don't restyle
  components by hand.

**Logo:** the official logo files ship in `bitrix24-logo/`. Bitrix24 uses the two-tone wordmark;
Partners uses the **official one-piece lockup** (`logo-partner-h*.png` / `-v*.png`) — never a
reconstruction. Full usage in §9.

---

## 3. Color

There are **two official palettes** — one per sub-brand. The right one is applied automatically by
the page class (default `.page` = corporate; `.page--sky` / `.page--partner-navy` = Partners).
Use the CSS variable, never a raw hex.

### 3a. Bitrix24 corporate palette — 3 shades of blue + accent green + gradient
| Token | HEX | RGB | CMYK | Role |
|---|---|---|---|---|
| `--b24-cyan` | `#2FC7F7` | 47 199 247 | 65 0 0 0 | **Blue 1** — bright cyan, primary brand color |
| `--b24-blue` | `#409EEF` | 64 158 239 | 68 29 0 0 | **Blue 2** — mid blue |
| `--b24-deep` | `#0066A1` | 0 102 161 | 91 54 13 1 | **Blue 3** — deep blue: dark surfaces, headings, links, body accents |
| `--b24-green` | `#BDF300` | 189 243 0 | 22 0 100 5 | **Accent** — green (accent/background only) |
| `--b24-grad-brand` | `#2FC7F7 → #409EEF` | — | — | **Gradient** — cyan → mid blue |

### Derived shade (not a new color)
- `--b24-deep-2` `#004E7C` — a darker shade of Blue 3, used only to give depth to gradients on
  deep-blue cards/hero. Stays within "shades of blue."

### Semantic aliases (map to the palette — use these in components)
`--b24-navy-900` = `--b24-deep` (titles/text) · `--b24-blue-500` = `--b24-deep` (links) ·
`--b24-lime` = `--b24-green` (pills/badges) · `--b24-lime-ink` = `--b24-deep` (text on green).

**Text on green is sub-brand–aware.** `--b24-lime-ink` defaults to the corporate deep blue
`--b24-deep` (`#0066A1`), but on Partner pages (`.page--sky` / `.page--partner-navy`) the kit
remaps it to the **partner navy `--b24p-deep` (`#063883`)** — so pills, tags and lime highlights
match the `.b24-btn` and the rest of the partner palette (never corporate blue on a partner page).

### Surfaces & text (tints of the palette)
| Token | Hex | Use |
|---|---|---|
| `--b24-page-cool` | `#F4FAFE` | Bitrix24 page background |
| `--b24-page-sky` | `#DCF2FE` | Partners page background (via `.page--sky`) |
| `--b24-card` | `#E9F5FD` | Light info-card fill |
| `--b24-white` | `#FFFFFF` | Table cells, white cards |
| `--b24-line` | `#C8E6F6` | Hairlines, table grid |
| `--b24-dashed` | `#6EC0EC` | Dashed outline stroke |
| `--b24-text` | `#143A57` | Body copy (deep-blue slate) |
| `--b24-text-mute` | `#5E86A3` | Labels, captions, footer |

### Gradients (pre-built)
- **★ `--b24-grad-partner-navy`** — the **signature Partner gradient**: a RADIAL azure glow → deep
  navy. Used **everywhere** a partner dark surface appears — covers/dividers/CTA
  (`.page--partner-navy`), table & comparison headers, and app tiles. See §3b. This is the one.
- `--b24-grad-partner-light` — Partner light page background (`.page--sky`).
- `--b24-grad-brand` — corporate cyan→blue brand gradient (buttons, accents, cover art).
- `--b24-grad-navy` / `--b24-grad-header` / `--b24-grad-page-sky` — corporate (non-partner) variants.

**Contrast rules (important — the green is very light):**
- On any deep-blue surface use **white** text (wrap the zone in `.b24-onnavy`, or use a full
  `.page--navy` sheet).
- **Green `#BDF300` is an accent/background only.** As text it is legible **only on deep blue**
  (e.g. `.b24-hl` highlight words on the navy cover). Never green text on white, never white text
  on green. Text on a green surface is always `--b24-deep` (`.b24-hl-lime`, `.b24-pill`).
- For emphasis on light pages use **deep-blue bold** (`<strong>`) or a green pill, not green text.

### 3b. Bitrix24 Partners palette — deep navy + pale blue + green + white
The Partner Program uses a **different, darker blue** as its main color. Applied automatically on
`.page--sky` (light) and `.page--partner-navy` (dark) — you rarely reference these tokens directly.

| Token | HEX | RGB | CMYK | Role |
|---|---|---|---|---|
| `--b24p-deep` | `#063883` | 6 56 131 | 95 57 0 49 | **Main** — deep navy: backgrounds, headings, table headers, logo |
| `--b24p-light` | `#EFFBFF` | 239 251 255 | 6 2 0 0 | **Light blue** (optional) — light page backgrounds |
| `--b24p-green` | `#BDF300` | 189 243 0 | 22 0 100 5 | **Accent** — green (same as corporate) |
| `#FFFFFF` | `#FFFFFF` | 255 255 255 | 0 0 0 0 | **White** — text/logo on navy |
| `--b24-grad-partner-navy` | radial `#0A63A6→#005E98→#04213F` | — | — | ★ **Signature gradient** (radial azure glow → deep navy) — covers, dividers, CTA, dark cards, **table/comparison headers, app tiles** |
| `--b24-grad-partner-light` | pale-blue gradient | — | — | Light page background |

**★ The signature gradient is the single most recognizable partner cue.** It is a **vivid azure
glow in the upper-centre fading to deep navy at the edges** — NOT a flat navy fill. Every dark
sheet (`.page--partner-navy`: covers, section dividers, closing CTA) must use it. Do **not**
flat-fill navy or swap in a subtle mono gradient — that's the #1 way partner materials end up
looking off-brand. The **same radial gradient is used on every partner dark surface** — dark
sheets, table & comparison headers, and app tiles — so the whole system reads as one recognizable
gradient. The flat `--b24p-deep` (`#063883`) stays for navy **text/headings/logo/table labels on
light pages**, not for backgrounds.

Colors may also be used with transparency. `--b24p-deep-2` / `--b24p-deep-hi` are the darkest/
brightest stops of the signature gradient (not new colors).

---

## 4. Typography

**Font: `Montserrat`** — the official brand font. One family for both display and body,
separated by weight. It is **embedded** from the local `Montserrat (1)/static/` folder via
`@font-face` in the kit, so exported PDFs are fully self-contained (no internet needed).
- **Display / headings:** Montserrat **800 (ExtraBold)** — the standard heading weight
  (cleaner than Black; matches the reference). Black 900 is available but not the default.
- **Body / UI:** Montserrat 400 (Regular) / 500 / 600 / 700.

Set via `--b24-font-display` and `--b24-font-body` (both Montserrat). If you move the font folder,
update the `url()` paths at the top of `bitrix24-kit.css`.

### Scale (A4)
| Class | Size / weight | Use |
|---|---|---|
| `.b24-display` | 46px / 800 | Cover title only |
| `.b24-h1` | 31px / 800, blue-400 | Page/section title |
| `.b24-h2` | 22px / 800, navy-900 | Sub-section |
| `.b24-h3` | 16px / 700 | Block heading |
| `.b24-lead` | 15.5px | Intro paragraph |
| `.b24-p` | 13px | Body copy |
| `.b24-label` | 11px / 600, muted | Small caption above a block ("Business pain") |
| `.b24-small` | 10.5px | Footnotes, footer |

### Inline
- `<strong>` / `.b24-strong` — bold deep-blue emphasis (use this on light pages).
- `.b24-hl` — **green** highlighted word. **Only on deep-blue surfaces** (e.g. the cover lead).
- `.b24-hl-lime` — word on a **green** rounded background (deep-blue text) — safe anywhere.
- `a` / `.b24-link` — underlined deep-blue link (used heavily in "Tools" lists).

**Rules:** one `.b24-display` per document (the cover). Headings are tight
(`letter-spacing:-.01em`), never all-caps. Keep line length ≤ ~70 characters on A4.

---

## 5. Layout & page format

- **Default format:** A4 portrait, `210 × 297 mm` (via `@page`). Other canvases ship as presets — see **§5a**.
- **One `.page` element = one printed sheet.** Stack as many as you need in one HTML file;
  each breaks to a new page automatically.
- **Margins:** `--b24-page-pad` = 18 mm content padding. Cover art may go full-bleed with
  `.page--flush` (padding 0).
- **Structure of a content page:**
  1. `.b24-runhead` — running header: document title (left) + logo (right), hairline under.
  2. Content (`.b24-h1`, then components).
  3. `.b24-footer` — pinned to bottom (`margin-top:auto`): logo (left) + `Page <span class="b24-pageno"></span>` (right, auto-numbered).
- **Backgrounds:** default `.page` = corporate cool. `.page--sky` = Partners light;
  `.page--partner-navy` = Partners deep-navy (covers/CTA, auto-whitens text);
  `.page--navy` = corporate deep-blue sheet. Navy sheets whiten text automatically.
- **Grid:** two-column blocks use CSS grid `1fr 1fr` (see the pain→tools card). Use the
  `.b24-row`/`.b24-col` flex utilities for ad-hoc columns.
- **Spacing:** only use the `--b24-s*` scale (4→64px). Cards sit `--b24-s5` (20px) apart.

### 5a. Page format presets
One brand, several canvases. Add a size modifier next to `.page`; the palette classes
(`.page--sky` / `.page--partner-navy`) still apply on top. The 1080 px social presets carry a
**punchier type scale** automatically (A4 body type is too small at that size).

| Preset | Class | Canvas | Export |
|---|---|---|---|
| A4 portrait *(default)* | `.page` | 210 × 297 mm | PDF |
| A4 landscape | `.page--a4-land` | 297 × 210 mm | PDF — doc must also set `@page { size: A4 landscape; margin:0 }` |
| **Industry Guide** | `.page--guide` | 1080 × 1350 px | **multi-page PDF** (all sheets in one file) |
| LinkedIn square | `.page--li` | 1080 × 1080 px | PNG per slide |
| **LinkedIn post (4:5)** | `.page--post` | 1080 × 1350 px | **JPEG** per slide (the Success Story post series) |
| Instagram Story | `.page--story` | 1080 × 1920 px | PNG per slide |

- **Industry Guide (`guide`)** is a **vertical multi-page PDF** — see **§5b**. It is the one 1080 px
  preset that stacks many sheets into a single PDF (like A4), not one image per slide.
- **Social = one `.page` per slide.** Render each slide with `@page { size: 1080px 1080px; margin:0 }`
  (story: `1080px 1920px`) to a 1-page PDF, then rasterize that page to **PNG** (one image per slide).
  For carousels, keep one slide per HTML file so each exports to its own image cleanly.
- **Instagram safe-zone:** wrap story content in `<div class="b24-safe">…</div>` — it insets the
  top/bottom ~240 px that Instagram overlays with the avatar (top) and reply/CTA bar (bottom).
- **Runhead / footer / page numbers** are for multi-page A4 (PDF); social slides normally use just
  a logo (and an optional slide counter), no running header.
- Social slides skip A4 mm padding and use their own px padding; drop in `.b24-plogo--cover`
  (44 px on social) for the logo. Everything else — colors, pills, buttons, tetris, stars — is shared.

### 5b. Industry Guide — a distinct direction  (`.page--guide`, format `guide`)

A **per-industry quick guide** (Construction & Remodeling, Digital Marketing, …): a
**1080 × 1350 px vertical, multi-page PDF**. It is its own direction, with a fixed page
sequence and one signature component. **Living reference:** `industry-guide-template.html`.
**Render:** `python3 scripts/render.py industry.html --format guide` → one multi-page PDF.

**Sub-brand — Bitrix24 corporate (not Partners).** Guides use the default `.page` family with
the **mono-ink logo `logo-ink.svg`** (the Bitrix24 wordmark recoloured to `#012254`) and a green
**"Quick Guide" pill**. Headings use Montserrat **Bold (700)** here, not ExtraBold — the cover
`.b24-display`, the section `.b24-h1`, and the `.b24-ig-star` decorations carry **no shadow**.
**Do NOT** put `.page--sky` /
`.page--partner-navy` on a guide page, and don't use the partner lockup here.

**★ Locked palette (the whole guide).** `.page--guide` fixes these — reuse, don't override:

| Role | Value |
|---|---|
| Page background | `#F5FAFF` |
| Dark surfaces — icon tiles, cover person/title plates, closing band, headings | one shared gradient **`var(--b24-ig-navy)`** (deep navy `#01447B` + soft azure glow) |
| Large content plates (the pain→tools→outcome cards) | `#01447B` at **alternating opacity — 4 %, 10 %, 4 %, …** (`.b24-card--t4` / `.b24-card--t10`) |
| Regular body text | `#002153` at **80 %** (`.page--guide` sets `--b24-text` to it) |

The **one** dark-navy gradient is used everywhere a dark surface appears, so tiles, plates and
headings all read as the same colour. `.b24-h1` is filled with it (gradient text); the cover
title/plates carry it as a background.

**Page sequence (cover → challenge pages → key-value close — ~6 pages at 2 cards/page):**

1. **Cover** (`.page--guide.b24-ig-cover`): a top row with `logo-ink.svg` (`#012254`) pinned right
   (`.b24-ig-head`). Below it a dark-navy **person plate** (`.b24-ig-plate`) — a **shorter band**
   pushed to the bottom (inline `height` ≈ 40 % of the free area + `margin-top:auto`) so **free
   space is left above it near the logo**. The cutout person floats **on top** of it
   (`.b24-ig-figure`) — **big, not clipped by the plate**. Make the figure a **child of the plate
   with `bottom:0`** so its bottom always sits **flush on the plate bottom (no gap)** while it
   overflows upward, its **head at the same height as the logo** (set only inline `height`; the
   upper body sits over the free space). `.b24-ig-figure` carries **no drop-shadow** — the cutout
   sits directly on the plate. Scatter 2–3 3-D brand
   **stars** around the person (`.b24-ig-star`, `bitrix24-images/star-3d.png`) — varied sizes,
   a few degrees of rotation, one optionally behind the person (`z-index:1`). Then a dark-navy
   **title plate** (`.b24-ig-titlecard`) that **hugs its content and is pinned to the bottom**
   (`margin-top:auto`, no filler space): a `.b24-ig-titlerow` holds the big white `.b24-display`
   title (left) and the green **"Quick Guide" pill** (right), aligned by their **top edges**;
   below, a white `.b24-lead` intro (~24 px). To stress part of the intro, make that span **bold
   in the same size, green or white** (`.b24-em--green` / `.b24-em--white`) — **not** a coloured
   underline. No bottom logo on the cover.
2. **Challenge pages**: an optional `.b24-h1` section title on the first, then a stack of
   **pain → tools → outcome** cards, tints alternating 4 %/10 % **down the whole document**.
   **Fit 2 or 3 blocks per page** — the number of blocks and how much copy each holds varies by
   content and by localization (COM vs ES/PL/DE), so this flexes per guide. **HARD RULE: the last
   block on a page must never reach the page bottom — always leave a clear bottom margin below it.**
   Put **3 blocks on a page only if they still leave that margin**; if they don't, **move a block
   to the next page and use 2 blocks per page** (never shrink type or overpack — a sheet clips
   overflow). A **2-block page keeps the centered logo footer**; a genuinely full **3-block page
   drops it**. (The bundled Construction template is 2 blocks/page — every page ends with a wide
   bottom margin.)
3. **Key-value close**: `.b24-h1` title, a `.b24-bullets` value list, a `.b24-quote`
   (green left-bar) thesis, and a closing **photo band** — a `.b24-ig-plate` with people
   (`duo-team`, sized large) as a **child of the plate** via `.b24-ig-figure` (`bottom:0`, flush
   on the plate bottom, not clipped, no shadow), plus 2–3 `.b24-ig-star` around them. Last page:
   **no** logo footer.

**Footer.** Guide content pages carry **only a centered logo** (`.b24-ig-foot`) — **no rule
line, no "Page N".** Put it on every middle page that has room (typically a 2-block page); a
**3-block page drops it** to make space. Never on the first (cover) or last (key-value) page.

**★ Industry people (cover + closing figure).** The `.b24-ig-figure` on the cover (one person)
and on the closing band (1–2 people) must **match the guide's industry** — swap by *attire*, not
only ethnicity/pose — and **every person always holds a device (phone / laptop / tablet)** because
we sell software. Reuse the bundled library for office-type guides; **generate a transparent
industry cutout** (worker in hi-vis, clinician in scrubs, …) for industries the library doesn't
cover, save it to `bitrix24-images/people/`, and point the two `src` paths at it. The full recipe
(generation prompt, framing/alpha requirements, industry→attire→device table) is **`PEOPLE.md`**.

**Signature component — Pain → Bitrix24 Tools → Practical Outcome** (`.b24-card.b24-solve`):
a translucent `#01447B` plate (alternating 4 %/10 %) with a two-column grid — **Business pain**
left, **Bitrix24 Tools** right (a comma list of links), a `.b24-tile` (`var(--b24-ig-navy)` +
white brand SVG) pinned top-right, then a full-width **Practical Outcome** row. Only the small
`.b24-label` captions distinguish the columns: the **pain text, the outcome text and the tool
links all share one style** — the body colour/weight/typeface (`#002153` @ 80 %, regular),
nothing bold; links carry only an underline. Section headings (`.b24-h1`) are a **solid** deep
navy `#01447B` (not gradient-filled — a flat colour avoids the clip-to-text box some viewers show).

> **★ The "Bitrix24 Tools" list is a set of real, localizable links.** Each tool name is an
> `<a href="…">` (deep-blue underline) so the exported PDF is clickable. The text **and** the
> URL localize per market: translate the text and swap the link domain (`.com`→`.es`→`.pl`),
> keeping the path. Full glossary + workflow: **`LOCALIZATION.md`**. Layouts must tolerate
> ~20–30 % text growth (ES/PL/DE) — split to a new page rather than shrink type; each
> `.page--guide` sheet is fixed-height with `overflow:hidden`, so overruns clip.

**What's provided in the kit for this direction:** the `.page--guide` size + locked palette
(`#F5FAFF`, `--b24-ig-navy`, `--b24-text`) + a calmer type scale; the cover/close helpers
`.b24-ig-cover` / `.b24-ig-head` / `.b24-ig-plate` / `.b24-ig-figure` / `.b24-ig-titlecard` +
`.b24-ig-titlerow` / `.b24-em--white` + `.b24-em--green` (bold same-size emphasis) /
`.b24-ig-star` (with `bitrix24-images/star-3d.png`) /
`.b24-ig-foot` (centred, enlarged logo); the card tints `.b24-card--t4` / `.b24-card--t10`;
guide-sized tuning of `.b24-card`, `.b24-solve*`, `.b24-tile`, `.b24-bullets`, `.b24-quote`,
and solid `.b24-h1`. Everything else — pills, logo — is the shared corporate system.

---

### 5c. Success Story — one narrative, TWO synchronized outputs  (`.page` + `.page--post`)

A **partner testimonial** produced as **two deliverables at once**, from the *same*
interview: a multi-page **PDF** and a series of **LinkedIn JPEG posts**. This is a
**Partners** direction — it uses `.page--sky` / `.page--partner-navy` and the
partner lockup, plus the `.b24-ss-*` components (kit §15). **Living references:**
`success-story-pdf-template.html` and `success-story-posts-template.html` (both
filled with the Askarasoft case), plus `success-story-pdf-template-reyada.html` (the Reyada case, showing the extended §15.x layouts); blank starters `success-story-*-skeleton.html`.

**★ Understand the difference — PDF vs LinkedIn. They are NOT the same file at two
sizes; they are two media with different jobs:**

| | **PDF** (`--format a4`) | **LinkedIn posts** (`--format post`) |
|---|---|---|
| Canvas | A4 portrait `.page` (210×297 mm) | `.page--post` 1080×1350 px (4:5) |
| File(s) | ONE multi-page PDF | a SERIES — one **JPEG per post** (~10) |
| Density | several Q&A per page | **one idea per slide**, bigger type |
| Header | partner runhead + page number on every sheet | plain `Bitrix24` wordmark on the cover only |
| Speaker | a dedicated intro page + quote cards | facts sit **on the cover** (`.b24-ss-personcard`) |
| CTA | a **real clickable** green "Sign up" link | ends "**use the link in the description**" (`.b24-ss-note`) — a post carries no clickable button |
| Job | send / print / email as a document | drip or carousel on the feed |

Author them as two HTML files (they share every `.b24-ss-*` component). For the
posts, **one `.page--post` per post** — the render script rasterizes each page to
its own JPEG.

**Page / post sequence** (both follow the same arc; the PDF merges some, the posts
split one-idea-per-slide):
cover → story intro → beginning of cooperation → work process / first clients →
lead generation → results → advantages / impact → advice → **case summary**
(facts + 3 stat cards + optional awards) → **CTA**.

**★ Cover photo — a NORMAL photo tinted by an OVERLAY, exactly like Figma.** The
partner sends an ordinary photo (full colour, usually with a background). You do
**not** recolour it — the brand navy comes from the blend: `.b24-ss-photo` sits
over the cover's navy gradient with **`mix-blend-mode: overlay`**, which tints the
photo into the monochrome-navy cover. So the image stays a real photo; the tone is
the overlay. `scripts/prep_cover_photo.py PHOTO.jpg --name <slug>` just **removes
the background** (a clean cutout blends best) and cuts a round avatar — a photo
*with* its background works too (`--keep-bg`; the overlay still tints it and the
inner-edge fade hides the seam). Then place `<img class="b24-ss-photo …">` and
**pick the framing that suits THAT photo** — `--right` (default), `--top`
(upper-centre, title below), `--bottom` (person low, title on top), `--wide` (two
people). Match the layout to the photo; don't force it into one fixed position. **The photo comes from the partner's brief (ТЗ)** and is the SAME person shown on the **cover** and in the **round avatar** (`.b24-ss-speaker__avatar`) — the avatar being a navy brand disc with that person's cut-out face composited on it, not a rectangular photo masked to a circle. A further placement variant is a **city / buildings image with the person laid on top** (the page-7 band — `.b24-ss-band` plus a cut-out person) — use it when the brief supplies such a photo.

**★ Awards are OPTIONAL and partner-supplied.** The hexagon award badges are a ready
image the partner attaches (`bitrix24-images/success-story/awards-<slug>.png`) — you
only place it in the `.b24-ss-awards` block on the case-summary page/post. **Many
stories have no awards** — delete the whole block then; the stat cards stand alone.

**★ PDF content pages (A4) — a two-column magazine.** Take the copy from the Figma
"A4 - N" frames (it is text-heavy — reproduce the real answers, don't invent).
Each content page: the partner lockup **top-LEFT, small** (`.b24-ss-loghead`, no
runhead caption and no rule line), the `.b24-ss-banner`, then **two EQUAL columns**
(`.b24-ss-cols`, `1fr 1fr`, 14 mm gutter). Body copy is **justified**; the question
is a bold navy `.b24-qa__q`, the answer a `.b24-qa__a`. Content flows column 1 then
column 2 (one Q&A per column; a single long answer flows across both with
`.b24-ss-flow2`). The **pull-quote sits inside a column** (left or right column); its **text is always
centre-aligned** — never flush-left or flush-right (it just must not stretch centred
across the whole page). **No footer, no page number, no bottom logo.** Tool chips
use a solid `*-white` glyph in a blue gradient circle (`.b24-ss-chip__ic`), labels
SemiBold; the **page-3 speaker avatar is a dark brand-navy disc with the person's
background-removed face cut out and composited on top** (azure→deep-navy radial disc, cut-out
head-and-shoulders bottom-aligned — never a plain cropped photo on a coloured circle), set in the
blue gradient ring (`.b24-ss-speaker__avatar`); the name SemiBold navy. Reusable question set + this case's answers:
`success-story-content.md`. **Banners (posts) do NOT use this** — they keep the
centred composition with a uniform **70 px** gap from the banner heading to the text.

**Signature components (kit §15):** `.b24-ss-cover` + `.b24-ss-photo` (duotone cover
photo, edge-fade), `.b24-ss-banner` (rounded navy-gradient section heading), `.b24-qa`
(question/answer pairs), `.b24-ss-speaker` / `.b24-ss-personcard` (speaker facts),
`.b24-ss-pquote` (big quote-mark pull-quote), `.b24-ss-chips` (product tags),
`.b24-ss-channels` (lead-gen channel cards), `.b24-ss-stats` (icon + number + label),
`.b24-ss-facts` (label/value rows), `.b24-ss-awards` (optional), `.b24-ss-ctacard`
(closing card — green link on PDF, "link in the description" on posts), `.b24-ss-orbit`
(the partner-community graphic).

**Extended layouts (kit §15.x — generalised from the Reyada case):** `.b24-ss-factpills` (vertical azure metric pills, e.g. “110+ clients”), `.b24-ss-certs` (deep-navy card holding certificate thumbnails, 2 top + 1 centred), `.b24-ss-checkband` + `.b24-ss-checkpill` (a wide photo band with floating check-badge role pills), and `.b24-ss-emblem` (a centred seal such as “Authorized Training Provider”). The same direction also supports a **full-bleed pre-toned cover** (one image already on the navy gradient, title overlaid — no blend needed), a **multi-paragraph intro**, the **speaker card top-LEFT** with the Q&A wrapping beside it, and the **buildings + person band**: the **city visual is its own layer pinned to the bottom**, and a **cut-out person is placed on top ONLY when the brief supplies a good photo** — sized to stay **fully inside the page, never clipped** by the edge (person centred). The certificate thumbnails, the emblem/seal and the check-band photo are **partner-supplied CONTENT** — like the award badges: swap the images (and the pill/label text) per story, the kit only fixes the **placement**. **Text sizes on that template are taken straight from Figma** (each Figma px ×1.334, since Figma's 595-px page renders here as an ~794-px A4), so the copy fills the page exactly as in the source frames rather than at the kit's default density. Reference: `success-story-pdf-template-reyada.html`.

**Text-treatment patterns (kit §15.x5 — generalised from the Figma library frames A4-38/63/84/98/106/135):** `.b24-ss-steps`/`.b24-ss-step` (numbered advice — navy circle + white number, bold lead-in then regular justified text, 2-col staggered), `.b24-ss-checklist` (result bullets with a navy **circle-check** marker instead of a dot; `--2col`), `.b24-ss-iconcard` (white card, big dark-navy **solid** icon centred above a caption), `.b24-ss-insight` (light-azure soft card — small navy icon badge + a line with a **bold** figure, for inline success numbers), `.b24-ss-statdisc` (horizontal stat card — big navy disc holds the figure at left, label at right; a calmer alternative to the vertical `.b24-ss-stat` trio), and `.b24-ss-advlabel` (navy pill sub-header such as “Advice 1” before a paragraph). Rules that carry across all of them: list markers are **circled numbers or check-badges, never plain dots**; emphasis is **bold** for terms/figures and **bold-italic** for a standout sentence; icons are flat **dark-navy solid**; sizes use the Figma×1.334 scale. Live reference: `assets/success-story-pdf-patterns-demo.html`. **Use these SELECTIVELY, not on every page.** They are variety tools: reach for one only when the copy genuinely fits its structure (a real step sequence, a list of wins, parallel short insights, headline figures) AND the spread needs breaking up. A page of ordinary Q&A prose should stay prose; forcing a pattern where the text doesn't fit, or repeating the same block page after page, reads worse than plain paragraphs. Aim for at most one or two of these accents per page, and let some pages carry none. **Stat / fact icons are flat dark-navy SOLID glyphs on NO tile** (bare `#063883` silhouette, from `bitrix24-images/icons-solid/*-navy.svg`) — never a light glyph on a navy square — and the **stat numbers are small and weight-600** (`.b24-ss-stat__num`), so the icon and label carry the card, not an oversized figure.

---

## 6. Component catalog

Components live in `bitrix24-template.html` (rendered in the **Partners** style — the current
default). Copy the block, swap the text. Every component works in either sub-brand: the palette
follows the page class (`.page` vs `.page--sky`/`.page--partner-navy`).

### Bitrix24 cover — photo + title card  (`.page--flush`)
Full-bleed page split into a light photo zone (top) and a deep-blue title card (bottom,
`.b24-onnavy`). Elements: logo top-right, 1–2 `.b24-star` sparkles, cutout-photo placeholder,
`.b24-pill` "Quick Guide", `.b24-display` title, `.b24-lead` intro with `.b24-hl` highlights.
*When:* first page of a **Bitrix24** (corporate) guide.

### Partners divider / cover  (`.page--partner-navy`)
Full deep-navy (`#063883`) sheet with the **centered white Partners lockup** (stacked),
green sparkles, and Tetris blocks bleeding off the corners — mirrors the Partner Program style
guide cover. *When:* opening or section-break page of a partner document.

### Pain → Tools → Outcome card  (`.b24-card.b24-solve`)
The signature Bitrix24 "challenge" block. Two-column grid: **Business pain** (left) and
**Bitrix24 Tools** (right, as a comma-separated list of `<a>` links), then a full-width
**Practical Outcome** row. A gradient app-icon `.b24-tile` (emoji/glyph) sits top-right.
*When:* mapping problems to product capabilities. Stack 2 per page.

### Bullet value list  (`.b24-bullets`)
Square navy bullets; lead each item with a bold `.b24-strong` label. On navy pages bullets turn lime.
*When:* listing benefits / key values.

### Quote callout  (`.b24-quote`)
Green left-bar, larger text, no background. *When:* a summary or thesis statement worth setting apart.

### Table  (`.b24-table-wrap > .b24-table`)
Rounded white card, **navy gradient header** with white display type, zebra rows, hairline grid.
First column is a bold blue label. Emoji accents allowed in cells.
*When:* comparisons, overviews (e.g. Effort/Result), specs.

### Comparison card  (`.b24-compare`)
Two-column: split navy header (`❌ Weak pitch` | `✅ What the client wants`) over a white body
with two large quoted statements. Often followed by a `.b24-dashed` conclusion box with a
`.b24-quotemark` watermark. *When:* reframing features vs. outcomes; before/after; do/don't.

### Checklist  (`.b24-checklist` with `.is-no` / `.is-yes`)
❌ / ✅ prefixed lines. *When:* quick do/don't or feature-vs-benefit points.

### CTA button — "Become a Partner"  (`.b24-btn`)  ⭐ fixed rules
The primary call-to-action. **Three hard rules:**
1. **Always a real link** — it must be an `<a href="https://partners.bitrix24.com/">` so the
   exported PDF carries a clickable hyperlink. Never a plain `<span>`.
2. **Always horizontally centered** on the page — wrap it in `.b24-btn-center`.
3. **Size up freely** — `.b24-btn` (default) → `.b24-btn--lg` → `.b24-btn--xl`. Bigger is on-brand.

Green fill, deep-blue label. Use on the closing page (deep-navy `.page--partner-navy` looks best).
```html
<div class="b24-btn-center">
  <a class="b24-btn b24-btn--lg" href="https://partners.bitrix24.com/">
    Become a Partner <span class="b24-btn__arrow">→</span>
  </a>
</div>
```

### Callout / CTA box  (`.b24-dashed`, `.b24-cta`)
Dashed rounded frame for highlighted asides. A small tilted `.b24-tag` ("and gets") and the
`.b24-arrow` add personality.

### Badges  (`.b24-pill`, `.b24-pill--outline`, `.b24-tag`)
Green pills for labels; outline variant on light backgrounds; tiny tilted tag for annotations.
(For the main action use `.b24-btn`, not a pill — the pill is not a link.)

### App-icon tile  (`.b24-tile`)
Rounded-square blue gradient holding a white glyph/emoji — echoes Bitrix24's in-product app icons.

---

## 7. Decorative elements

- **Sparkle stars** (`.b24-star`): scatter 1–3 near the cover title / hero. Brand green `#BDF300`.
  Vary size (36–60px). Don't overcrowd. (`.b24-star--lime` is an alias — same green.)
- **Tetris rounded blocks** (`.b24-tetris`) — the Partners graphic motif: large rounded squares
  with one notched corner (`.b24-tetris--notch-tr` / `--notch-bl`), that interlock like Tetris.
  Deep-navy (default) and light (`.b24-tetris--light`) variants; pair with a green `.b24-dot`.
  Use as **background decoration** bleeding off the page edges at low opacity — never let them
  compete with the message. Partners only.
- **Dashed frames** (`.b24-dashed`): the Partners motif — hero outlines and CTA boxes.
- **Quote-mark watermark** (`.b24-quotemark`): oversized `"` in `--b24-line`, low emphasis,
  bottom-right of a callout.
- **Curved arrow** (`.b24-arrow`): hand-drawn-style pointer connecting a note to a conclusion.
- **Floating objects** (reference used coins, a toy plane): optional themed cutout PNGs, softly
  shadowed, partially off-frame. Keep subtle.

Position decoration with `.b24-deco` (absolute, `z-index:0`) and keep text in `.b24-content-z`.

---

## 8. Imagery

- **★ Industry people (for Industry Guides).** The cover/closing figures should **match the
  guide's industry by attire** (construction → hi-vis + hard hat; medical → scrubs/coat; …) and
  **always hold a device (phone/laptop/tablet)** since we sell software. Reuse the bundled library
  when a generic business look fits; otherwise **generate a transparent industry cutout** and drop
  it in. The complete feature — generation prompt, framing/alpha requirements, and an
  industry→attire→device table — is in **`PEOPLE.md`**.
- **Style:** photorealistic **cutout people** (no background) — smiling professionals, business
  attire, often holding a phone/tablet/prop relevant to the topic. Placed on the light zone or
  overlapping a navy card.
- **The kit now ships a real photo library** (from the Figma *People* set): transparent-background
  1000×1000 cutouts. A large curated, cleanly-named set (24+) lives in **`bitrix24-images/people/`**
  (e.g. `man-laptop.png`, `man-suit.png`, `woman-headset.png`, `man-asian-suit.png`,
  `woman-arms-crossed.png`, `duo-team.png`, `woman-glasses.png`, `man-phone.png`) —
  a diverse mix of gender/ethnicity and poses (laptop, tablet, phone, arms-crossed, pointing,
  thinking, a duo). The **full raw library** (70+) is in `People/` if you need even more.
- **Use them where they add life** — covers, hero zones, a value/quote page, a closing page —
  not on every page. Two ways:
  - **Floating cutout** (`.b24-cutout`) — a transparent PNG bleeding off a cover/hero, positioned
    with inline `height` + `right/bottom`. Keep text in `.b24-content-z` above it. Add
    `.b24-cutout--shadow` for a soft ground shadow. Best on navy covers / CTA pages.
  - **Photo band** (`.b24-photo > img`) — a real image filling a rounded container (`object-fit:
    cover`), e.g. a full-width band on a content page.
- Keep faces friendly, diverse, front-lit. Never stretch; the classes handle fit. Never place
  small body text over a busy photo.

```html
<!-- floating cutout on a navy cover (person on the right, text on the left) -->
<img class="b24-cutout b24-cutout--shadow" src="bitrix24-images/people/woman-laptop.png" alt="">
<!-- photo band on a light content page -->
<div class="b24-photo" style="height:230px"><img src="bitrix24-images/people/man-tablet.png" alt=""></div>
```

---

## 9. Iconography & logo

### ★ Icon rule for ALL PDFs — the official Bitrix24 icon base (`ICONS.md`)
Icons come from the official **Bitrix24 "Common" icon library**; the full base — every icon,
its meaning, and its Figma node id — is cataloged in **`ICONS.md`** (read it to choose icons).
The rule, for every PDF (Industry Guide and all others):
- **Default to the SOLID set** (*Solid Icons (Web and Mobile)*). Use **Outline Bold (Web)** only
  when the user explicitly asks for the outline look.
- **One icon style per file — never mix.** Whole document is Solid, or whole document is Outline.
- **Pick by MEANING, not decoration** (a leads block → *Lead*; growth/optimisation → *Trend up* /
  *Statistics arrow* / *Graphs diagram*; automation → *Business process*; access → *Shield* /
  *Lock*). Use the semantic index in `ICONS.md`.
- **Recolour to the design system** (icons export in brand green — never use them green):
  **white** on navy tiles / dark surfaces, **deep navy `#01447B`** inline on light pages. Export
  with Figma `download_assets` (svg) by node id, then run `scripts/prep_icon.py raw.svg <name>
  --dir assets/bitrix24-images/icons-solid` to get the `<name>.svg` (navy) + `<name>-white.svg` twins.
- **Fetch on demand — don't bulk-download.** For each document, look up only the few icons it
  needs in `ICONS.md`, check the `bitrix24-images/icons-solid/` cache, and fetch just the missing
  node ids (a handful per doc — light on Figma's per-seat limit). The cache grows over time; it is
  seeded with `lead`, `crm`, `funnel`, `chart`. Keep every icon in a document the same family; the
  current Industry Guide still uses the older curated `bitrix24-images/icons/` set.

- **Brand icons** live in **`bitrix24-images/icons/`** — clean
  single-color SVGs in brand navy, each with a `-white.svg` twin for dark surfaces. All are
  normalized to a centered square so they sit perfectly centered and at a uniform optical size in
  any tile. **Prefer these over emoji.** Two groups:
  - **Product / concept:** `ai`, `crm`, `calendar`, `funnel`, `messenger`, `person`, `cart`.
  - **UI / utility:** `check`, `cross`, `plus`, `minus`, `clock`, `lock`, `unlock`, `alert`,
    `settings`, `refresh`, `filter`, `play`, `pause`, `mic`, `trash`.
  (The full raw icon library is in `Icons/`.)
  - **In an app tile** (navy gradient) use the white icon: `<div class="b24-tile"><img src="bitrix24-images/icons/crm-white.svg" alt=""></div>`
  - **Inline** next to a label use `.b24-ic` with the navy icon on light pages / the white one on
    navy: `<span><img class="b24-ic" src="bitrix24-images/icons/ai.svg" alt=""> AI, scaled by tier</span>`
- **Ready-made badges** (signature-gradient circle + glyph — the official designer assets):
  `badge-check` and `badge-1` / `badge-2` / `badge-3`, each with a `-onnavy.svg` twin (pale badge for
  navy pages). Use these for **checklists and numbered steps** — they carry the signature gradient.
  - **Checklists:** just use `.b24-checklist` with `.is-yes` / `.is-no`; the kit renders the check
    badge / cross automatically. **Never use ✅ / ❌ emoji** — emoji checkmarks are the #1 "made by
    a bot" tell; the brand check badge is the only correct tick.
  - **Numbered steps** (e.g. a 3-step list, ranked cards): drop in `badge-1/2/3.svg` (`-onnavy` on
    navy) instead of a hand-made number circle.
- **App tiles** (`.b24-tile`) represent Bitrix24 tools/apps — put a brand icon (above) or, as a
  quick stand-in, an emoji glyph.
- **Inline emoji** in tables/lists (🎯 ⚡ 🤝 💎 📚 🔥 ✅ ❌) is still on-brand for quick accents, but a
  brand icon reads more polished for product/tool references.
- **Logo files** in `bitrix24-logo/`:
  | File | Use |
  |---|---|
  | `logo.svg` | **Bitrix24** two-tone wordmark (cyan "Bitrix" + deep "24" + clock). Light backgrounds. |
  | `logo-white.svg` | All-white **Bitrix24** wordmark — deep-blue / photo backgrounds. |
  | `logo-partner-h.png` / `logo-partner-h-white.png` | **Partners horizontal lockup** — deep-navy / white. The official one-line lockup. |
  | `logo-partner-v.png` / `logo-partner-v-white.png` | **Partners stacked lockup** — deep-navy / white. Two-line version for covers/dividers. |
  | `logo.png` / `logo-circle.png`, `logo.jpg`, `logo-b24.ai` | Bitrix24 raster / print / source. |

  **Bitrix24 lockup** (corporate docs) — two-tone SVG:
  `<span class="b24-logo"><img src="bitrix24-logo/logo.svg" alt="Bitrix24"></span>` (white variant on navy).

  **Partners lockup** — use the **official single-image lockup** (extracted from the Partner
  Program Style Guide — one cohesive wordmark, correct font). **Do NOT rebuild it** from the
  Bitrix24 wordmark + a separate "Partners" word (that mismatches the font and looks off).
  Deep-navy on light pages, white on deep-navy pages; size by height via `.b24-plogo` classes.
  ```html
  <!-- light partner page: header/footer -->
  <img class="b24-plogo b24-plogo--foot" src="bitrix24-logo/logo-partner-h.png" alt="Bitrix24 Partners">
  <!-- deep-navy cover / CTA -->
  <img class="b24-plogo b24-plogo--cover" src="bitrix24-logo/logo-partner-h-white.png" alt="Bitrix24 Partners">
  <!-- stacked, for a navy section-divider -->
  <img class="b24-plogo b24-plogo--v" src="bitrix24-logo/logo-partner-v-white.png" alt="Bitrix24 Partners">
  ```
  Sizes: `.b24-plogo--foot` (16px, running head/footer), `--cover` (32px), `--v` (120px, stacked).
  Keep clear space ≥ the clock-glyph height; never recolor, re-proportion, or distort the lockup.
  (These lockups are high-res raster from the official guide; the vector master is `logo-b24.ai`.)

---

## 10. Voice & content patterns

- **Benefit-first.** Lead with the business outcome, then the tools (the whole thesis of the
  Partners deck: "sell value, not features").
- **Structured problem→solution.** Business pain → Bitrix24 tools → Practical Outcome.
- **Confident, concise, professional.** Short sentences. Bold the phrase that matters; highlight
  one key idea per paragraph with `.b24-hl`.
- **Localizable.** Reference exists in EN and ES — keep copy translation-friendly; layouts must
  tolerate ~30% text expansion (don't hard-pack columns).

---

## 11. How to work with Claude (the workflow)

When you want a new document, tell Claude something like:

> "Using the Bitrix24 PDF design system in this folder, make a 5-page A4 guide:
> *Bitrix24 for Real Estate*. Cover + 2 challenge pages (pain→tools→outcome) + a value list
> with a quote + a closing CTA. Then export to PDF."

Claude should:
1. **Read** `DESIGN_SYSTEM.md` and open `bitrix24-template.html` for the exact markup.
2. **Create a new HTML file** that `<link>`s `bitrix24-kit.css`.
3. **Assemble pages** by copying component blocks and replacing the placeholder text; pick
   `.page` (Bitrix24) or `.page--sky` (Partners) per the sub-brand.
4. **Keep every value tokenized** — reuse classes/variables, add nothing off-palette.
5. **Render to PDF** with headless Chrome (see README) and visually check each page against
   this spec before delivering.

**Do / don't for Claude**
- ✅ Reuse components; ✅ keep one `.b24-display` (cover only); ✅ auto-number via `.b24-pageno`;
  ✅ verify contrast (white on navy, deep-blue on green).
- ✅ **"Become a Partner" is always** `.b24-btn` inside `.b24-btn-center`, linked to
  `https://partners.bitrix24.com/`, sized up (`--lg`/`--xl`) — never a plain pill.
- ✅ Keep the Partners logo **monochrome and balanced** ("Partners" = wordmark height).
- ❌ No raw hex/px outside the tokens; ❌ no new fonts; ❌ no full-width small text over photos;
  ❌ don't change `@page` size; ❌ don't mix the two sub-brand palettes on one page.

---

## 12. ★ Print gotcha — soft shadows become ugly grey boxes (handled automatically)

**Symptom:** a hard grey/green **rectangle** appears around a button (`.b24-btn`), tile
(`.b24-tile`), white card or table in the exported PDF.

**Root cause:** it is **not** a bug in your HTML or in Chrome. Chrome writes a *correct* soft
`box-shadow` into the PDF, but common viewers — **macOS Preview / Quick Look** — rasterize that
blurred shadow into a solid rectangle. This is insidious because programmatic rasterizers
(PyMuPDF/`fitz`, `pdftoppm`) render the shadow *correctly*, so **the box is invisible when you
verify with a screenshot and only shows up when the user opens the PDF in Preview.**

**Fix (already automatic):** `scripts/render.py` now injects a print-safe reset on every render
that strips `box-shadow` from all shadowed components (`.b24-btn`, `.b24-tile`, `.b24-card--white`,
`.b24-card--navy`, `.b24-table-wrap`, `.b24-compare`, `.b24-solve`, `.b24-quote`, pills/tags) and
restores container definition with a hairline `--b24-line` border. You get flat, print-clean
components with no boxes — **do nothing**.

**Rules for Claude:**
- ❌ **Never rely on `box-shadow` for depth** in a document meant for PDF. Do not add your own
  `box-shadow` — it will box in Preview even though your `fitz` check looks clean.
- ✅ To separate a surface, use a **hairline border** (`1px solid var(--b24-line)`), not a shadow.
- ✅ **Verifying is not enough with `fitz` alone for this class of bug** — `fitz` hides it. Trust
  the reset (shadows are removed at the source), and if you must confirm visually, open the PDF in
  Preview/Quick Look, not just a `fitz` rasterization.
- The one shadow that is safe is the cutout-people **`filter: drop-shadow`** (`.b24-cutout--shadow`)
  — that's a filter on a transparent PNG, not a box-shadow on a rectangle, so it renders fine.
