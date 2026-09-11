#!/usr/bin/env python3
"""
Render a Bitrix24 brand-content HTML file to its final asset.

  A4 (portrait / landscape) -> PDF
  Industry Guide (1080x1350 vertical) -> one multi-page PDF
  Success Story (A4) -> one multi-page PDF ; (posts) -> one JPEG per post
  Social (LinkedIn square / portrait post / Instagram story) -> one image per slide

The script wires up the bundled design-system assets for you: it points the
document at assets/bitrix24-kit.css (fonts + logos resolve automatically via a
<base> tag) and injects the correct @page size for the chosen format. So the
HTML you author only needs the <section class="page ..."> blocks — no need to
worry about stylesheet paths or @page rules.

Usage:
  python3 render.py INPUT.html --format {a4,a4-land,guide,li,post,story} [--out OUT] [--scale 2] [--jpeg|--png]

Examples:
  python3 render.py guide.html   --format a4         -> guide.pdf
  python3 render.py handout.html --format a4-land    -> handout.pdf
  python3 render.py industry.html --format guide     -> industry.pdf (multi-page 1080x1350)
  python3 render.py carousel.html --format li        -> carousel-01.png, -02.png ...
  python3 render.py posts.html   --format post       -> posts-01.jpg, -02.jpg ... (1080x1350)
  python3 render.py story.html   --format story --scale 2  -> story-01.png (2160x3840)

Output image type for the social formats: PNG by default, EXCEPT `post`, which
defaults to JPEG (the Success Story LinkedIn series ships as JPEGs). Force either
with --jpeg / --png. A4 / guide always export PDF; --jpeg/--png are ignored there.
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
    "guide":   ("1080px 1350px",   False),   # Industry Guide — multi-page vertical PDF
    "li":      ("1080px 1080px",   True),
    "post":    ("1080px 1350px",   True),    # Success Story LinkedIn/JPEG post series (4:5)
    "story":   ("1080px 1920px",   True),
}

# Social formats whose default output image type is JPEG (others default to PNG).
JPEG_DEFAULT = {"post"}

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
    """Inject <base> + the kit stylesheet (early), and @page + shadow reset (late).

    The @page rule and shadow reset are injected right before </head> so they land
    AFTER any stylesheet the document links itself (including bitrix24-kit.css,
    which carries a default `@page { size: A4 }`). Later same-specificity rules
    win, so the chosen format's page size always overrides the kit default — even
    when the document self-links the kit (e.g. the living templates)."""
    base_href = ASSETS.as_uri() + "/"
    # --- early: <base> so assets resolve, and the kit if the doc didn't link it ---
    head_open = f'<base href="{base_href}">\n'
    if "bitrix24-kit.css" not in src_html:
        head_open += '<link rel="stylesheet" href="bitrix24-kit.css">\n'

    # --- late: @page size for the chosen format, then the print-safe shadow reset ---
    head_close = f'<style>@page {{ size: {page_size}; margin: 0; }} @media screen{{body{{padding:0}}}}</style>\n'
    # Print-safe shadow reset. A soft CSS box-shadow is rasterized into a HARD GREY
    # RECTANGLE by common PDF viewers (macOS Preview / Quick Look) — an ugly box
    # around buttons, tiles, cards and tables. (Chrome writes a correct shadow and
    # renderers like PyMuPDF show it fine, which is why it hides during verification
    # and only appears when the user opens the PDF.) So we strip component shadows in
    # every rendered output and preserve container definition with a hairline border.
    # !important makes this win regardless of stylesheet order. See DESIGN_SYSTEM.md.
    head_close += (
        '<style>'
        '.b24-btn,.b24-tile,.b24-tag,.b24-pill,.b24-card,.b24-card--white,'
        '.b24-card--navy,.b24-table-wrap,.b24-compare,.b24-solve,.b24-quote'
        '{box-shadow:none !important}'
        '.b24-card--white,.b24-table-wrap{border:1px solid var(--b24-line) !important}'
        '</style>\n'
    )

    if re.search(r"<head[^>]*>", src_html, re.I):
        out = re.sub(r"(<head[^>]*>)", r"\1\n" + head_open, src_html, count=1, flags=re.I)
        if re.search(r"</head>", out, re.I):
            return re.sub(r"(</head>)", head_close + r"\1", out, count=1, flags=re.I)
        return out + head_close
    if re.search(r"<html[^>]*>", src_html, re.I):
        return re.sub(r"(<html[^>]*>)", r"\1<head>" + head_open + head_close + "</head>",
                      src_html, count=1, flags=re.I)
    return "<head>" + head_open + head_close + "</head>" + src_html

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

def rasterize(pdf_path: Path, out_prefix: Path, scale: int, ext: str = "png", quality: int = 92):
    """One image per PDF page. Try PyMuPDF, then pdftoppm, then sips (page 1 only).

    ext is "png" or "jpg". JPEG has no alpha, so pages are flattened onto white
    (social slides are opaque anyway) and written at `quality`."""
    dpi = 96 * scale
    ext = "jpg" if ext.lower() in ("jpg", "jpeg") else "png"
    # 1) PyMuPDF (rendered via a white-backed pixmap, then saved through Pillow so
    #    JPEG quality is controllable and alpha is flattened predictably).
    try:
        import fitz
        doc = fitz.open(pdf_path)
        outs = []
        for i in range(doc.page_count):
            out = out_prefix.parent / f"{out_prefix.name}-{i+1:02d}.{ext}"
            pix = doc[i].get_pixmap(dpi=dpi, alpha=False)
            try:
                from PIL import Image
                img = Image.frombytes("RGB", (pix.width, pix.height), pix.samples)
                if ext == "jpg":
                    img.save(out, "JPEG", quality=quality, subsampling=0, optimize=True)
                else:
                    img.save(out, "PNG")
            except ImportError:
                pix.save(out)   # Pillow absent: let PyMuPDF write by extension
            outs.append(out)
        return outs
    except ImportError:
        pass
    # 2) pdftoppm (poppler)
    if shutil.which("pdftoppm"):
        flag = "-jpeg" if ext == "jpg" else "-png"
        subprocess.run(["pdftoppm", flag, "-r", str(dpi), str(pdf_path),
                        str(out_prefix)], check=True)
        got = sorted(out_prefix.parent.glob(f"{out_prefix.name}-*"))
        return got
    # 3) sips (macOS, first page only)
    if shutil.which("sips"):
        fmt = "jpeg" if ext == "jpg" else "png"
        out = out_prefix.parent / f"{out_prefix.name}-01.{ext}"
        subprocess.run(["sips", "-s", "format", fmt, str(pdf_path), "--out",
                        str(out)], capture_output=True)
        if out.exists():
            print("WARNING: only sips available — exported page 1 only. "
                  "Install PyMuPDF (pip install pymupdf) or poppler for multi-slide.")
            return [out]
    sys.exit("ERROR: need PyMuPDF (pip install pymupdf) or poppler (pdftoppm) "
             "to rasterize social slides to images.")

def main():
    ap = argparse.ArgumentParser(description="Render Bitrix24 brand-content HTML.")
    ap.add_argument("input", help="Input HTML file")
    ap.add_argument("--format", required=True, choices=list(FORMATS))
    ap.add_argument("--out", help="Output path (PDF) or PNG prefix. Default: alongside input.")
    ap.add_argument("--scale", type=int, default=2, help="Image scale for social (1=1080px, 2=2160px). Default 2.")
    ap.add_argument("--jpeg", action="store_true", help="Force JPEG output for a social format.")
    ap.add_argument("--png",  action="store_true", help="Force PNG output for a social format.")
    ap.add_argument("--quality", type=int, default=92, help="JPEG quality (1-100). Default 92.")
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
            # Choose image type: explicit flag wins, else JPEG for `post`, else PNG.
            if args.jpeg and args.png:
                sys.exit("ERROR: pass only one of --jpeg / --png.")
            ext = "jpg" if args.jpeg else "png" if args.png \
                  else ("jpg" if args.format in JPEG_DEFAULT else "png")
            prefix = Path(args.out) if args.out else src.with_suffix("")
            outs = rasterize(tmp_pdf, prefix, args.scale, ext=ext, quality=args.quality)
            print("Rendered slides:")
            for o in outs:
                print(" ", o)
        else:
            out = Path(args.out) if args.out else src.with_suffix(".pdf")
            shutil.copyfile(tmp_pdf, out)
            print("Rendered PDF:", out)

if __name__ == "__main__":
    main()
