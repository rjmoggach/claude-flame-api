"""Parse the Flame 2027 Batch/Action node attribute pages (raw_md) into data.

Usage (as module): from parse import parse_file
"""
import re
import json

SEC = re.compile(r"^## (.+) Attributes\s*$")
HDR = re.compile(r"^###\s+`?\s*([A-Za-z0-9_]+)\s+\((type|class)\s+'([^']*)'\)\s*`?\s*$")
VR = re.compile(r"^Value [rR]ange:\s*(.*)$")


def _clean(line, ctx, fixes):
    """Repair known markup garbles (confirmed against the HTML original)."""
    s = line.rstrip("\n")
    st = s.strip()
    if st in (">", "`"):
        fixes.append(f"{ctx}: dropped stray line {st!r} (HTML markup artefact)")
        return None
    if st.startswith("`") and st.endswith("`") and len(st) > 1 and not st.startswith("- "):
        fixes.append(f"{ctx}: removed wrapping backticks from {st!r}")
        st = st[1:-1]
    if st.startswith("- `"):
        new = "- " + st[3:].rstrip("`")
        fixes.append(f"{ctx}: removed stray backticks from bullet {st!r}")
        st = new
    if st.startswith("- ") and st.endswith("<"):
        fixes.append(f"{ctx}: removed stray '<' from bullet {st!r}")
        st = st[:-1]
    if "The  token" in st:
        st = st.replace("The  token", "The <version> token")
        fixes.append(f"{ctx}: restored '<version>' token stripped by HTML->md conversion")
    return st


def _parse_body(lines, ctx, fixes):
    desc, values, args = [], "UNSET", None
    i = 0
    cl = []
    for ln in lines:
        c = _clean(ln, ctx, fixes)
        if c is None:
            continue
        # split "....complete.Value range:" glued lines
        m = re.match(r"^(.*\S)(Value [rR]ange:.*)$", c)
        if m and not c.startswith("Value"):
            fixes.append(f"{ctx}: split description glued to 'Value range:'")
            cl.extend([m.group(1), m.group(2)])
        else:
            cl.append(c)
    cl = [c for c in cl if c != ""]
    while i < len(cl):
        c = cl[i]
        m = VR.match(c)
        if m:
            rest = m.group(1).strip()
            if rest == "None":
                values = None
                i += 1
                continue
            if rest:
                raise ValueError(f"{ctx}: unexpected value range text {rest!r}")
            # following: None or bullets
            j = i + 1
            if j < len(cl) and cl[j] == "None":
                values = None
                i = j + 1
                continue
            vals = []
            while j < len(cl) and cl[j].startswith("- "):
                vals.append(cl[j][2:].strip())
                j += 1
            values = vals
            i = j
            continue
        if c.startswith("- "):
            # bullets without a Value range header -> argument list
            if args is None:
                args = []
            args.append(c[2:].strip())
            i += 1
            continue
        if values != "UNSET":
            raise ValueError(f"{ctx}: text after value range: {c!r}")
        desc.append(c.strip())
        i += 1
    d = {"description": " ".join(desc)}
    if values == "UNSET":
        d["values"] = None
        d["value_range_given"] = False
    else:
        d["values"] = values
    if args is not None:
        d["arguments"] = args
    return d


def parse_file(path):
    """Return (title, sections, fixes); sections = list of (node, [(attr, info)])."""
    text = open(path, encoding="utf-8").read().split("\n")
    title = next(l[2:].strip() for l in text if l.startswith("# "))
    sections, fixes = [], []
    cur, attr, body = None, None, []

    def flush():
        nonlocal attr, body
        if attr is not None:
            name, kind, typ = attr
            info = {"type": typ}
            if kind == "class":
                info["kind"] = "class"
            info.update(_parse_body(body, f"{cur[0]}.{name}", fixes))
            cur[1].append((name, info))
        attr, body = None, []

    for line in text:
        if line.startswith("## "):
            flush()
            m = SEC.match(line)
            if m:
                cur = (m.group(1).strip(), [])
                sections.append(cur)
            else:
                cur = None  # e.g. "Related pages"
            continue
        if cur is None:
            continue
        if line.startswith("### "):
            flush()
            m = HDR.match(line)
            if not m:
                raise ValueError(f"bad attr header: {line!r}")
            if not line.strip().endswith("`"):
                fixes.append(f"{cur[0]}.{m.group(1)}: attr heading not code-formatted in source")
            attr = (m.group(1), m.group(2), m.group(3))
            continue
        if line.strip() == "---":
            flush()
            continue
        if attr is not None:
            body.append(line)
        elif line.strip():
            raise ValueError(f"stray text in {cur[0]}: {line!r}")
    flush()
    return title, sections, fixes


def defkey(info):
    return json.dumps(info, sort_keys=True)
