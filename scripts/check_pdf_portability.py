#!/usr/bin/env python3
"""
Check that a rendered PDF will look THE SAME in every PDF viewer.

Chrome (Skia) writes some CSS effects into the PDF with constructs that only
Chrome's own viewer (PDFium) draws correctly. macOS Preview / Quick Look,
Safari (Apple PDFKit), PDFgear, many mail/phone previewers and some print RIPs
draw them wrong — a gradient collapses into one flat colour, gradient text is
cropped or disappears, soft shadows become grey boxes.

This script lists every such construct per page and exits non-zero when any is
found, so a PDF that would look different outside Chrome never ships.

  python3 scripts/check_pdf_portability.py out.pdf            # report + exit code
  python3 scripts/check_pdf_portability.py out.pdf --quiet    # exit code only

Portable (allowed): text, vector paths, solid fills, images (with or without an
alpha mask), plain opacity. Not portable (flagged):
  - any smooth shading (gradient) — ShadingType 1-7, via `sh` or a Pattern
  - tiling patterns (PatternType 1) — Skia uses them for background-clip:text
  - PostScript-calculator functions (FunctionType 4)
  - luminosity soft masks (CSS mask-image / some filters)
  - blend modes other than Normal (CSS mix-blend-mode)
render.py flattens CSS gradients into images before printing, so a PDF made by
render.py passes; a failure means the HTML uses an effect the flattener does not
cover (see "PDF portability" in SKILL.md).

Needs pikepdf (pip install pikepdf).
"""
import sys
from collections import Counter

try:
    import pikepdf
except ImportError:
    sys.exit("ERROR: pip install pikepdf")


def _walk_resources(res, found, seen):
    if not isinstance(res, pikepdf.Dictionary):
        return
    key = res.objgen
    if key != (0, 0):
        if key in seen:
            return
        seen.add(key)
    for sh in (res.get("/Shading") or {}).values() if isinstance(res.get("/Shading"), pikepdf.Dictionary) else []:
        found[f"gradient (ShadingType {int(sh.get('/ShadingType', 0))})"] += 1
    pats = res.get("/Pattern")
    if isinstance(pats, pikepdf.Dictionary):
        for p in pats.values():
            pt = int(p.get("/PatternType", 0))
            if pt == 1:
                found["tiling pattern (gradient text / repeated fill)"] += 1
                _walk_resources(p.get("/Resources"), found, seen)
            elif pt == 2:
                sh = p.get("/Shading")
                st = int(sh.get("/ShadingType", 0)) if sh is not None else 0
                found[f"gradient (ShadingType {st})"] += 1
                _walk_funcs(sh, found)
    gs = res.get("/ExtGState")
    if isinstance(gs, pikepdf.Dictionary):
        for g in gs.values():
            bm = g.get("/BM")
            if bm is not None and str(bm) not in ("/Normal", "/Compatible"):
                found[f"blend mode {bm}"] += 1
            sm = g.get("/SMask")
            if isinstance(sm, pikepdf.Dictionary):
                if str(sm.get("/S")) == "/Luminosity":
                    found["luminosity soft mask (mask-image / filter)"] += 1
                _walk_resources((sm.get("/G") or {}).get("/Resources") if sm.get("/G") is not None else None, found, seen)
    xo = res.get("/XObject")
    if isinstance(xo, pikepdf.Dictionary):
        for x in xo.values():
            if str(x.get("/Subtype")) == "/Form":
                _walk_resources(x.get("/Resources"), found, seen)


def _walk_funcs(obj, found):
    if obj is None:
        return
    f = obj.get("/Function") if isinstance(obj, (pikepdf.Dictionary, pikepdf.Stream)) else None
    fs = f if isinstance(f, pikepdf.Array) else [f] if f is not None else []
    for fn in fs:
        if int(fn.get("/FunctionType", -1)) == 4:
            found["PostScript function (FunctionType 4)"] += 1
        for sub in fn.get("/Functions", []) or []:
            if int(sub.get("/FunctionType", -1)) == 4:
                found["PostScript function (FunctionType 4)"] += 1


def audit(path):
    pdf = pikepdf.open(path)
    report = {}
    for i, page in enumerate(pdf.pages, 1):
        found = Counter()
        _walk_resources(page.obj.get("/Resources"), found, set())
        if found:
            report[i] = found
    return report


def main():
    if len(sys.argv) < 2:
        sys.exit(__doc__)
    path = sys.argv[1]
    quiet = "--quiet" in sys.argv
    report = audit(path)
    if not report:
        if not quiet:
            print(f"OK: {path} — no viewer-dependent constructs; renders the same everywhere.")
        return 0
    if not quiet:
        print(f"NOT PORTABLE: {path} will look different outside Chrome:")
        for page, found in report.items():
            items = ", ".join(f"{k} ×{v}" for k, v in sorted(found.items()))
            print(f"  page {page}: {items}")
    return 1


if __name__ == "__main__":
    sys.exit(main())
