#!/usr/bin/env python3
"""
Print HTML to a PDF that looks THE SAME in every PDF viewer.

Why: Chrome (Skia) writes CSS gradients, gradient text (background-clip:text),
masks, blend modes, filters and SVG gradients into the PDF as smooth shadings,
tiling patterns and soft masks. Only Chrome's own viewer draws all of them
correctly; macOS Preview / Quick Look, Safari, PDFgear and many phone / mail
previewers show a flat dark colour instead of the gradient, crop gradient text,
or drop masked photos.

How: before printing, every element that uses one of those effects is painted
by Chrome itself into a high-resolution bitmap (Page.captureScreenshot of just
that element, on a transparent background) and the effect is swapped for that
bitmap. Text, vector shapes, solid fills and borders stay vector — only the
effect layer becomes an image, so it is pixel-identical to what Chrome shows
and every viewer draws it the same way.

Dependency-free: talks to Chrome over the DevTools protocol with a tiny stdlib
WebSocket client, so it needs nothing but Chrome/Chromium and Python 3.

Used by render.py for every PDF format. Standalone:
  python3 scripts/pdf_flatten.py prepared.html out.pdf --width 794 --height 1123
"""
import base64, json, os, re, shutil, socket, struct, subprocess, sys, tempfile, time
import urllib.request
from pathlib import Path

SCALE = float(os.environ.get("PDF_FLATTEN_SCALE", "3"))   # 3 = 288 dpi at 96 css px/in
TIMEOUT = int(os.environ.get("CHROME_TIMEOUT", "120"))


# --------------------------------------------------------------------------
# Minimal WebSocket client (RFC 6455) — enough for the DevTools protocol
# --------------------------------------------------------------------------
class _WS:
    def __init__(self, url):
        m = re.match(r"ws://([^/:]+):(\d+)(/.*)", url)
        host, port, path = m.group(1), int(m.group(2)), m.group(3)
        self.s = socket.create_connection((host, port), timeout=TIMEOUT)
        key = base64.b64encode(os.urandom(16)).decode()
        req = (f"GET {path} HTTP/1.1\r\nHost: {host}:{port}\r\nUpgrade: websocket\r\n"
               f"Connection: Upgrade\r\nSec-WebSocket-Key: {key}\r\n"
               "Sec-WebSocket-Version: 13\r\n\r\n")
        self.s.sendall(req.encode())
        resp = b""
        while b"\r\n\r\n" not in resp:
            chunk = self.s.recv(4096)
            if not chunk:
                raise ConnectionError("DevTools handshake failed")
            resp += chunk
        if b" 101 " not in resp.split(b"\r\n", 1)[0]:
            raise ConnectionError(resp.split(b"\r\n", 1)[0].decode(errors="replace"))
        self.buf = resp.split(b"\r\n\r\n", 1)[1]

    def _read(self, n):
        while len(self.buf) < n:
            chunk = self.s.recv(1 << 20)
            if not chunk:
                raise ConnectionError("DevTools connection closed")
            self.buf += chunk
        out, self.buf = self.buf[:n], self.buf[n:]
        return out

    def send(self, text):
        data = text.encode()
        hdr = bytearray([0x81])
        n = len(data)
        if n < 126:
            hdr.append(0x80 | n)
        elif n < 65536:
            hdr.append(0x80 | 126); hdr += struct.pack(">H", n)
        else:
            hdr.append(0x80 | 127); hdr += struct.pack(">Q", n)
        mask = os.urandom(4)
        hdr += mask
        self.s.sendall(bytes(hdr) + bytes(b ^ mask[i % 4] for i, b in enumerate(data)))

    def recv(self):
        parts = []
        while True:
            b0, b1 = self._read(2)
            op, n = b0 & 0x0F, b1 & 0x7F
            if n == 126:
                n = struct.unpack(">H", self._read(2))[0]
            elif n == 127:
                n = struct.unpack(">Q", self._read(8))[0]
            mask = self._read(4) if b1 & 0x80 else None
            payload = self._read(n)
            if mask:
                payload = bytes(b ^ mask[i % 4] for i, b in enumerate(payload))
            if op == 0x9:          # ping -> ignore (Chrome does not require pong)
                continue
            if op == 0x8:
                raise ConnectionError("DevTools closed the socket")
            parts.append(payload)
            if b0 & 0x80:
                return b"".join(parts).decode()


