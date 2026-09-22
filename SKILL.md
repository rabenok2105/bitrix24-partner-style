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
- **`linkedin-banner-template.html`** — living reference for the **LinkedIn
  banner** direction (the `li-land` format): four 1200×628 single-image creatives
  (cover/hook, 3D-icon hero, numbered cards, light close). Copy a banner and swap
  the copy. See §"LinkedIn — carousels, posts and banners" below.
- **`battle-card-template.html`** — living reference for the **Battle Cards**
  direction: a multi-page A4 **PDF** that positions Bitrix24 against ONE competitor
  (cover → pros/cons → advantages/positioning prose → PRICING → a multi-page
  FEATURES matrix). Competitor-agnostic — filled via `{{COMPETITOR}}` / `{{Competitor}}`
  placeholders plus a per-file competitor-logo slot; the bundled example is filled
  with ZOHO. See §"Battle Cards" below.
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
| **Battle Cards / Батлкарта** (Bitrix24 vs a competitor) | `a4` | 210×297 mm | `.bc-sheet` | multi-page PDF |
| LinkedIn carousel / gallery | `li` | 1080×1080 | `.page--li` | one PNG per slide |
| **LinkedIn banner** (single-image post / ad) | `li-land` | 1200×628 | `.page--li-land` | one PNG per banner |
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

### Battle Cards · «Батлкарта» (competitive comparison PDF)

**Registered template — "Battle Cards".** A multi-page A4 PDF that positions
Bitrix24 against ONE competitor: cover → **page 2**: competitor snapshot
(launch year / local-or-international), pros/cons vs Bitrix24 advantages, and —
directly **under** that block — the **"Bitrix24 vs. <competitor>" snapshot table**
(Built for / Core idea / Business model) → **page 3**: Bitrix24 advantages overview,
competitor positioning (prose), and the **"Pricing model"** comparison table (Pricing
model / User logic / Plan scaling) → **one PRICING page** carrying all three plan blocks
stacked — **If billed monthly**, **If billed annually**, **Free plan** (each = competitor
note card + Bitrix24 plan card) → competitor "pricing / Example cases" → a multi-page
FEATURES matrix (feature-category tables with solid-navy circle-check / grey
circle-minus icons) → **closing section** on the last page: the **"Bitrix24 Cowork"**
highlight card and a **"Conclusion"** paragraph, above the navy footer logo.

**★ Fill free space with the next table.** A FEATURES page must not sit half-empty:
if a page has room after its tables, pull the next category's table up onto it (e.g.
Telephony + Reports and analytics + Customer & External User Engagement share one page)
rather than leaving a big blank area with that table alone on the following page. Pack
each page as full as it fits (checking the no-clip rule), and only start a new page when
the next table genuinely won't fit.

**★ Bitrix24 Cowork = white card, no border.** The "Bitrix24 Cowork" block is a
**plain white card with NO border** (white fill, rounded corners, 15 px inner padding):
navy title on the left, a **navy "Coming soon" pill on the right** (navy-gradient fill,
white text, **no shadow**), and the body note in brand navy `#063883`. The "Conclusion" paragraph is a plain navy heading + body text in brand navy
`#063883` (not muted). The competitor-positioning paragraphs on page 3 are also brand
navy `#063883`, not a muted grey-blue.

**★ Tables share one content width.** Every table is laid out at the same content width
(≈ 562 px at Figma scale) — the FEATURES matrix, the pricing "Example cases" module
tables and the Vibe+ tables all stretch to that width, not a narrower one. Module-table
rows use the same row height / vertical padding, **body text size (≈10px, regular)** and
**grey header style (≈14px, 600)** as the rest of the document's tables, so they read as
one organic system — no smaller/denser one-off table. Module names and prices are all
regular weight. The bottom price band keeps just **two** text styles (avoid a zoo of
sizes/weights): a **muted label** (≈8.5px, `#7089A6`) for the parenthetical note and the
"Price if billed …" captions, and one **bold-navy key value** (≈12px, 700, `#063883`)
shared by `Users: N` and every price figure. Vibe+ tables follow the document scale:
10px regular body text, bold plan names, gradient header bar.

**★ Reproduce the source doc in full — no paraphrasing away detail.** Every text
unit from the partner's Word doc goes into the PDF verbatim (feature tier tags like
"All paid plans (CoPilot); unlimited AI from Standard Vibe+ (coming soon)", the full
"…priced at €6 excluding VAT" wording, the Cowork + Conclusion sections). Do NOT
abbreviate ("Mon–Fri" for "Monday to Friday") or drop parentheticals. After building,
run the automated coverage check (every docx paragraph + table cell must appear in the
rendered PDF text) and treat only icon/split-cell/hyphenation differences as expected.
Living reference: `battle-card-template.html` (`--format a4`), built
pixel-for-pixel from the Figma "Battle Cards" design. This is an **internal /
sales-enablement** piece — every cover carries the **"Internal use ONLY"** tag.

