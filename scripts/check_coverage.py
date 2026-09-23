#!/usr/bin/env python3
"""Battle Card source check: is every text unit of the partner's .docx in the PDF?

    python3 scripts/check_coverage.py SOURCE.docx battle-card.pdf

Walks every paragraph and every table cell of the Word doc (merged cells
counted once), normalises whitespace/case, and looks for each fragment in the
PDF text (pdftotext, or PyMuPDF as a fallback). Fragments are split on
parentheses and em-dashes, and leading "+"/"-" markers are ignored, because the
template renders those as check / minus icons.

Expected leftovers (review, don't "fix"): words broken across lines with a
hyphen, a header cell that is empty by design ("Aspect"), cover notes such as
"логотипы". Anything else in the list = dropped text: put it back.
Exit code 1 when anything is missing.
"""
import re, subprocess, sys

def pdf_text(path):
    try:
        return subprocess.run(["pdftotext", path, "-"], capture_output=True,
                              text=True, check=True).stdout
    except Exception:
        import fitz  # PyMuPDF
        return "\n".join(p.get_text() for p in fitz.open(path))

def norm(s):
    s = s.replace("’", "'").replace(" ", " ")
    return re.sub(r"\s+", " ", s).strip().lower()

def main():
    if len(sys.argv) != 3:
        sys.exit(__doc__)
    import docx
    from docx.table import Table
    from docx.text.paragraph import Paragraph
    d = docx.Document(sys.argv[1])
    units = []
    for ch in d.element.body.iterchildren():
        if ch.tag.endswith("}p"):
            units.append(Paragraph(ch, d).text)
        elif ch.tag.endswith("}tbl"):
            for row in Table(ch, d).rows:
                seen = []
                for c in row.cells:
                    if any(c._tc is x for x in seen):
                        continue
                    seen.append(c._tc)
                    units += c.text.split("\n")
    # join hyphenated line breaks so "add-\nons" matches "add-ons"
    raw = pdf_text(sys.argv[2])
    raw = re.sub(r"-\s*\n\s*", "-", raw)
    pdf = norm(raw)
    pdf_nohy = pdf.replace("-", "")  # Chrome drops the hyphen at a line break ("per-user" -> "peruser")
    missing = []
    for u in units:
        u = norm(u.lstrip("•"))
        for frag in re.split(r"[()—]", u):
            frag = frag.strip(" +-.,;:")
            if (len(frag) > 3 and frag not in pdf and frag.replace("-", "") not in pdf_nohy
                    and frag not in missing):
                missing.append(frag)
    if not missing:
        print("OK: every text unit of the source doc is in the PDF.")
        return
    print(f"{len(missing)} fragment(s) not found in the PDF:")
    for m in missing:
        print("  -", m)
    sys.exit(1)

if __name__ == "__main__":
    main()