class _CDP:
    def __init__(self, ws_url):
        self.ws = _WS(ws_url)
        self.i = 0

    def __call__(self, method, **params):
        self.i += 1
        my = self.i
        self.ws.send(json.dumps({"id": my, "method": method, "params": params}))
        while True:
            msg = json.loads(self.ws.recv())
            if msg.get("id") == my:
                if "error" in msg:
                    raise RuntimeError(f"{method}: {msg['error']}")
                return msg.get("result", {})

    def js(self, expr, await_promise=False):
        r = self("Runtime.evaluate", expression=expr, returnByValue=True,
                 awaitPromise=await_promise)
        if "exceptionDetails" in r:
            raise RuntimeError("JS error: " + json.dumps(r["exceptionDetails"])[:800])
        return r.get("result", {}).get("value")


# --------------------------------------------------------------------------
# In-page logic
# --------------------------------------------------------------------------
CAPTURE_CSS = r"""
html.pdfcap, html.pdfcap body { background: transparent !important; }
html.pdfcap *, html.pdfcap *::before, html.pdfcap *::after {
  visibility: hidden !important; transition: none !important; animation: none !important;
  opacity: 1 !important; }
html.pdfcap [data-pdfcap-self] { visibility: visible !important; color: transparent !important;
  -webkit-text-fill-color: transparent !important; text-shadow: none !important;
  border-color: transparent !important; outline: none !important; box-shadow: none !important;
  text-decoration-color: transparent !important; }
html.pdfcap [data-pdfcap-self] *, html.pdfcap [data-pdfcap-self]::before,
html.pdfcap [data-pdfcap-self]::after { visibility: hidden !important; }
html.pdfcap [data-pdfcap-tree], html.pdfcap [data-pdfcap-tree] *,
html.pdfcap [data-pdfcap-tree]::before, html.pdfcap [data-pdfcap-tree]::after,
html.pdfcap [data-pdfcap-tree] *::before, html.pdfcap [data-pdfcap-tree] *::after {
  visibility: visible !important; }
html.pdfcap [data-pdfcap-probe] { visibility: visible !important; background: #f00 !important;
  border-radius: 0 !important; mask: none !important; -webkit-mask: none !important;
  filter: none !important; mix-blend-mode: normal !important; color: transparent !important;
  -webkit-text-fill-color: transparent !important; border-color: transparent !important;
  outline: none !important; box-shadow: none !important; object-position: -99999px -99999px !important; }
html.pdfcap [data-pdfcap-probe] *, html.pdfcap [data-pdfcap-probe]::before,
html.pdfcap [data-pdfcap-probe]::after { visibility: hidden !important; }
[data-pdfdone-tree] *, [data-pdfdone-tree]::before, [data-pdfdone-tree]::after,
[data-pdfdone-hide] { visibility: hidden !important; }
"""

