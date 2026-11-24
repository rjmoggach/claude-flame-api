"""Build nodes/ docs + JSON from raw_md attribute pages.

python3 -I build.py <raw_md_dir> <out_dir>
"""
import sys
import os
import re
import json
from collections import Counter, OrderedDict

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from parse import parse_file, defkey  # noqa: E402

RAW, OUT = sys.argv[1], sys.argv[2]
FILES = {
    "batch": "PyNode_Batch_Nodes_Attributes.md",
    "action": "PyCoNode_Action_Nodes_Attributes.md",
}


def slug(s):
    s = s.strip().lower()
    s = re.sub(r"[^a-z0-9 _-]", "", s)
    return s.replace(" ", "-")


def md_text(s):
    s = re.sub(r"\*\*([A-Za-z0-9_]+)\*\*", r"`\1`", s)
    s = re.sub(r"(?<![*\w])\*([A-Za-z0-9_]+)\*(?![*\w])", r"`\1`", s)
    s = s.replace("<version>", "`<version>`")
    return s.replace("|", "\\|")


def md_type(info):
    t = f"`{info['type']}`"
    return t + " (class)" if info.get("kind") == "class" else t


def md_values(info):
    out = []
    if info.get("value_range_given") is False:
        out.append("(no value range given)")
    elif info["values"] is None:
        out.append("None")
    else:
        out.append("; ".join(
            v.replace("|", "\\|") if re.match(r"^(Min|Max): ", v) else f"`{v}`"
            for v in info["values"]))
    if "arguments" in info:
        out.append("Arguments: " + "; ".join(md_text(a) for a in info["arguments"]))
    return " ".join(out)


def row(attr, info, note=""):
    d = md_text(info["description"])
    if note:
        d = f"**{note}** {d}"
    return f"| `{attr}` | {md_type(info)} | {d} | {md_values(info)} |"


HEAD = "| attr | type | description | value range |\n|---|---|---|---|"

data, meta = {}, {}
for kind, fn in FILES.items():
    title, sections, fixes = parse_file(os.path.join(RAW, fn))
    raw_pairs = sum(len(a) for _, a in sections)
    nodes, dups = OrderedDict(), Counter()
    for node, attrs in sections:
        d = OrderedDict()
        for a, info in attrs:
            if a in d:
                raise SystemExit(f"duplicate attr {node}.{a}")
            d[a] = info
        if node in nodes:
            if json.dumps(nodes[node]) != json.dumps(d):
                raise SystemExit(f"non-identical duplicate section {node}")
            dups[node] += 1
            continue
        nodes[node] = d
    # common set: most frequent definition per attr, present identically in > 50% of nodes
    cnt = Counter()
    order = []
    for node, d in nodes.items():
        for a, info in d.items():
            cnt[(a, defkey(info))] += 1
            if a not in order:
                order.append(a)
    best = {}
    for (a, k), c in cnt.items():
        if a not in best or c > best[a][1]:
            best[a] = (k, c)
    N = len(nodes)
    common = [a for a in order if best[a][1] > N / 2]
    common_defs = OrderedDict((a, json.loads(best[a][0])) for a in common)
    data[kind] = nodes
    meta[kind] = dict(title=title, fixes=fixes, dups=dups, common=common,
                      common_defs=common_defs, common_count={a: best[a][1] for a in common},
                      raw_sections=len(sections), raw_pairs=raw_pairs, N=N)


def node_parts(kind, node):
    m = meta[kind]
    d = data[kind][node]
    specific, differs = [], []
    for a, info in d.items():
        if a in m["common_defs"]:
            if defkey(info) != defkey(m["common_defs"][a]):
                differs.append(a)
                specific.append((a, info, "Differs from common definition."))
        else:
            specific.append((a, info, ""))
    missing = [a for a in m["common"] if a not in d]
    return specific, differs, missing


