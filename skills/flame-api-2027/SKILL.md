---
name: flame-api-2027
description: Autodesk Flame 2027 developer API reference — Python `flame` module classes and signatures, Python hooks (project, batch, export, tokens, custom UI actions), Batch/Action node attributes, Open Clip XML, Matchbox/Lightbox shaders, Pybox, Inference Builder. Use whenever writing, reviewing or debugging code that runs inside Autodesk Flame / Flare / Flame Assist, imports `flame`, defines Flame hooks or menu actions, generates .clip files, or builds Flame shaders/Pybox/Inference models.
---

# Flame 2027 API context library

Before writing Flame code, read `README.md` in this directory (task → file routing table), then open only the files it points to. Do not answer Flame API questions from memory — signatures and attribute names must come from these files.

Key reminders:
- Check `guides/whats-new-2027.md` for anything 2027-specific; the pydoc-derived `api/classes/` predates part of 2027 (affected files carry a banner).
- Attribute access returns `PyAttribute`; use `.get_value()` / `.set_value()`.
- Hooks block the UI; use `flame.execute_command()` not `subprocess`.
- Flagged lines in Autodesk samples are buggy — don't copy them.
- To search: `grep -rn "<identifier>" <this dir>` — identifiers are backticked and exact; `_source_md/` holds original page text.
