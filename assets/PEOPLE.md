# Industry People — cover & closing figures

Every Industry Guide shows people **on the cover** (one hero person) and **on the
closing "Key Value" page** (one or two people). They are the biggest visual cue
for *who the guide is for*, so they must **match the guide's industry** — and,
because we sell software, **each person always holds a device: a phone, a laptop,
or a tablet.**

This file is the feature that lets you swap those people per guide — by
**industry attire** (a construction guide → a worker in hi-vis/hard hat; a
medical guide → clinical staff in scrubs/coat), not only by ethnicity or pose.

---

## Where the people live in the layout

Both are `.b24-ig-figure` cutouts (transparent PNG) sitting on a dark plate:

- **Cover** — one person, child of the cover person-plate:
  `<img class="b24-ig-figure" src="bitrix24-images/people/<file>.png" style="bottom:0; height:806px;">`
- **Closing page** — one or two people, child of the closing band plate:
  `<img class="b24-ig-figure" src="bitrix24-images/people/<file>.png" style="bottom:0; height:840px;">`

Swapping a guide's people = changing those two `src` paths (and, if the new
cutout is framed differently, nudging `height`). Nothing else in the layout
changes. The plate + `bottom:0` guarantee the figure sits flush on the plate
(no gap) and is never clipped.

---

## Two ways to get an industry person

**1) Reuse the bundled library** (`bitrix24-images/people/*.png`) when a generic
business look is fine and you only need to pick ethnicity / gender / pose /
device. The curated set already holds a diverse mix holding laptops, tablets and
phones (e.g. `man-asian-suit.png`, `woman-laptop.png`, `man-tablet.png`,
`woman-headset.png`, `duo-team.png`). Good for office/CRM/sales/marketing guides.

**2) Generate an industry-specific cutout** when the industry needs distinctive
attire the library doesn't have (construction, medical, manufacturing, logistics,
hospitality, beauty, automotive, agriculture, …). Produce a **transparent-background
PNG** with the recipe below, save it to `bitrix24-images/people/` under a clear
name (e.g. `construction-tablet.png`, `medical-duo.png`), then point the figure
`src` at it.

> If no image generator is available in the session, fall back to the closest
> library person and say so — never ship a mismatched or low-quality cutout.

---

## Generation recipe (transparent cutout that drops straight into the layout)

Use this prompt, filling the two blanks. Keep every other constraint — the CSS
positions the figure assuming this framing (head near the top, centered, feet/
lower body reaching the frame bottom, even lighting, **no background, no floor
shadow**).

> **Prompt template**
> "Photorealistic studio portrait of **{a friendly professional in {INDUSTRY
> ATTIRE}}**, three-quarter to full body, standing, facing the camera, warm
> natural smile, **holding a {DEVICE}** and looking at the camera. Front, even
> studio lighting. **Fully transparent background (cut-out, alpha channel), no
> backdrop, no floor, no shadow.** Centered, head near the top of the frame,
> body filling the frame down to the bottom edge. High resolution, sharp, clean
> edges. Vertical 4:5 framing."

- **{DEVICE}** is required and is always one of **a smartphone / a laptop / a
  tablet** — it signals "software." Vary it between the cover person and the
  closing people so the guide isn't repetitive.
- For the **closing page** you may generate **two** people (a small team): make it
  "two friendly professionals in {INDUSTRY ATTIRE}, standing side by side, each
  holding a {DEVICE}…" — same transparent-cutout constraints.
- Keep faces friendly, diverse across guides, front-lit. No logos/brands on the
  clothing. Neutral, real-looking attire (not costumes).

### Technical requirements for the PNG
- **Transparent** background (real alpha; corners fully transparent).
- **Portrait**, tall enough for the layout — at least ~1000 px wide, ~1300+ px tall.
- **Head near the top**, body **centered**, content continuing to the **bottom
  edge** (so `bottom:0` seats it on the plate with no gap).
- **No baked-in drop shadow** (the layout adds none either — the cutout sits
  directly on the plate).
- Save as `bitrix24-images/people/<industry>-<device>.png` (e.g.
  `logistics-phone.png`). After adding it, **re-render and eyeball** the cover /
  closing page; adjust the inline `height` (and, if needed, `top`/`bottom`) so the
  head lands at the logo line (cover) and the people sit flush on the plate.

---

## Industry → attire → device (starting points)

Pick attire that reads instantly as the industry; rotate the device.

| Industry | Attire cue | Device |
|---|---|---|
| Construction & Remodeling | hard hat + hi-vis vest over a shirt | tablet |
| Medical / Clinics | scrubs or white coat, stethoscope | tablet or laptop |
| Manufacturing / Industrial | work coverall / safety vest, safety glasses | tablet |
| Logistics / Delivery | branded-neutral polo or courier jacket | smartphone |
| Retail / E-commerce | smart-casual store staff, apron optional | tablet |
| Hospitality / Restaurants | chef whites or host attire | tablet |
| Beauty / Salons | stylist's apron / smock | smartphone |
| Automotive / Service | mechanic's coverall or service polo | tablet |
| Education | smart-casual teacher | laptop |
| Real Estate | business-smart blazer | smartphone |
| Finance / Legal / Professional | business suit | laptop |
| Agriculture | field jacket / cap | smartphone |
| IT / Tech | smart-casual, hoodie or shirt | laptop |

(Not exhaustive — infer sensible attire for any industry, always keep a device.)

---

## How to ask for it

When building a guide, just state the industry and (optionally) the look, e.g.:

- *"Industrial guide — put a worker in a hard hat and hi-vis holding a tablet on
  the cover, and two workers on the last page."*
- *"Medical guide — clinician in scrubs with a tablet on the cover; two clinical
  staff on the closing page."*

Claude picks or generates the cutouts per this file, drops them into
`bitrix24-images/people/`, wires the two `src` paths, and re-renders.
