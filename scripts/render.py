#!/usr/bin/env python3
"""
Render a Bitrix24 brand-content HTML file to its final asset.

  A4 (portrait / landscape) -> PDF
  Social (LinkedIn square / Instagram story) -> one PNG per slide

The script wires up the bundled design-system assets for you: it points the
document at assets/bitrix24-kit.css (fonts + logos resolve automatically via a
<base> tag) and injects the correct @page size for the chosen format. So the
HTML you author only needs the <section class="page ..."> blocks — no need to
worry about stylesheet paths or @page rules.

Usage:
  python3 render.py INPUT.html --format {a4,a4-land,li,story} [--out OUT] [--scale 2]

Examples:
  python3 render.py guide.html   --format a4         -> guide.pdf
  python3 render.py handout.html --format a4-land    -> handout.pdf
  python3 render.py carousel.html --format li        -> carousel-01.png, -02.png ...
  python3 render.py story.html   --format story --scale 2  -> story-01.png (2160x3840)
"""
import argparse, os, re, shutil, subprocess, sys, tempfile
from pathlib import Path

SKILL_ROOT = Path(__file__).resolve().parent.parent
ASSETS = SKILL_ROOT / "assets"
KIT = ASSETS / "bitrix24-kit.css"

# format -> (@page size, is_social)
# NOTE: use explicit dimensions for landscape. Some Chrome builds ignore the
# `size: A4 landscape` keyword and fall back to portrait, so the sheet must be
# given as explicit mm ("297mm 210mm") to guarantee landscape orientation.
FORMATS = {
    "a4":      ("A4 portrait",     False),
    "a4-land": ("297mm 210mm",     False),
    "li":      ("1080px 1080px",   True),
    "story":   ("1080px 1920px",   True),
}