SCAN_JS = r"""
(svgFiles) => {
  const GRAD = /gradient\(/;
  const items = [];
  const inTree = new Set();
  const has = (v) => v && v !== 'none';
  const svgNeedsFlatten = (el) => !!el.querySelector('linearGradient,radialGradient,pattern,mask,filter');
  const imgNeedsFlatten = (el) => {
    const src = (el.currentSrc || el.src || '');
    return svgFiles.some(f => src.endsWith(f));
  };
  const all = Array.from(document.querySelectorAll('body *'));
  let n = 0;
  // Capture region = element box expanded OUT to whole CSS px; lw/lh = the element's
  // own (untransformed) border-box size. The exact painted position inside the
  // capture is measured later with a probe, so sub-pixel snapping never shifts it.
  const box = (el) => { const r = el.getBoundingClientRect();
    const x = r.left + scrollX, y = r.top + scrollY;
    // stay inside the viewport width: a wider clip makes Chrome resize + relayout mid-capture
    const VW = document.documentElement.clientWidth;
    const fx = Math.max(0, Math.floor(x) - 1), fy = Math.max(0, Math.floor(y) - 1);
    const cw = Math.max(1, Math.min(VW, Math.ceil(x + r.width) + 1) - fx);
    const ch = Math.ceil(y + r.height) + 1 - fy;
    const cs = getComputedStyle(el);
    const svg = tagOf(el) === 'svg';
    const lw = svg ? (parseFloat(cs.width) || r.width) : (el.offsetWidth || r.width);
    const lh = svg ? (parseFloat(cs.height) || r.height) : (el.offsetHeight || r.height);
    return {x: fx, y: fy, w: cw, h: ch, ex: x, ey: y, rw: r.width, rh: r.height, lw, lh}; };
  const tagOf = (el) => el.tagName.toLowerCase();
  const insideTree = (el) => { for (let p = el.parentElement; p; p = p.parentElement)
    if (inTree.has(p)) return true; return false; };
  const opaque = (cs) => !/rgba\([^)]*,\s*0?\.\d+\)|rgba\([^)]*,\s*0\)|transparent/.test(cs.backgroundImage)
       && ['borderTopLeftRadius','borderTopRightRadius','borderBottomLeftRadius','borderBottomRightRadius']
          .every(k => parseFloat(cs[k]) === 0);
  for (const el of all) {
    const cs = getComputedStyle(el);
    if (cs.display === 'none') continue;
    const tag = el.tagName.toLowerCase();
    const clip = (cs.webkitBackgroundClip || '') + ' ' + (cs.backgroundClip || '');
    const bgGrad = GRAD.test(cs.backgroundImage);
    const tree =
      (bgGrad && clip.includes('text')) ||
      has(cs.maskImage) || has(cs.webkitMaskImage) || has(cs.webkitMaskBoxImage) ||
      has(cs.backdropFilter) ||
      (tag === 'svg' && svgNeedsFlatten(el)) ||
      (tag === 'img' && imgNeedsFlatten(el));
    const blend = cs.mixBlendMode && cs.mixBlendMode !== 'normal';
    for (const ps of ['::before', '::after']) {
      const p = getComputedStyle(el, ps);
      if (p.content !== 'none' && (GRAD.test(p.backgroundImage) || has(p.maskImage) || has(p.webkitMaskImage)))
        items.push({kind: 'unsupported', why: 'gradient/mask on ' + tag + ps});
    }
    if (!(tree || blend || bgGrad)) continue;
    if (insideTree(el)) continue;
    const b = box(el);
    if (b.rw < 0.5 || b.rh < 0.5) continue;
    const id = String(n++);
    if (blend) {
      // Blend with the backdrop: capture the nearest painted ancestor together with el.
      let root = el.parentElement;
      while (root && root !== document.body) {
        const rc = getComputedStyle(root);
        if (rc.backgroundImage !== 'none' || !/rgba\(0, 0, 0, 0\)|transparent/.test(rc.backgroundColor)) break;
        root = root.parentElement;
      }
      if (!root || root === document.body) { items.push({kind: 'unsupported', why: 'blend without backdrop'}); continue; }
      let rid = root.getAttribute('data-pdfid');
      if (!rid) { rid = String(n++); root.setAttribute('data-pdfid', rid); }
      el.setAttribute('data-pdfid', id);
      inTree.add(el);
      const existing = items.find(it => it.id === rid);
      if (existing) { existing.kind = 'blendroot'; existing.with = (existing.with || []).concat(id);
                      existing.key = null; }
      else { const rcs = getComputedStyle(root);
             items.push({id: rid, kind: 'blendroot', with: [id], ...box(root), fmt: opaque(rcs) ? 'jpeg' : 'png'}); }
      items.push({id, kind: 'hide'});
      continue;
    }
    const key0 = tag === 'svg' ? 'svg|' + el.outerHTML + '|' + [b.lw, b.lh].join(',') : null;
    el.setAttribute('data-pdfid', id);
    if (tree) {
      inTree.add(el);
      const key = key0;
      items.push({id, kind: tag === 'img' ? 'img' : 'tree', ...b, fmt: 'png', key});
    } else {
      const key = ['self', cs.backgroundImage, cs.backgroundColor, cs.backgroundSize, cs.backgroundPosition,
                   cs.backgroundClip, cs.backgroundOrigin, cs.borderRadius, cs.borderWidth, b.lw, b.lh].join('|');
      items.push({id, kind: 'self', ...b, fmt: (opaque(cs) && b.w * b.h > 150000) ? 'jpeg' : 'png', key});
    }
  }
  return items;
}
"""

