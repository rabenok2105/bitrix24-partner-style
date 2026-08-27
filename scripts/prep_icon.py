#!/usr/bin/env python3
"""
Normalise a Figma-exported Bitrix24 icon SVG into the two brand twins used by the
kit: a deep-navy version (`<name>.svg`) and a white version (`<name>-white.svg`).

The Bitrix24 "Common" icon library exports each 24×24 icon with a solid brand-green
fill (#15C674) plus a grey/white background rect from the Figma canvas. This script
strips those background rects and recolours every icon fill to the target colour, so
the result is a clean, single-colour 24×24 SVG that tints correctly:
  • white  → on the navy app tiles / any dark surface  (use the -white twin)
  • navy   → inline on light pages                     (use the plain twin)

Usage:
  python3 scripts/prep_icon.py RAW_EXPORT.svg NAME [--dir OUTDIR]
  # writes OUTDIR/NAME.svg (navy) and OUTDIR/NAME-white.svg (white)

Colours follow the design system: navy = #01447B (matches guide headings / tiles).
"""
import re, sys, os, argparse

NAVY = "#01447B"     # design-system deep navy (guide headings / tile base)
WHITE = "#FFFFFF"
# Figma canvas backdrop fills to drop (not part of the icon)
BG_FILLS = {"#ECECEC", "#FFFFFF", "#FFF", "#F5F5F5", "#E5E5E5"}

def clean(svg: str, color: str) -> str:
    # 1) drop full-canvas background rects (the #ECECEC cell bg + the big white
    #    overlay rect Figma adds). Match <rect ...fill="#ECECEC".../> and the
    #    translated backdrop rect.
    svg = re.sub(r'<rect\b[^>]*\bfill="#ECECEC"[^>]*/>', '', svg, flags=re.I)
    svg = re.sub(r'<rect\b[^>]*fill-opacity="0\.5"[^>]*/>', '', svg, flags=re.I)
    svg = re.sub(r'<rect\b[^>]*\bwidth="1185"[^>]*/>', '', svg, flags=re.I)
    # 2) recolour every remaining explicit fill (the icon) to the target colour.
    #    Leave fill="none" alone. Also recolour any stroke.
    def repl_fill(m):
        val = m.group(1)
        return f'fill="{color}"' if val.lower() != 'none' else m.group(0)
    svg = re.sub(r'fill="(#[0-9A-Fa-f]{3,8}|[a-zA-Z]+)"', repl_fill, svg)
    svg = re.sub(r'stroke="(#[0-9A-Fa-f]{3,8})"', f'stroke="{color}"', svg)
    # 3) tidy: ensure a 24×24 viewBox root; strip the Figma wrapper <g id="...">
    #    layers are fine to keep, but drop empty groups left by rect removal.
    svg = re.sub(r'<g[^>]*>\s*</g>', '', svg)
    return svg

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("src"); ap.add_argument("name")
    ap.add_argument("--dir", default=".")
    a = ap.parse_args()
    raw = open(a.src, encoding="utf-8").read()
    os.makedirs(a.dir, exist_ok=True)
    open(os.path.join(a.dir, f"{a.name}.svg"), "w", encoding="utf-8").write(clean(raw, NAVY))
    open(os.path.join(a.dir, f"{a.name}-white.svg"), "w", encoding="utf-8").write(clean(raw, WHITE))
    print(f"wrote {a.name}.svg (navy) + {a.name}-white.svg (white) in {a.dir}")

if __name__ == "__main__":
    main()
