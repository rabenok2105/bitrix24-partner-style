#!/usr/bin/env python3
"""
Prepare a Success Story COVER PHOTO from a raw headshot the partner sent in.

The partner drops a NORMAL photo — full colour, usually with a background,
unprocessed. On the cover the brand-navy tint is applied by CSS (the photo sits
over the navy gradient with `mix-blend-mode: overlay`, exactly like Figma), so
this script does NOT recolour the image. It just removes the background — a clean
cutout blends best — and cuts a small round AVATAR for the speaker card. You then
place `<img class="b24-ss-photo …">` and pick the framing that suits the photo
(--right / --top / --bottom / --wide); harmonious placement matters more than
copying one layout.

    python3 scripts/prep_cover_photo.py PHOTO.jpg --name askarasoft

writes, into assets/bitrix24-images/success-story/ (override with --outdir):
    speaker-<name>.png          full-colour cutout (transparent bg) — the overlay tints it
    speaker-<name>-avatar.png   square avatar (round it in CSS)

Options:
    --name NAME     slug used in the output filenames (default: photo stem)
    --outdir DIR    output directory (default: the skill's success-story assets)
    --keep-bg       DON'T remove the background — keep the whole colour frame
                    (the cover overlay still tints it and the edge-fade hides the
                    seam; use for photos whose backdrop should stay)
    --no-avatar     skip the avatar crop
    --duotone       ALSO bake a navy duotone into the cutout (legacy look, for
                    contexts without the CSS overlay). Not needed for the cover.
    --shadow HEX    duotone shadow colour   (default #04213F) — only with --duotone
    --highlight HEX duotone highlight colour (default #96C8F0) — only with --duotone
    --contrast N    duotone autocontrast cutoff %, 0-10 (default 1) — only with --duotone

Background removal uses `rembg` when available (best quality):
    pip install "rembg[cpu]" onnxruntime
Without rembg, pass --keep-bg (the overlay still works) or the script falls back
to a simple near-solid-background key that only works for plain/studio backdrops.
"""
import argparse, sys
from pathlib import Path

SKILL_ROOT = Path(__file__).resolve().parent.parent
DEFAULT_OUT = SKILL_ROOT / "assets" / "bitrix24-images" / "success-story"


def hex2rgb(h):
    h = h.lstrip("#")
    return tuple(int(h[i:i + 2], 16) for i in (0, 2, 4))


def remove_bg(img):
    """Return an RGBA cutout. Prefer rembg (u2net); else a light-background key."""
    try:
        import rembg
        from rembg import new_session
        try:
            sess = new_session("u2net")           # ~176 MB, downloaded once
        except Exception:
            sess = None
        return rembg.remove(img, session=sess) if sess else rembg.remove(img)
    except Exception as e:
        print(f"NOTE: rembg unavailable ({e.__class__.__name__}); using a simple "
              "light-background key. For clean cutouts install: pip install "
              '"rembg[cpu]" onnxruntime — or pass --keep-bg.', file=sys.stderr)
        return _key_light_bg(img)


def _key_light_bg(img):
    """Very rough fallback: make near-white/near-uniform corners transparent."""
    from PIL import Image
    im = img.convert("RGBA")
    px = im.load()
    w, h = im.size
    corners = [px[0, 0], px[w - 1, 0], px[0, h - 1], px[w - 1, h - 1]]
    br = sum(sum(c[:3]) for c in corners) / (3 * len(corners))
    if br < 180:                    # background isn't light — don't guess
        print("NOTE: background doesn't look light/plain; keeping it. Use rembg "
              "for a real cutout, or --keep-bg.", file=sys.stderr)
        return im
    bg = tuple(sum(c[i] for c in corners) // len(corners) for i in range(3))
    out = im.copy()
    op = out.load()
    for y in range(h):
        for x in range(w):
            r, g, b, a = px[x, y]
            if abs(r - bg[0]) + abs(g - bg[1]) + abs(b - bg[2]) < 60:
                op[x, y] = (r, g, b, 0)
    return out


def duotone(img, shadow, highlight, cutoff):
    """Map luminance -> shadow..highlight, preserving the source alpha."""
    from PIL import Image, ImageOps
    rgba = img.convert("RGBA")
    alpha = rgba.split()[3]
    gray = ImageOps.grayscale(rgba.convert("RGB"))
    gray = ImageOps.autocontrast(gray, cutoff=cutoff)
    mid = tuple((s + h) // 2 for s, h in zip(shadow, highlight))
    duo = ImageOps.colorize(gray, black=shadow, white=highlight, mid=mid).convert("RGBA")
    duo.putalpha(alpha)
    return duo


def make_avatar(img, size=240):
    """Square, face-biased crop for the round speaker avatar (CSS rounds it)."""
    from PIL import Image, ImageOps
    src = img.convert("RGBA")
    # bias the crop toward the top third (faces sit high in a headshot)
    return ImageOps.fit(src, (size, size), centering=(0.5, 0.32))


def main():
    ap = argparse.ArgumentParser(description="Prepare a Success Story cover photo.")
    ap.add_argument("photo", help="Raw photo the partner sent (jpg/png).")
    ap.add_argument("--name", help="Slug for output filenames (default: photo stem).")
    ap.add_argument("--outdir", default=str(DEFAULT_OUT))
    ap.add_argument("--keep-bg", action="store_true", help="Keep the background; don't cut out.")
    ap.add_argument("--no-avatar", action="store_true")
    ap.add_argument("--duotone", action="store_true", help="Bake a navy duotone (legacy; not needed for the cover).")
    ap.add_argument("--shadow", default="#04213F")
    ap.add_argument("--highlight", default="#96C8F0")
    ap.add_argument("--contrast", type=float, default=1)
    args = ap.parse_args()

    try:
        from PIL import Image
    except ImportError:
        sys.exit("ERROR: Pillow required (pip install pillow).")

    src = Path(args.photo)
    if not src.exists():
        sys.exit(f"ERROR: photo not found: {src}")
    name = args.name or src.stem.lower().replace(" ", "-")
    outdir = Path(args.outdir)
    outdir.mkdir(parents=True, exist_ok=True)

    raw = Image.open(src).convert("RGBA")
    cover = raw if args.keep_bg else remove_bg(raw)
    if args.duotone:   # legacy baked look; the cover normally tints via CSS overlay
        cover = duotone(cover, hex2rgb(args.shadow), hex2rgb(args.highlight), args.contrast)
    cover_path = outdir / f"speaker-{name}.png"
    cover.save(cover_path)
    print("Wrote", cover_path, "(duotone baked)" if args.duotone else "(full colour — tinted by the cover overlay)")

    if not args.no_avatar:
        av = make_avatar(raw)                       # avatar keeps natural colour
        av_path = outdir / f"speaker-{name}-avatar.png"
        av.save(av_path)
        print("Wrote", av_path)

    print("\nNext: reference it on the cover, e.g.\n"
          f'  <img class="b24-ss-photo b24-ss-photo--right" '
          f'src="bitrix24-images/success-story/speaker-{name}.png">\n'
          "Try --right / --top / --bottom / --wide and pick the best framing.")


if __name__ == "__main__":
    main()