MARK_JS = r"""
(ids, mode) => {
  document.querySelectorAll('[data-pdfcap-self],[data-pdfcap-tree],[data-pdfcap-probe]').forEach(e => {
    e.removeAttribute('data-pdfcap-self'); e.removeAttribute('data-pdfcap-tree');
    e.removeAttribute('data-pdfcap-probe'); });
  if (!ids) { document.documentElement.classList.remove('pdfcap'); return true; }
  const [first, ...rest] = ids;
  const el = document.querySelector('[data-pdfid="' + first + '"]');
  el.setAttribute(mode === 'probe' ? 'data-pdfcap-probe' : mode === 'tree' ? 'data-pdfcap-tree' : 'data-pdfcap-self', '');
  if (mode !== 'probe') rest.forEach(i => document.querySelector('[data-pdfid="' + i + '"]').setAttribute('data-pdfcap-tree', ''));
  document.documentElement.classList.add('pdfcap');
  return true;
}
"""

# Find the probe's painted box inside a capture, with sub-pixel precision taken
# from the anti-aliased edge coverage. Runs in the page (canvas), no deps.
MEASURE_JS = r"""
(url) => new Promise((res, rej) => { const im = new Image(); im.onload = () => {
  const W = im.naturalWidth, H = im.naturalHeight, c = document.createElement('canvas');
  c.width = W; c.height = H; const g = c.getContext('2d', {willReadFrequently: true});
  g.drawImage(im, 0, 0); const d = g.getImageData(0, 0, W, H).data;
  const A = (x, y) => d[(y * W + x) * 4 + 3] / 255;
  let x0 = -1, x1 = -1, y0 = -1, y1 = -1;
  const rowHas = (y) => { for (let x = 0; x < W; x++) if (A(x, y) > 0.02) return true; return false; };
  for (let y = 0; y < H; y++) if (rowHas(y)) { y0 = y; break; }
  for (let y = H - 1; y >= 0; y--) if (rowHas(y)) { y1 = y; break; }
  if (y0 < 0) { res(null); return; }
  const my = Math.floor((y0 + y1) / 2);
  for (let x = 0; x < W; x++) if (A(x, my) > 0.02) { x0 = x; break; }
  for (let x = W - 1; x >= 0; x--) if (A(x, my) > 0.02) { x1 = x; break; }
  const mx = Math.floor((x0 + x1) / 2);
  res({W, H, left: x0 + 1 - A(x0, my), right: x1 + A(x1, my),
       top: y0 + 1 - A(mx, y0), bottom: y1 + A(mx, y1)});
}; im.onerror = () => rej('probe decode failed'); im.src = url; })
"""

APPLY_JS = r"""
(id, kind, url, m) => {
  const el = document.querySelector('[data-pdfid="' + id + '"]');
  const imp = (k, v) => el.style.setProperty(k, v, 'important');
  if (kind === 'hide') { el.setAttribute('data-pdfdone-hide', ''); return true; }
  const kx = m.lw / (m.right - m.left), ky = m.lh / (m.bottom - m.top);
  const bg = 'url("' + url + '") ' + (-m.left * kx) + 'px ' + (-m.top * ky) + 'px / ' +
             (m.W * kx) + 'px ' + (m.H * ky) + 'px no-repeat border-box';
  if (kind === 'img') {
    const cs = getComputedStyle(el);
    imp('width', cs.width); imp('height', cs.height);
    imp('filter', 'none'); imp('mask', 'none'); imp('-webkit-mask', 'none'); imp('mix-blend-mode', 'normal');
    imp('background', bg);
    el.removeAttribute('srcset');
    el.src = 'data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7';
    return true;
  }
  imp('background', bg);
  if (kind === 'tree') {
    imp('-webkit-background-clip', 'border-box'); imp('background-clip', 'border-box');
    imp('color', 'transparent'); imp('-webkit-text-fill-color', 'transparent');
    imp('text-shadow', 'none'); imp('border-color', 'transparent'); imp('box-shadow', 'none');
    imp('outline-color', 'transparent'); imp('text-decoration-color', 'transparent');
    imp('mask', 'none'); imp('-webkit-mask', 'none'); imp('filter', 'none'); imp('backdrop-filter', 'none');
    imp('mix-blend-mode', 'normal');
    el.setAttribute('data-pdfdone-tree', '');
  }
  return true;
}
"""


