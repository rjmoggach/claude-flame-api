# claude-flame-api

A Claude skill that gives Claude the full **Autodesk Flame 2027 developer API** as context: the Python `flame` module (71 classes), hooks, custom UI actions, Batch/Action node attributes, Open Clip XML, Matchbox/Lightbox shaders, Pybox and the Inference Builder.

When you ask Claude to write, review or debug Flame tools, it routes through `skills/flame-api-2027/README.md` and reads the exact signatures and attribute names instead of guessing.

## Install

### Claude Desktop / claude.ai (chat)

1. Download `flame-api-2027.zip` from the [latest release](https://github.com/rjmoggach/claude-flame-api/releases), or build it yourself (see below).
2. In Claude Desktop, open **Settings → Capabilities**, make sure **Code execution and file creation** is on, then under **Skills** click **Upload skill** and choose the zip.
3. Switch the `flame-api-2027` skill on. Claude uses it automatically for Flame questions. You can also ask for it by name: *"use the flame-api skill"*.

### Claude Code (CLI, or the Code tab in Claude Desktop)

```
/plugin marketplace add rjmoggach/claude-flame-api
/plugin install flame-api@claude-flame-api
```

To get updates later, run `/plugin marketplace update claude-flame-api`.

## Try it

- "Write a Flame Python hook that adds a right-click action on media panel clips to export them as ProRes to /mnt/delivery."
- "In Batch, list every Action node and print the names of its media layers."
- "Write a Matchbox shader with a single float blur slider, including the XML."

## Layout

```
.claude-plugin/        plugin + marketplace manifests (Claude Code)
skills/flame-api-2027/ the skill: SKILL.md, routing README, api/, hooks/, nodes/, shaders/, ...
```

## Rebuilding the Desktop zip

```bash
python -I - <<'EOF'
import zipfile, pathlib
root = pathlib.Path("skills")
with zipfile.ZipFile("dist/flame-api-2027.zip", "w", zipfile.ZIP_DEFLATED) as z:
    for p in sorted((root / "flame-api-2027").rglob("*")):
        rel = p.relative_to(root)
        if p.is_file() and "_build" not in rel.parts:
            z.write(p, rel.as_posix())
EOF
```

Source: *Autodesk Flame Family 2027 Help* (84 pages, captured 2026-11-11). Flame and Autodesk are trademarks of Autodesk, Inc. This project is not affiliated with Autodesk.