# shared (non-common) definitions that recur in >= 2 nodes
def recurring(kind):
    m = meta[kind]
    rec = OrderedDict()
    for node, d in data[kind].items():
        for a, info in d.items():
            if a in m["common_defs"] and defkey(info) == defkey(m["common_defs"][a]):
                continue
            rec.setdefault((a, defkey(info)), []).append(node)
    return [(a, nodes) for (a, k), nodes in rec.items() if len(nodes) >= 2]


def write_nodes_md(kind, fname, heading, intro):
    m = meta[kind]
    L = [f"> Source: {m['title']}", "", f"# {heading}", ""] + intro + [""]
    for node in data[kind]:
        specific, differs, missing = node_parts(kind, node)
        L.append(f"## {node}")
        L.append("")
        info = []
        if m["dups"].get(node):
            info.append(f"Section appears {m['dups'][node] + 1}x in source with identical content (deduplicated here).")
        if missing:
            info.append("Common attrs: all except " + ", ".join(f"`{a}`" for a in missing)
                        + " (not listed for this node in source).")
        else:
            info.append(f"Common attrs: all {len(m['common'])}.")
        if differs:
            info.append("Common attr(s) with a different definition here: "
                        + ", ".join(f"`{a}`" for a in differs) + " (listed below).")
        if not specific:
            info.append("No node-specific attributes.")
        L.append(" ".join(info))
        L.append("")
        if specific:
            L.append(HEAD)
            for a, inf, note in specific:
                L.append(row(a, inf, note))
            L.append("")
    open(os.path.join(OUT, fname), "w", encoding="utf-8").write("\n".join(L).rstrip() + "\n")


write_nodes_md("batch", "batch-nodes.md", "Batch node attributes (node-specific)", [
    "Per Batch node type: only attributes that are NOT in the common set (see `README.md` → "
    "\"Common Batch attributes\"). Every node also has the common attributes unless stated otherwise. "
    "Section names are the source section titles with the trailing \" Attributes\" removed.",
    "",
    "Values column: `Min: x; Max: y` = numeric range; backticked items = accepted values (enum); "
    "`None` = source gives no range (\"Value range: None\"). Access every attribute as `node.<attr>` "
    "(see README).",
])
write_nodes_md("action", "action-nodes.md", "Action object (PyCoNode) attributes (node-specific)", [
    "Per Action object (node inside an Action/Image/GMask Tracer schematic, class `flame.PyCoNode`): "
    "only attributes NOT in the common Action set (see `README.md` → \"Common Action object attributes\"). "
    "Section names are the source section titles with the trailing \" Attributes\" removed.",
    "",
    "Values column: `Min: x; Max: y` = numeric range; backticked items = accepted values or (min tuple; max tuple) "
    "for tuple ranges; `None` = source gives no range.",
])

# JSON
js = OrderedDict()
js["source"] = {k: meta[k]["title"] for k in FILES}
js["batch"] = data["batch"]
js["action"] = data["action"]
js["common_batch"] = meta["batch"]["common"]
js["common_action"] = meta["action"]["common"]
js["common_batch_definitions"] = meta["batch"]["common_defs"]
js["common_action_definitions"] = meta["action"]["common_defs"]
js["notes"] = {
    "schema": "node -> attr -> {type, description, values}. values: list of strings verbatim from source "
              "('Min: x'/'Max: y' = numeric range; other items = accepted values or min/max tuples), or null "
              "when source says 'Value range: None'. Optional keys: kind='class' when the source declares "
              "(class '<type>') instead of (type '<type>'); value_range_given=false when the source gives no "
              "Value range line; arguments=list for bullet arguments given without a Value range.",
    "common": "common_* = attributes whose identical definition appears in more than half of the nodes of that "
              "page. Per-node dicts here are COMPLETE (they still include the common attributes).",
    "duplicate_sections": {k: {n: c + 1 for n, c in meta[k]["dups"].items()} for k in FILES},
    "source_fixes": {k: meta[k]["fixes"] for k in FILES},
}
def dump_js(js):
    # one line per attribute: compact yet grep-friendly
    def c(o):
        return json.dumps(o, ensure_ascii=False)
    out = ["{"]
    keys = list(js)
    for ki, k in enumerate(keys):
        v = js[k]
        end = "," if ki < len(keys) - 1 else ""
        if k in ("batch", "action"):
            out.append(f" {c(k)}: {{")
            nodes = list(v)
            for ni, n in enumerate(nodes):
                out.append(f"  {c(n)}: {{")
                attrs = list(v[n])
                for ai, a in enumerate(attrs):
                    out.append(f"   {c(a)}: {c(v[n][a])}" + ("," if ai < len(attrs) - 1 else ""))
                out.append("  }" + ("," if ni < len(nodes) - 1 else ""))
            out.append(" }" + end)
        elif k.endswith("_definitions"):
            out.append(f" {c(k)}: {{")
            attrs = list(v)
            for ai, a in enumerate(attrs):
                out.append(f"  {c(a)}: {c(v[a])}" + ("," if ai < len(attrs) - 1 else ""))
            out.append(" }" + end)
        else:
            out.append(f" {c(k)}: " + json.dumps(v, ensure_ascii=False, indent=1).replace("\n", "\n ") + end)
    out.append("}")
    return "\n".join(out) + "\n"


