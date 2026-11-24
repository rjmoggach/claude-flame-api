"""Parse the pydoc-generated 'flame module' help page into per-class Markdown.
Usage: python3 -I pydoc2md.py <flame_module.html> <out_dir>
Outputs: <out_dir>/<ClassName>.md, _functions.md, _data.md, _hierarchy.md
"""
import sys, os, re, html

TAG = re.compile(r"<[^>]+>")


def text(fragment):
    fragment = re.sub(r"<br\s*/?>", "\n", fragment, flags=re.I)
    t = TAG.sub("", fragment)
    t = html.unescape(t)
    # some descriptions contain double-escaped markup
    t = TAG.sub("", t)
    t = html.unescape(t)
    lines = [l.strip() for l in t.split("\n")]
    out, blank = [], 0
    for l in lines:
        if not l:
            blank += 1
            if blank == 1:
                out.append("")
        else:
            blank = 0
            out.append(l)
    return "\n".join(out).strip()


def parse_entries(chunk):
    """Return list of (name, raw_dt_text, dd_text) for each <dl><dt>..</dt><dd>..</dd></dl>."""
    entries = []
    for m in re.finditer(r"<dt>(.*?)</dt>\s*(?:<dd>(.*?)</dd>)?", chunk, re.S):
        dt, dd = m.group(1), m.group(2) or ""
        nm = re.search(r"<strong>(.*?)</strong>", dt, re.S)
        name = text(nm.group(1)) if nm else text(dt)
        entries.append((name, " ".join(text(dt).split()), text(dd)))
    return entries


def split_sections(body):
    """Split class body by <hr> into (heading, html)."""
    parts = re.split(r"<hr\s*/?>", body)
    out = []
    for p in parts:
        if "Method resolution order" in p[:300]:
            heading = "Method resolution order:"
        else:
            pre = p.split("<dl", 1)[0]
            pre_t = " ".join(text(pre).split())
            heading = pre_t if pre_t.endswith(":") and len(pre_t) < 120 else ""
        out.append((heading, p))
    return out


def fmt_method(name, dt, dd):
    lines = [f"### `{name}`", ""]
    if dd:
        # signature is usually first paragraph: "name( (Cls)arg1, ...) -> type :"
        paras = dd.split("\n\n")
        sig = paras[0].strip()
        rest = "\n\n".join(paras[1:]).strip()
        if re.match(rf"^{re.escape(name)}\s*\(", sig):
            lines += ["```python", sig.rstrip(" :"), "```", ""]
            if rest:
                lines += [rest, ""]
        else:
            lines += [dd, ""]
    elif dt and dt != name:
        lines += [f"`{dt}`", ""]
    return lines


def main(src, out):
    os.makedirs(out, exist_ok=True)
    s = open(src, encoding="utf-8", errors="replace").read()
    starts = [m.start() for m in re.finditer(r'<table[^>]*summary="section"', s)]
    starts.append(s.find('class="was-this-helpful"', starts[-1]) if s.find('class="was-this-helpful"', starts[-1]) > 0 else len(s))
    summary = []
    for a, b in zip(starts, starts[1:]):
        seg = s[a:b]
        cm = re.search(r'<a name="(\w+)">class <strong>(\w+)</strong></a>\((.*?)\)</font>', seg, re.S)
        if not cm:
            head = text(seg[:400]).split("\n")[0].strip()
            if head.startswith("Classes"):
                open(os.path.join(out, "_hierarchy_raw.txt"), "w").write(text(seg))
            elif head.startswith("Functions"):
                ents = parse_entries(seg)
                L = ["# flame module-level functions", "", "Called as `flame.<function>(...)`.", ""]
                for n, dt, dd in ents:
                    L += fmt_method(n, dt, dd)
                open(os.path.join(out, "_functions.md"), "w").write("\n".join(L) + "\n")
            elif head.startswith("Data"):
                raw = re.sub(r"<br\s*/?>", "\n", seg, flags=re.I)
                raw = html.unescape(TAG.sub("", raw))
                raw = raw.split("<div")[0]
                body_lines = [" ".join(l.split()) for l in raw.split("\n") if l.strip() and l.strip() != "Data"]
                L = ["# flame module-level data (singletons / constants)", "", "These are pre-instantiated objects available as `flame.<name>`.", "", "```"] + body_lines + ["```"]
                open(os.path.join(out, "_data.md"), "w").write("\n".join(L) + "\n")
            continue
        cls, base = cm.group(2), text(cm.group(3)).strip()
        # description = first tt in class header rows
        dm = re.search(r"<td colspan=\"2\"><tt>(.*?)</tt></td>", seg, re.S)
        desc = text(dm.group(1)) if dm else ""
        # body = main cell
        bm = re.search(r'<td width="100%">(.*)', seg, re.S)
        body = bm.group(1) if bm else seg
        L = [f"# class `flame.{cls}`" + (f"({base})" if base else ""), ""]
        if desc:
            L += [desc, ""]
        inherited = []
        for heading, part in split_sections(body):
            ents = parse_entries(part)
            if heading.startswith("Method resolution order"):
                mro = [e[1] for e in ents if e[1] != "Method resolution order:"] or re.findall(r"#(\w+)\">", part)
                mro = re.findall(r'<dd><a [^>]*>(\w+)</a></dd>', part) or mro
                L += ["**Method resolution order:** " + " → ".join(mro), ""]
                continue
            if not ents:
                continue
            if "inherited from" in heading:
                names = [n for n, _, _ in ents if not n.startswith("__")]
                if names:
                    inherited.append((heading.rstrip(":"), names))
                continue
            h = heading.rstrip(":") or "Members"
            h = {"Static methods defined here": "Methods", "Data descriptors defined here": "Properties (data descriptors)"}.get(h, h)
            L += [f"## {h}", ""]
            for n, dt, dd in ents:
                if n in ("__init__", "__reduce__", "__getattr__", "__setattr__") and ("cannot be instantiated" in dd or not dd or "Raises an exception" in dd or n in ("__reduce__",)):
                    if n == "__init__" and "cannot be instantiated" in dd:
                        L += ["> Cannot be instantiated from Python (obtained from other API objects).", ""]
                    continue
                L += fmt_method(n, dt, dd)
        if inherited:
            L += ["## Inherited members", ""]
            for h, names in inherited:
                L += [f"- **{h}:** " + ", ".join(f"`{n}`" for n in names)]
            L += [""]
        md = "\n".join(L)
        md = re.sub(r"\n{3,}", "\n\n", md)
        open(os.path.join(out, f"{cls}.md"), "w").write(md.strip() + "\n")
        summary.append((cls, base, desc.split("\n")[0][:120]))
    with open(os.path.join(out, "_classes.tsv"), "w") as fh:
        for c, b, d in summary:
            fh.write(f"{c}\t{b}\t{d}\n")
    print(f"{len(summary)} classes")


if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2])
