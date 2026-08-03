# Bitrix24 Partner Brand Style — skill

A Claude Code skill that turns the official **Bitrix24 Partners design system**
into a one-prompt content generator. Ask Claude to make a partner guide, sales
playbook, pricing one-pager, LinkedIn carousel, or Instagram story, and it
assembles the HTML from the bundled brand kit and renders the final file.

**Outputs**
- **A4 PDF** — guides, brochures, one-pagers, playbooks (portrait *or* landscape)
- **LinkedIn** — square 1080×1080 carousels / galleries (PNG per slide)
- **Instagram Stories** — 1080×1920 with a built-in UI safe-zone (PNG per slide)

Everything (Montserrat font, official logos, colors, components) is bundled, so
output is self-contained, offline, and on-brand every time.

---

## Prerequisites
- **Google Chrome** (or Chromium/Edge) — used to render HTML → PDF.
- **Python 3** — ships with macOS/Linux; on Windows install from python.org
  (tick *"Add python.exe to PATH"* during setup).
- For social PNG export, one of:
  - `pip install pymupdf`  *(recommended — works the same on all platforms)*, or
  - **poppler** — `brew install poppler` (macOS) / `apt-get install poppler-utils`
    (Linux). On Windows poppler is fiddly, so just use PyMuPDF.

The render script auto-detects Chrome on macOS, Linux **and Windows**, so it works
on all three — only the install commands below differ per OS.

## Install (Claude Code)

Skills are auto-discovered from the `skills/` folder in your Claude config dir.

### macOS / Linux
```bash
# unzip the delivered archive, then — personal (every project):
cp -R bitrix24-partner-style ~/.claude/skills/
# …or one project only:
mkdir -p .claude/skills && cp -R bitrix24-partner-style .claude/skills/
```
Verify: `ls ~/.claude/skills/bitrix24-partner-style/SKILL.md`

### Windows
The config dir is `%USERPROFILE%\.claude\skills\` (i.e. `C:\Users\<you>\.claude\skills\`).

- **Easiest (Explorer):** right-click the zip → *Extract All*, then drag the
  `bitrix24-partner-style` folder into `C:\Users\<you>\.claude\skills\`
  (create the `.claude\skills` folders if they don't exist).
- **PowerShell:**
  ```powershell
  Expand-Archive bitrix24-partner-style-skill.zip -DestinationPath $env:TEMP\b24skill
  New-Item -ItemType Directory -Force "$env:USERPROFILE\.claude\skills" | Out-Null
  Copy-Item "$env:TEMP\b24skill\bitrix24-partner-style" "$env:USERPROFILE\.claude\skills\" -Recurse -Force
  ```
  Verify: `dir "$env:USERPROFILE\.claude\skills\bitrix24-partner-style\SKILL.md"`

> **WSL note:** if you run Claude Code inside WSL (Ubuntu), use the macOS/Linux
> commands above — the skill lives in your WSL home (`~/.claude/skills/`), not the
> Windows profile.

No restart needed on any platform. In a session you can type
`/bitrix24-partner-style` to invoke it directly, or just ask naturally (below).

## Use it
Just describe what you want — the skill triggers on its own:
- *"Собери партнёрскую брошюру про Vibe+ на A4."*
- *"Сделай карусель для LinkedIn на 5 слайдов о том, как продавать ценность, а не фичи."*
- *"Нужна сторис в инсту с CTA «Стать партнёром»."*

Or drive the renderer directly.

macOS / Linux:
```bash
python3 ~/.claude/skills/bitrix24-partner-style/scripts/render.py mydoc.html --format a4
python3 ~/.claude/skills/bitrix24-partner-style/scripts/render.py slide.html --format li
python3 ~/.claude/skills/bitrix24-partner-style/scripts/render.py story.html --format story
```
Windows (PowerShell — note `python`, not `python3`):
```powershell
python "$env:USERPROFILE\.claude\skills\bitrix24-partner-style\scripts\render.py" mydoc.html --format a4
```
Formats: `a4` · `a4-land` · `li` (LinkedIn 1080²) · `story` (IG 1080×1920).

## What's inside
```
bitrix24-partner-style/
├── SKILL.md                  # instructions + trigger description
├── INSTALL.md                # this file
├── assets/
│   ├── DESIGN_SYSTEM.md      # full spec (colors, components, formats, logo rules)
│   ├── bitrix24-kit.css      # tokens + component classes
│   ├── bitrix24-template.html# copy-paste component source
│   ├── bitrix24-logo/        # official logos (incl. partner lockups)
│   └── Montserrat (1)/       # brand font (embedded)
└── scripts/
    └── render.py             # HTML → PDF (A4) / PNG per slide (social)
```

## Updating
Replace the folder with a newer version (same path). To tweak the brand system
itself, edit files in `assets/` — `DESIGN_SYSTEM.md` is the source of truth.