open(os.path.join(OUT, "node-attributes.json"), "w", encoding="utf-8").write(dump_js(js))

# README fragments (tables) -> written to scratch for hand-assembly
frag = []
for kind, label in (("batch", "Batch"), ("action", "Action object")):
    m = meta[kind]
    frag.append(f"<!-- COMMON {kind} -->")
    frag.append("| attr | type | description | value range | nodes listing it |")
    frag.append("|---|---|---|---|---|")
    for a, info in m["common_defs"].items():
        frag.append(row(a, info)[:-1] + f"| {m['common_count'][a]}/{m['N']} |")
    frag.append(f"<!-- RECURRING {kind} -->")
    frag.append("| attr | nodes (identical definition) |")
    frag.append("|---|---|")
    for a, nodes in recurring(kind):
        frag.append(f"| `{a}` | " + ", ".join(nodes) + " |")
    frag.append(f"<!-- INDEX {kind} -->")
    fname = "batch-nodes.md" if kind == "batch" else "action-nodes.md"
    frag.append("| node | specific attrs | missing common | link |")
    frag.append("|---|---|---|---|")
    for node in data[kind]:
        specific, differs, missing = node_parts(kind, node)
        frag.append(f"| {node} | {len(specific)} | "
                    + (", ".join(f"`{a}`" for a in missing) or "-")
                    + f" | [{fname}#{slug(node)}]({fname}#{slug(node)}) |")
open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "readme_fragments.md"), "w").write("\n".join(frag) + "\n")

# assemble README from template
HERE = os.path.dirname(os.path.abspath(__file__))
tpl = open(os.path.join(HERE, "README_template.md"), encoding="utf-8").read()
blocks, curk = {}, None
for line in frag:
    if line.startswith("<!-- "):
        curk = line
        blocks[curk] = []
    else:
        blocks[curk].append(line)
for k, v in blocks.items():
    assert k in tpl, k
    tpl = tpl.replace(k, "\n".join(v))
notes = []
for k in FILES:
    for f in meta[k]["fixes"]:
        notes.append(f"- {meta[k]['title']} — repaired: {f}")
notes += [l.rstrip("\n") for l in open(os.path.join(HERE, "manual_notes.md"), encoding="utf-8") if l.strip()]
tpl = tpl.replace("<!-- NOTES -->", "\n".join(notes))
open(os.path.join(OUT, "README.md"), "w", encoding="utf-8").write(tpl)


for k in FILES:
    m = meta[k]
    print(k, "sections", m["raw_sections"], "unique nodes", m["N"], "raw pairs", m["raw_pairs"],
          "unique pairs", sum(len(d) for d in data[k].values()), "common", m["common"], "dups", dict(m["dups"]))
