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
| LinkedIn square | `.page--li` | 1080 × 1080 px | PNG per slide |
| Instagram Story | `.page--story` | 1080 × 1920 px | PNG per slide |

- **Social = one `.page` per slide.** Render each slide with `@page { size: 1080px 1080px; margin:0 }`
  (story: `1080px 1920px`) to a 1-page PDF, then rasterize that page to **PNG** (one image per slide).
  For carousels, keep one slide per HTML file so each exports to its own image cleanly.
- **Instagram safe-zone:** wrap story content in `<div class="b24-safe">…</div>` — it insets the
  top/bottom ~240 px that Instagram overlays with the avatar (top) and reply/CTA bar (bottom).
- **Runhead / footer / page numbers** are for multi-page A4 (PDF); social slides normally use just
  a logo (and an optional slide counter), no running header.
- Social slides skip A4 mm padding and use their own px padding; drop in `.b24-plogo--cover`
  (44 px on social) for the logo. Everything else — colors, pills, buttons, tetris, stars — is shared.

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

- **Brand icons** (from the Figma *Icons* set) live in **`bitrix24-images/icons/`** — clean
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