def find_chrome():
    candidates = [
        "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome",
        "/Applications/Chromium.app/Contents/MacOS/Chromium",
        "/Applications/Microsoft Edge.app/Contents/MacOS/Microsoft Edge",
    ]
    for name in ("google-chrome", "google-chrome-stable", "chromium",
                 "chromium-browser", "microsoft-edge"):
        p = shutil.which(name)
        if p:
            candidates.insert(0, p)
    # Windows
    for p in (r"C:\Program Files\Google\Chrome\Application\chrome.exe",
              r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe"):
        candidates.append(p)
    for c in candidates:
        if c and Path(c).exists():
            return c
    sys.exit("ERROR: Chrome/Chromium not found. Install Google Chrome, or set it on PATH.")

def prepare_html(src_html: str, page_size: str) -> str:
    """Inject <base> (so assets resolve), the kit stylesheet if absent, and @page."""
    base_href = ASSETS.as_uri() + "/"
    inject = f'<base href="{base_href}">\n'
    if "bitrix24-kit.css" not in src_html:
        inject += '<link rel="stylesheet" href="bitrix24-kit.css">\n'
    inject += f'<style>@page {{ size: {page_size}; margin: 0; }} @media screen{{body{{padding:0}}}}</style>\n'

    # Print-safe shadow reset. A soft CSS box-shadow is rasterized into a HARD GREY
    # RECTANGLE by common PDF viewers (macOS Preview / Quick Look) — an ugly box
    # around buttons, tiles, cards and tables. (Chrome writes a correct shadow and
    # renderers like PyMuPDF show it fine, which is why it hides during verification
    # and only appears when the user opens the PDF.) So we strip component shadows in
    # every rendered output and preserve container definition with a hairline border.
    # !important makes this win regardless of stylesheet order. See DESIGN_SYSTEM.md.
    inject += (
        '<style>'
        '.b24-btn,.b24-tile,.b24-tag,.b24-pill,.b24-card,.b24-card--white,'
        '.b24-card--navy,.b24-table-wrap,.b24-compare,.b24-solve,.b24-quote'
        '{box-shadow:none !important}'
        '.b24-card--white,.b24-table-wrap{border:1px solid var(--b24-line) !important}'
        '</style>\n'
    )

    if re.search(r"<head[^>]*>", src_html, re.I):
        return re.sub(r"(<head[^>]*>)", r"\1\n" + inject, src_html, count=1, flags=re.I)
    if re.search(r"<html[^>]*>", src_html, re.I):
        return re.sub(r"(<html[^>]*>)", r"\1<head>" + inject + "</head>", src_html, count=1, flags=re.I)
    return "<head>" + inject + "</head>" + src_html

def to_pdf(chrome: str, html_path: Path, pdf_path: Path):
    cmd = [chrome, "--headless=new", "--disable-gpu", "--no-pdf-header-footer",
           f"--print-to-pdf={pdf_path}", html_path.as_uri()]
    r = subprocess.run(cmd, capture_output=True, text=True)
    if not pdf_path.exists():
        # some Chrome builds need the old headless flag
        cmd[1] = "--headless"
        subprocess.run(cmd, capture_output=True, text=True)
    if not pdf_path.exists():
        sys.exit(f"ERROR: Chrome failed to produce a PDF.\n{r.stderr[:800]}")

def rasterize(pdf_path: Path, out_prefix: Path, scale: int):
    """One PNG per PDF page. Try PyMuPDF, then pdftoppm, then sips (page 1 only)."""
    dpi = 96 * scale
    # 1) PyMuPDF
    try:
        import fitz
        doc = fitz.open(pdf_path)
        outs = []
        for i in range(doc.page_count):
            png = out_prefix.parent / f"{out_prefix.name}-{i+1:02d}.png"
            doc[i].get_pixmap(dpi=dpi).save(png)
            outs.append(png)
        return outs
    except ImportError:
        pass
    # 2) pdftoppm (poppler)
    if shutil.which("pdftoppm"):
        subprocess.run(["pdftoppm", "-png", "-r", str(dpi), str(pdf_path),
                        str(out_prefix)], check=True)
        return sorted(out_prefix.parent.glob(f"{out_prefix.name}-*.png"))
    # 3) sips (macOS, first page only)
    if shutil.which("sips"):
        png = out_prefix.parent / f"{out_prefix.name}-01.png"
        subprocess.run(["sips", "-s", "format", "png", str(pdf_path), "--out",
                        str(png)], capture_output=True)
        if png.exists():
            print("WARNING: only sips available — exported page 1 only. "
                  "Install PyMuPDF (pip install pymupdf) or poppler for multi-slide.")
            return [png]
    sys.exit("ERROR: need PyMuPDF (pip install pymupdf) or poppler (pdftoppm) "
             "to rasterize social slides to PNG.")

def main():
    ap = argparse.ArgumentParser(description="Render Bitrix24 brand-content HTML.")
    ap.add_argument("input", help="Input HTML file")
    ap.add_argument("--format", required=True, choices=list(FORMATS))
    ap.add_argument("--out", help="Output path (PDF) or PNG prefix. Default: alongside input.")
    ap.add_argument("--scale", type=int, default=2, help="PNG scale for social (1=1080px, 2=2160px). Default 2.")
    args = ap.parse_args()

    if not KIT.exists():
        sys.exit(f"ERROR: bundled kit not found at {KIT}")
    src = Path(args.input)
    if not src.exists():
        sys.exit(f"ERROR: input not found: {src}")

    page_size, is_social = FORMATS[args.format]
    chrome = find_chrome()
    prepared = prepare_html(src.read_text(encoding="utf-8"), page_size)

    with tempfile.TemporaryDirectory() as td:
        tmp_html = Path(td) / "render.html"
        tmp_html.write_text(prepared, encoding="utf-8")
        tmp_pdf = Path(td) / "render.pdf"
        to_pdf(chrome, tmp_html, tmp_pdf)

        if is_social:
            prefix = Path(args.out) if args.out else src.with_suffix("")
            outs = rasterize(tmp_pdf, prefix, args.scale)
            print("Rendered slides:")
            for o in outs:
                print(" ", o)
        else:
            out = Path(args.out) if args.out else src.with_suffix(".pdf")
            shutil.copyfile(tmp_pdf, out)
            print("Rendered PDF:", out)

if __name__ == "__main__":
    main()