def _unclip(m, it, scale):
    """If an ancestor's overflow clips the probe (element hanging off a page edge),
    rebuild the clipped side(s) from the element's known on-screen size."""
    for a, b, org, size in (("left", "right", it["ex"] - it["x"], it["rw"]),
                            ("top", "bottom", it["ey"] - it["y"], it["rh"])):
        exp_a, exp_len = org * scale, size * scale
        if (m[b] - m[a]) >= exp_len - 1.5:
            continue
        if abs(m[a] - exp_a) <= 1.5:
            m[b] = m[a] + exp_len
        elif abs(m[b] - (exp_a + exp_len)) <= 1.5:
            m[a] = m[b] - exp_len
        else:
            m[a], m[b] = exp_a, exp_a + exp_len


# --------------------------------------------------------------------------
# Chrome lifecycle
# --------------------------------------------------------------------------
def _launch(chrome, user_dir):
    flags = ["--disable-gpu", "--no-first-run", "--no-default-browser-check",
             "--disable-dev-shm-usage", "--hide-scrollbars", "--mute-audio",
             "--disable-extensions", "--allow-file-access-from-files",
             "--remote-allow-origins=*", "--remote-debugging-port=0",
             f"--user-data-dir={user_dir}", "--force-color-profile=srgb",
             ]
    if hasattr(os, "geteuid") and os.geteuid() == 0:
        flags.append("--no-sandbox")
    if not ("headless_shell" in chrome or "headless-shell" in chrome):
        flags.insert(0, "--headless=new")
    # stderr goes to a file: a PIPE nobody reads fills up and can freeze Chrome
    log = open(Path(user_dir) / "chrome.log", "wb")
    proc = subprocess.Popen([chrome, *flags, "about:blank"],
                            stdout=subprocess.DEVNULL, stderr=log)
    port_file = Path(user_dir) / "DevToolsActivePort"
    t0 = time.time()
    while not port_file.exists() or not port_file.read_text().strip():
        if proc.poll() is not None:
            raise RuntimeError("Chrome exited: " + (Path(user_dir) / "chrome.log").read_text(errors="replace")[-600:])
        if time.time() - t0 > 30:
            proc.kill(); raise RuntimeError("Chrome did not open a DevTools port in 30 s")
        time.sleep(0.05)
    port = int(port_file.read_text().split()[0])
    for _ in range(100):
        try:
            with urllib.request.urlopen(f"http://127.0.0.1:{port}/json/list", timeout=5) as r:
                pages = [t for t in json.load(r) if t.get("type") == "page"]
            if pages:
                return proc, pages[0]["webSocketDebuggerUrl"]
        except OSError:
            pass
        time.sleep(0.05)
    proc.kill()
    raise RuntimeError("no DevTools page target")


def _svg_files_with_effects(assets: Path):
    """Asset SVG files (used via <img>) whose content has gradients/patterns/masks/filters."""
    out = []
    for p in assets.rglob("*.svg"):
        try:
            t = p.read_text(encoding="utf-8", errors="ignore")
        except OSError:
            continue
        if re.search(r"<(linearGradient|radialGradient|pattern|mask|filter)\b", t):
            out.append("/" + "/".join(p.relative_to(assets).parts).replace(" ", "%20"))
    return out


