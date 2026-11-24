"""Stdlib-only converter: Autodesk help HTML page -> Markdown (body content only).
Usage: python3 -I html2md.py <src_dir> <out_dir>
"""
import sys, os, re, glob, html
from html.parser import HTMLParser

PREFIX = "Autodesk Flame Family 2027 Help _ "
SUFFIX = " _ Autodesk.html"


def slug(title):
    s = re.sub(r"[^A-Za-z0-9]+", "_", title).strip("_")
    return s


class Conv(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.out = []
        self.pre = 0
        self.lists = []  # stack of 'ul'/'ol' counters
        self.table = None  # list of rows
        self.row = None
        self.cell = None
        self.href = None
        self.skip = 0
        self.code = 0

    # helpers
    def w(self, t):
        if self.cell is not None:
            self.cell.append(t)
        else:
            self.out.append(t)

    def nl(self, n=1):
        self.w("\n" * n)

    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if tag in ("script", "style", "noscript", "iframe", "svg"):
            self.skip += 1
            return
        if self.skip:
            return
        if tag in ("h1", "h2", "h3", "h4", "h5", "h6"):
            self.nl(2)
            self.w("#" * int(tag[1]) + " ")
        elif tag == "p":
            if self.cell is None:
                self.nl(2) if not self.lists else self.nl(1)
            else:
                self.w(" ")
        elif tag == "br":
            self.w("\n" if self.pre else ("<br>" if self.cell is not None else "  \n"))
        elif tag == "pre":
            self.pre += 1
            self.nl(2)
            self.w("```python\n")
        elif tag == "code":
            if not self.pre:
                self.code += 1
                self.w("`")
        elif tag in ("strong", "b"):
            if not self.pre:
                self.w("**")
        elif tag in ("em", "i"):
            if not self.pre:
                self.w("*")
        elif tag in ("ul", "ol"):
            self.lists.append([tag, 0])
            self.nl(1)
        elif tag == "li":
            depth = len(self.lists) - 1
            self.nl(1)
            if self.lists and self.lists[-1][0] == "ol":
                self.lists[-1][1] += 1
                bullet = f"{self.lists[-1][1]}. "
            else:
                bullet = "- "
            if self.cell is not None:
                self.w(" • ")
            else:
                self.w("  " * max(depth, 0) + bullet)
        elif tag == "dt":
            self.nl(2)
            self.w("### ")
        elif tag == "dd":
            self.nl(2)
        elif tag == "hr":
            self.nl(2)
            self.w("---")
            self.nl(2)
        elif tag == "table":
            self.table = []
        elif tag == "tr":
            self.row = []
        elif tag in ("td", "th"):
            self.cell = []
        elif tag == "a":
            self.href = a.get("href")
        elif tag == "img":
            alt = a.get("alt") or ""
            if alt:
                self.w(f"[image: {alt}]")

    def handle_endtag(self, tag):
        if tag in ("script", "style", "noscript", "iframe", "svg"):
            self.skip = max(0, self.skip - 1)
            return
        if self.skip:
            return
        if tag in ("h1", "h2", "h3", "h4", "h5", "h6", "p", "dd"):
            if self.cell is None:
                self.nl(1)
        elif tag == "dt":
            self.nl(1)
        elif tag == "pre":
            self.pre -= 1
            self.w("\n```\n")
        elif tag == "code":
            if not self.pre and self.code:
                self.code -= 1
                self.w("`")
        elif tag in ("strong", "b"):
            if not self.pre:
                self.w("**")
        elif tag in ("em", "i"):
            if not self.pre:
                self.w("*")
        elif tag in ("ul", "ol"):
            if self.lists:
                self.lists.pop()
            self.nl(1)
        elif tag in ("td", "th"):
            if self.cell is not None and self.row is not None:
                txt = "".join(self.cell)
                txt = re.sub(r"\s*\n\s*", " ", txt).strip().replace("|", "\\|")
                self.row.append(txt)
            self.cell = None
        elif tag == "tr":
            if self.row is not None and self.table is not None:
                self.table.append(self.row)
            self.row = None
        elif tag == "table":
            rows = self.table or []
            self.table = None
            if rows:
                n = max(len(r) for r in rows)
                rows = [r + [""] * (n - len(r)) for r in rows]
                self.nl(2)
                self.w("| " + " | ".join(rows[0]) + " |\n")
                self.w("|" + "---|" * n + "\n")
                for r in rows[1:]:
                    self.w("| " + " | ".join(r) + " |\n")
                self.nl(1)
        elif tag == "a":
            self.href = None

    def handle_data(self, data):
        if self.skip:
            return
        if not self.pre:
            data = re.sub(r"\s+", " ", data)
        self.w(data)


def extract_body(s):
    i = s.find('id="body-content"')
    if i < 0:
        i = s.find('class="caas_body"')
    i = s.find(">", i) + 1
    ends = [s.find(m, i) for m in ('class="was-this-helpful"', 'class="related-links"', 'class="familylinks"')]
    ends = [e for e in ends if e > 0]
    j = min(ends) if ends else len(s)
    j = s.rfind("<", i, j)
    return s[i:j]


def related(s):
    """Return parent/child link titles for navigation context."""
    i = s.find('class="related-links"')
    if i < 0:
        return []
    chunk = s[i:i + 20000]
    out = []
    for t in re.findall(r"<a [^>]*>(.*?)</a>", chunk, re.S):
        t = html.unescape(re.sub("<[^>]+>", "", t)).strip()
        if t.startswith("Creative Commons"):
            break
        if t:
            out.append(t)
    return out[:40]


def tidy(md):
    md = re.sub(r"[ \t]+\n", "\n", md)
    md = re.sub(r"\n{3,}", "\n\n", md)
    md = re.sub(r"`\s*`", "", md)
    md = re.sub(r"\*\*\s*\*\*", "", md)
    # "Value range:" + None on the same line
    md = re.sub(r"Value range:\s*\n+None", "Value range: None", md)
    return md.strip() + "\n"


def main(src, out):
    os.makedirs(out, exist_ok=True)
    index = []
    for f in sorted(glob.glob(os.path.join(src, "*.html"))):
        base = os.path.basename(f)
        title = base[len(PREFIX):-len(SUFFIX)] if base.startswith(PREFIX) else base[:-5]
        s = open(f, encoding="utf-8", errors="replace").read()
        c = Conv()
        c.feed(extract_body(s))
        md = tidy("".join(c.out))
        rel = related(s)
        name = slug(title) + ".md"
        header = f"<!-- source: {base} -->\n"
        if rel:
            md += "\n## Related pages\n\n" + "\n".join(f"- {r}" for r in rel) + "\n"
        open(os.path.join(out, name), "w", encoding="utf-8").write(header + md)
        index.append((title, name, len(md)))
    with open(os.path.join(out, "_INDEX.tsv"), "w") as fh:
        for t, n, l in index:
            fh.write(f"{t}\t{n}\t{l}\n")
    print(f"converted {len(index)} pages")


if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2])
