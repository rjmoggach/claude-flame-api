"""Losslessness check.

1. Independent parse of the ORIGINAL HTML pages (html.parser) -> (node, attr, type, description, values).
2. Independent line-scan of raw_md (### headings per ## section) -> (node, attr) pairs.
3. Compare both against node-attributes.json (names, types, descriptions, values).
4. Check every (node, attr) is represented in the md files (row in node section, or covered by README common table).

python3 -I verify.py <raw_md_dir> <html_dir> <nodes_dir>
"""
import sys
import os
import re
import json
from html.parser import HTMLParser

RAW, HTML, OUT = sys.argv[1:4]
PAGES = {
    "batch": ("PyNode_Batch_Nodes_Attributes.md", "Autodesk Flame Family 2027 Help _ PyNode_ Batch Nodes Attributes _ Autodesk.html"),
    "action": ("PyCoNode_Action_Nodes_Attributes.md", "Autodesk Flame Family 2027 Help _ PyCoNode_ Action Nodes Attributes _ Autodesk.html"),
}
J = json.load(open(os.path.join(OUT, "node-attributes.json"), encoding="utf-8"))
errors = []


class P(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.secs = []  # [node, [ [dt_text, [p...], [li...]] ]]
        self.tag = None
        self.buf = ""
        self.in_dd = False

    def handle_starttag(self, t, a):
        if t in ("h2", "dt", "p", "li"):
            self.tag, self.buf = t, ""
        if t == "dd":
            self.in_dd = True

    def handle_endtag(self, t):
        if t == "dd":
            self.in_dd = False
        if t != self.tag:
            return
        txt = " ".join(self.buf.split())
        if t == "h2":
            m = re.match(r"^(.+) Attributes$", txt)
            self.secs.append([m.group(1) if m else None, []])
        elif t == "dt" and self.secs and self.secs[-1][0]:
            self.secs[-1][1].append([txt, [], []])
        elif t in ("p", "li") and self.in_dd and self.secs and self.secs[-1][0] and self.secs[-1][1]:
            self.secs[-1][1][-1][1 if t == "p" else 2].append(txt)
        self.tag = None

    def handle_data(self, d):
        if self.tag:
            self.buf += d


def html_pairs(path):
    p = P()
    p.feed(open(path, encoding="utf-8", errors="replace").read())
    out = []
    for node, attrs in p.secs:
        if not node:
            continue
        for dt, ps, lis in attrs:
            m = re.match(r"^(\w+) \((type|class) '([^']*)'\)$", dt)
            if not m:
                errors.append(f"HTML dt unparsed: {dt!r}")
                continue
            out.append((node, m.group(1), m.group(3), ps, lis))
    return out


def md_pairs(path):
    out, sec = [], None
    for line in open(path, encoding="utf-8"):
        if line.startswith("## "):
            m = re.match(r"^## (.+) Attributes\s*$", line)
            sec = m.group(1) if m else None
        elif line.startswith("### ") and sec:
            out.append((sec, re.search(r"(\w+) \(", line).group(1)))
    return out


def md_text(s):  # same display transform as build.py
    s = re.sub(r"\*\*([A-Za-z0-9_]+)\*\*", r"`\1`", s)
    s = re.sub(r"(?<![*\w])\*([A-Za-z0-9_]+)\*(?![*\w])", r"`\1`", s)
    s = s.replace("<version>", "`<version>`")
    return s.replace("|", "\\|")


readme = open(os.path.join(OUT, "README.md"), encoding="utf-8").read()
report = {}
for kind, (mdf, htf) in PAGES.items():
    data = J[kind]
    hp = html_pairs(os.path.join(HTML, htf))
    mp = md_pairs(os.path.join(RAW, mdf))
    # 1/2: pair coverage
    hset = {(n, a) for n, a, *_ in hp}
    mset = set(mp)
    jset = {(n, a) for n, d in data.items() for a in d}
    for name, s in (("HTML", hset), ("raw_md", mset)):
        if s - jset:
            errors.append(f"{kind}: pairs in {name} missing from JSON: {sorted(s - jset)}")
        if jset - s:
            errors.append(f"{kind}: pairs in JSON not in {name}: {sorted(jset - s)}")
    # 3: content vs HTML
    checked = 0
    for n, a, typ, ps, lis in hp:
        if (n, a) not in jset:
            continue
        j = data[n][a]
        if j["type"] != typ:
            errors.append(f"{kind} {n}.{a}: type {j['type']} != HTML {typ}")
        desc_ps = [p for p in ps if not re.match(r"^Value [rR]ange:", p)]
        hdesc = " ".join(desc_ps)
        jdesc = j["description"].replace("<version>", "").replace("**", "").replace("*", "")
        hdesc_c = hdesc.replace("  ", " ").replace("*", "")
        if " ".join(jdesc.split()) != " ".join(hdesc_c.split()):
            errors.append(f"{kind} {n}.{a}: desc mismatch\n  J: {jdesc}\n  H: {hdesc}")
        jvals = (j["values"] or []) + j.get("arguments", [])
        if [" ".join(v.split()) for v in jvals] != lis:
            errors.append(f"{kind} {n}.{a}: values mismatch J={jvals} H={lis}")
        checked += 1
    # 4: md coverage
    fname = "batch-nodes.md" if kind == "batch" else "action-nodes.md"
    md = open(os.path.join(OUT, fname), encoding="utf-8").read()
    sections = dict(re.findall(r"^## (.+?)\n(.*?)(?=^## |\Z)", md, flags=re.S | re.M))
    common = J[f"common_{kind}_definitions"]
    in_rows = in_common = 0
    for n, d in data.items():
        sec = sections.get(n)
        if sec is None:
            errors.append(f"{kind}: no md section for {n}")
            continue
        for a, info in d.items():
            rowm = re.search(r"^\| `" + re.escape(a) + r"` \|.*$", sec, flags=re.M)
            if a in common and json.dumps(info, sort_keys=True) == json.dumps(common[a], sort_keys=True):
                if rowm:
                    errors.append(f"{kind} {n}.{a}: common attr unexpectedly in table")
                if f"`{a}`" in sec.split("\n\n")[1] if sec.count("\n\n") else False:
                    pass
                if not re.search(r"^\| `" + re.escape(a) + r"` \|", readme, flags=re.M):
                    errors.append(f"{kind}: common {a} not in README table")
                in_common += 1
                continue
            if not rowm:
                errors.append(f"{kind} {n}.{a}: no row in {fname}")
                continue
            r = rowm.group(0)
            if md_text(info["description"]) not in r:
                errors.append(f"{kind} {n}.{a}: description not in row")
            for v in (info["values"] or []) + info.get("arguments", []):
                if v.replace("|", "\\|") not in r and md_text(v) not in r:
                    errors.append(f"{kind} {n}.{a}: value {v!r} not in row")
            if f"`{info['type']}`" not in r:
                errors.append(f"{kind} {n}.{a}: type not in row")
            in_rows += 1
        # missing common attrs must be declared
        missing = [a for a in common if a not in d]
        for a in missing:
            if f"`{a}`" not in sec.strip().split("\n")[0]:
                errors.append(f"{kind} {n}: missing common {a} not declared")
        if not missing and f"Common attrs: all {len(common)}" not in sec:
            errors.append(f"{kind} {n}: common statement absent")
        if f"| {n} |" not in readme:
            errors.append(f"{kind}: {n} not in README index")
    report[kind] = dict(html_pairs=len(hp), html_unique=len(hset), raw_md_pairs=len(mp), raw_md_unique=len(mset),
                        json_pairs=len(jset), json_nodes=len(data), content_checked_vs_html=checked,
                        md_rows=in_rows, covered_by_common=in_common)

print(json.dumps(report, indent=1))
print("ERRORS:", len(errors))
for e in errors:
    print(" -", e)