**The template is competitor-agnostic — fill it per competitor via placeholders:**
- `{{COMPETITOR}}` — competitor name in HEADINGS and table column headers
  (upper-case, e.g. `ZOHO`). Find & Replace.
- `{{Competitor}}` — competitor name in prose / sentences (e.g. `Zoho`). Find & Replace.
- Competitor **logo** on pages 1–2 — a `.logo-slot` placeholder; the partner
  attaches the logo per file (it changes; Bitrix24's own logo stays).
Everything else (launch year, pros/cons, prices, feature rows) is **example
content (ZOHO)** — overwrite it with the real competitor's data.

**★ Table system — keep it identical across the whole file.** Competitor &
Bitrix24 columns are **white cards with light row dividers and NO outer outline**;
the first (label) column is plain text with **white dividers aligned to the light
dividers** of the data columns; grey header = competitor, azure→navy **gradient**
header = Bitrix24; **all bold text is brand navy `#063883`**; row heights sync
across the three columns and cell content is **vertically centred**.

**★ One spacing system — everything on a 20 px rhythm.** Every gap between a heading
(page title, sub-title, "vs" / "Pricing model" heading, "If billed …", "Example cases")
and the table or content directly under it is **20 px**, and every gap between two large
logical blocks (table→next heading, table→table, section→section) is also **20 px**.
Cards carry a **15 px inner padding**. Do not leave odd one-off gaps (14/16/18/30) — after
building, verify the whole file reads on the same 20 px rhythm. Titles are Montserrat
SemiBold with **no extra letter-spacing**.

**★ Typography — restrained sizes, one uniform letter-spacing.** Keep the page/section
headings modest (page title ≈ 18px, sub-titles ≈ 15–18px) and table column headers
just slightly smaller than the body headline (feature-table header ≈ 14px, 3-column /
plan-card header ≈ 17px) so pages never look dense or shouty. **Letter-spacing is
`normal` everywhere** — never leave a stray `letter-spacing` value on one element while
others are default; uneven tracking across the document is a defect. Check the whole
file for inconsistent tracking before delivering.

**★ Cell alignment — icon + text goes left.** A comparison cell that holds BOTH an
icon (check / minus) AND text (a tier tag like "Basic Vibe+", or "Via integrations"
beside a minus) is **left-aligned**, not centred, so every such cell's text starts on
the same left edge within the column and reads as one clean list. Plain icon-only or
plain text-only cells stay centred.

**★ Vibe+ ⇒ recolour to the Vibe style.** Bitrix24 Vibe+ has its own look — a
**blue→purple→pink gradient** with a **single purple accent `#6B4FD8`** (use ONE
purple, never two shades). Wherever Vibe+ is the subject, switch that element from the
navy scheme to the Vibe scheme:
- **Dedicated Vibe+ tables** (Vibe+ plans, "what's new") — a card with a **gradient
  border** (`linear-gradient(100deg,#4F8FF2,#7C7BF0,#A87BE9,#E38DDA)`), a
  gradient-filled header, and `#6B4FD8` for every text accent (page title, column
  labels, values).
- **A feature table whose Bitrix24 column is all Vibe+** (e.g. "AI tools", "AI &
  no-code platform") — recolour only the Bitrix24 column: its **header uses the Vibe
  gradient** instead of navy, and its **check icons are purple** (the Vibe gradient).
  The competitor column and the rest of the page stay navy.
- If only one row/item is Vibe+, leave the column navy and keep the tier tag; recolour
  the whole column only when Vibe+ dominates it.

**★ Closing Bitrix24 logo — dark navy.** The Bitrix24 logo centred at the very
bottom of the **last page** (end of file) is rendered in **solid dark navy
`#063883`**, not the full-colour (blue/cyan) logo — a monochrome navy version of
the wordmark + clock (recolour every fill in `bitrix24-logo/logo.svg` to `#063883`,
e.g. `logo-navy.svg`). The **cover** Bitrix24 logo stays full colour; only the
closing footer logo is inked navy.

**★ Optional Vibe+ blocks — base form has none.** The **default / base** battle
card does **NOT** include the Bitrix24 Vibe+ page (the dedicated "Vibe+ plans" +
"what's new" spread) or any **gradient recolouring** on feature tables — plain navy
throughout. The Vibe+ blocks are an **opt-in add-on**: include the Vibe+ page and the
gradient Bitrix24-column recolour only when the file is meant to feature Vibe+
(build flag `BC_VIBE=1`). When Vibe+ is off, the "Vibe+ Launch Promo" note and the
Vibe pricing are omitted too.

**★ Muted-blue captions.** Footnotes / captions under tables (e.g. the Vibe+ promo
note) use the same **muted blue-grey `#8AA0BE`** as the other file captions, with any
bold lead-in in brand navy `#063883` — never a purple caption.

**★ Pricing example-cases page is OPTIONAL.** The "… pricing → Example cases" module
tables exist only when the competitor prices per-module (like MEFI CRM). Many competitors
have plain plan-based pricing and **no such page at all** — in that case omit the whole
"Example cases" page; do not invent module rows to fill it. Include it only when the
partner's source doc actually has a module price list. When present, it looks like:
two stacked 4-column module tables (`Modules | {{COMPETITOR}} | Modules | {{COMPETITOR}}`),
each closed by a **plain white** bottom band (no border) whose vertical divider
continues the grid after the first competitor column to split **Users (left)** from
**prices (right)**. In the Users block the **parenthetical note sits on top and
`Users: N` (bold navy) below it**; prices are two stacked labels — "Price if billed
monthly / €…/month" and "Price if billed annually / €…/year". The gap between the
"Example cases" sub-title and the first table matches the subtitle→table spacing on
the pricing pages above (14 px), so the pages read consistently.

**★ Never let a page clip.** A4 pages are fixed-height — after every render look
at each page and confirm no table or text runs past the bottom edge; split or
compact rather than overflow. The only elements meant to sit at the very edge are
the cover's "Internal use ONLY" tag and the closing Bitrix24 logo.

**★ Final source check.** Before delivering, verify the PDF against the partner's
source doc: every table present, every feature row (label + competitor/Bitrix24
value) and every price carried over with nothing dropped or invented.

**★ Process — build the .COM version first, then localize.** When a partner asks
for a Battle Card **with localization**, do NOT jump straight to the localized file:
1. **International (.COM / English) first.** Say up front that you'll produce the
   **.COM (English) battle card** and get it **approved**. The partner sends the
   English copy; you review it, apply any fixes it needs, and lock that version.
2. **Ask before localizing.** Once the .COM version is approved, **ask** whether to
   start localization and **request all the texts** you need for that language —
   don't translate on your own initiative.
3. **Localize on the approved .COM template.** Produce the localized version from
   the SAME signed-off template, swapping in only the partner's supplied texts —
   keep the layout and styles unchanged.
4. **New block or table → confirm.** If a localization needs an extra block or a new
   table, add it, then **show the partner and ask whether it should look that way /
   whether everything is good** before finalizing.

### LinkedIn — carousels, posts and banners

Three different things, and picking the wrong one is the usual mistake:

| | Canvas | Format | What it is |
|---|---|---|---|
| **Carousel / gallery** | 1080×1080 | `li` | a SERIES of square slides, swiped in the feed |
| **Post series** | 1080×1350 | `post` | a SERIES of 4:5 slides (the Success Story posts) |
| **Banner** | 1200×628 | `li-land` | ONE landscape creative — a single-image post or ad |

**★ Landscape is NOT a carousel slide.** LinkedIn document carousels render square
or portrait and **crop** landscape artwork. Use `li-land` only for a single-image
post / ad creative; for a swipeable series use `li` or `post`. Living reference:
`linkedin-banner-template.html` (`--format li-land`).

**★ The banner composition is a SPLIT.** `.b24-bnr-split` — copy on the LEFT, exactly
**ONE** dominant visual anchor on the RIGHT (cutout person, one 3D icon, a UI mock-up,
a price card). `.b24-bnr-split--flip` mirrors it; keep one direction across a series.
Optional `.b24-bnr-panel` puts a soft panel behind the object — place the object
inside it with breathing room, never touching the edges.

**★ Never pin the text mass to an edge.** `.page--li-land` centres its content
vertically on purpose. A banner whose copy sits on the bottom (or top) edge with a
void opposite it is a defect — rebalance instead.

**★ One idea per creative, one hero object.** Do not stack two 3D elements, and do
not let decorative accents (tetris, stars) compete with the hero — they stay
secondary. On a cover, prefer exactly one 3D object.

**★ Series rules (carousel or banner set).** Default to **5–7 slides** unless the
user asks otherwise; each slide carries ONE takeaway. Repeat the structural
elements — logo position, the `.b24-bnr-strip` takeaway line, the corner badge — so
separate creatives read as one campaign rather than unrelated banners. Use
headlines, bullets and cards instead of paragraphs; contrast is intentional (dark
shell, light content cards, lime emphasis via `--b24-lime`).

**★ Slide patterns** that work on these canvases: cover/hook, table or comparison
(2–3 columns, strict grid, skimmable cells), checklist or process step (3–5 bullets,
optional step badge top-right), **numbered cards** (`.b24-bnr-cards` — 2–3 cards;
three is the ceiling at 628px), educational split (one side explains, the other
holds one illustrative object), light CTA/summary (a pale sheet reads as a cleaner
ending after several dark ones), closing CTA (back to cover logic + a bright CTA
block, cleaner than the middle slides).

**★ Default outline** when the user gives no slide-by-slide plan: hook / promise →
context or problem → examples, segmentation or comparison → process or
recommendation → CTA. Expand to 6–7 only when the topic needs the room, and vary
the middle (table / numbered cards / checklist / split) instead of repeating one
block. Assets come from the kit — `bitrix24-images/people/`, `3d-icons/`,
`bitrix24-logo/` — never invent a new social style.

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