def html_to_portable_pdf(chrome, html_path: Path, pdf_path: Path, width_px: int, height_px: int,
                         assets: Path, verbose=True):
    user_dir = tempfile.mkdtemp(prefix="b24-chrome-")
    proc = None
    try:
        proc, ws_url = _launch(chrome, user_dir)
        cdp = _CDP(ws_url)
        cdp("Page.enable"); cdp("Runtime.enable")
        cdp("Emulation.setDeviceMetricsOverride", width=width_px, height=height_px,
            deviceScaleFactor=1, mobile=False)
        cdp("Emulation.setEmulatedMedia", media="print")
        cdp("Page.navigate", url=html_path.as_uri())
        # wait for load + fonts + images
        cdp.js("""new Promise(res => { const go = () => document.fonts.ready.then(() =>
                   Promise.all(Array.from(document.images).map(i => i.complete ? 1 :
                     new Promise(r => { i.onload = i.onerror = r; })))).then(() =>
                   requestAnimationFrame(() => requestAnimationFrame(() => res(true))));
                 if (document.readyState === 'complete') go(); else addEventListener('load', go); })""",
               await_promise=True)
        cdp.js("(() => { const s = document.createElement('style'); s.id = 'pdfcap-css';"
               f"s.textContent = {json.dumps(CAPTURE_CSS)}; document.head.appendChild(s); return 1; }})()")
        items = cdp.js(f"({SCAN_JS})({json.dumps(_svg_files_with_effects(assets))})")
        unsupported = [it["why"] for it in items if it["kind"] == "unsupported"]
        cdp("Emulation.setDefaultBackgroundColorOverride", color={"r": 0, "g": 0, "b": 0, "a": 0})
        cache, done = {}, []
        for it in items:
            if it["kind"] in ("unsupported", "hide"):
                if it["kind"] == "hide":
                    done.append((it["id"], "hide", "", {}))
                continue
            key = it.get("key")
            if key and key in cache:
                url, m = cache[key]
            else:
                ids = [it["id"], *it.get("with", [])]
                mode = "tree" if it["kind"] in ("tree", "img") else "self"
                # small things (icons, pills) get extra resolution so edges stay crisp when zoomed
                scale = max(SCALE, min(10.0, 240.0 / max(it["w"], it["h"], 1)))
                clip = {"x": it["x"], "y": it["y"], "width": it["w"], "height": it["h"], "scale": scale}
                # 1) probe: where exactly does Chrome paint this box inside the capture?
                cdp.js(f"({MARK_JS})({json.dumps(ids)}, 'probe')")
                probe = cdp("Page.captureScreenshot", format="png", captureBeyondViewport=True,
                            fromSurface=True, clip=clip)
                m = cdp.js(f"({MEASURE_JS})({json.dumps('data:image/png;base64,' + probe['data'])})",
                           await_promise=True)
                if not m or m["right"] - m["left"] < 1 or m["bottom"] - m["top"] < 1:
                    unsupported.append("empty capture")
                    continue
                m.update(lw=it["lw"], lh=it["lh"])
                _unclip(m, it, scale)
                # 2) the real paint
                cdp.js(f"({MARK_JS})({json.dumps(ids)}, {json.dumps(mode)})")
                fmt = it["fmt"]
                shot = cdp("Page.captureScreenshot", format=fmt,
                           **({"quality": 92} if fmt == "jpeg" else {}),
                           captureBeyondViewport=True, fromSurface=True, clip=clip)
                url = f"data:image/{fmt};base64," + shot["data"]
                if key:
                    cache[key] = (url, m)
            done.append((it["id"], "tree" if it["kind"] == "tree" else
                         "img" if it["kind"] == "img" else "self", url, m))
        cdp.js(f"({MARK_JS})(null, null)")
        cdp("Emulation.setDefaultBackgroundColorOverride")
        for id_, kind, url, m in done:
            cdp.js(f"({APPLY_JS})({json.dumps(id_)}, {json.dumps(kind)}, {json.dumps(url)}, {json.dumps(m)})")
        # let the swapped images decode before printing
        cdp.js("""new Promise(res => Promise.all(Array.from(document.images).map(i => i.decode().catch(() => 0)))
                  .then(() => requestAnimationFrame(() => requestAnimationFrame(() => res(true)))))""",
               await_promise=True)
        cdp("Emulation.clearDeviceMetricsOverride")
        pdf = cdp("Page.printToPDF", printBackground=True, preferCSSPageSize=True,
                  displayHeaderFooter=False, marginTop=0, marginBottom=0, marginLeft=0,
                  marginRight=0, generateTaggedPDF=False)
        pdf_path.write_bytes(base64.b64decode(pdf["data"]))
        if verbose:
            n = sum(1 for d in done if d[1] != "hide")
            print(f"PDF portability: flattened {n} effect layer(s) into images "
                  f"({len(cache)} unique).", file=sys.stderr)
            for w in sorted(set(unsupported)):
                print(f"WARNING: not flattened ({w}) — this will render differently outside Chrome.",
                      file=sys.stderr)
        return True
    finally:
        if proc:
            proc.kill()
            try:
                proc.wait(5)
            except Exception:
                pass
        shutil.rmtree(user_dir, ignore_errors=True)


if __name__ == "__main__":
    import argparse
    sys.path.insert(0, str(Path(__file__).resolve().parent))
    from render import find_chrome, ASSETS
    ap = argparse.ArgumentParser()
    ap.add_argument("html"); ap.add_argument("pdf")
    ap.add_argument("--width", type=int, default=794); ap.add_argument("--height", type=int, default=1123)
    a = ap.parse_args()
    html_to_portable_pdf(find_chrome(), Path(a.html).resolve(), Path(a.pdf), a.width, a.height, ASSETS)
