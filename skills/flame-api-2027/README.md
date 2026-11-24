# Autodesk Flame 2027 — Developer API Context Library

Structured, source-verified reference for coding agents building Flame Python scripts, hooks, custom menu actions, Batch/Action automation, Open Clip files, Matchbox/Lightbox shaders, Pybox handlers and Inference models.

Built from the official *Autodesk Flame Family 2027 Help* (84 pages, downloaded 2026-11-11). Everything here is traceable to those pages; inferred guidance is labelled **Agent note**. Where Autodesk's pages contradict themselves, the relevant file says so explicitly instead of guessing.

## Start here — route by task

| I need to… | Read |
|---|---|
| Understand how objects relate / how to reach a clip, reel, batch, segment | [api/object-model.md](api/object-model.md) |
| Look up a class, method signature, or attribute | [api/index.md](api/index.md) → `api/classes/<Class>.md` |
| Call a module-level function (`flame.find_by_uid`, `flame.import_clips`, `flame.execute_command`, …) | [api/flame-module-functions.md](api/flame-module-functions.md), [api/flame-module-data.md](api/flame-module-data.md) |
| Use anything new/changed in 2027 (metadata API, node markers, annotations, renamed members) | [guides/whats-new-2027.md](guides/whats-new-2027.md) — **authoritative over the pydoc where they differ** |
| Write a first script / run code in the Python console | [guides/getting-started.md](guides/getting-started.md) |
| Get exact option strings / constants / node type names | [guides/constants.md](guides/constants.md) |
| Write a hook (project, batch, export, tokens, app init) | [hooks/README.md](hooks/README.md) (full hook table + per-category files) |
| Add a right-click / main-menu custom action | [hooks/custom-ui-actions.md](hooks/custom-ui-actions.md) |
| Avoid known hook pitfalls (blocking, threading, reloading) | [hooks/tips-and-gotchas.md](hooks/tips-and-gotchas.md) |
| Read/set attributes on a specific Batch node or Action object | [nodes/README.md](nodes/README.md), [nodes/batch-nodes.md](nodes/batch-nodes.md), [nodes/action-nodes.md](nodes/action-nodes.md), [nodes/node-attributes.json](nodes/node-attributes.json) |
| Colour management (OCIO, colour spaces, context variables) | [guides/colour-management.md](guides/colour-management.md) |
| Find a working code sample | [examples/README.md](examples/README.md) (indexed by task and API used) |
| Generate / parse Open Clip (`.clip`) XML | [openclip/README.md](openclip/README.md), [openclip/elements.md](openclip/elements.md) |
| Write a Matchbox or Lightbox shader | [shaders/README.md](shaders/README.md), [shaders/shader-api.md](shaders/shader-api.md), [shaders/xml-reference.md](shaders/xml-reference.md) |
| Write a Pybox handler | [pybox/README.md](pybox/README.md) |
| Package an ONNX model for the Inference node | [inference/README.md](inference/README.md) |
| Check exact original wording | `_source_md/` (raw page conversions; `_source_md/pydoc/` = per-class pydoc) |

## Layout

```
README.md            this file (routing)
SKILL.md             Claude Code skill entry point
api/
  index.md           class hierarchy + table of every class with method/property names
  object-model.md    navigation tree, singletons, PyAttribute/PyTime semantics, threading rules
  flame-module-functions.md / flame-module-data.md
  classes/Py*.md     71 class files (68 pydoc + 3 stubs for 2027-only classes): signatures + documented attributes (+ 2027 banners)
guides/              getting-started, whats-new-2027, python-api-overview, constants, colour-management
examples/            224 verbatim code samples grouped by area, with index
hooks/               README (all hooks), project / batch / export / tokens / custom-ui-actions / other, tips
nodes/               per-node attributes for 92 Batch node types and 48 Action objects (+ JSON)
openclip/            Open Clip XML: element reference, Creator tool, metadata edits, examples
shaders/             Matchbox / Lightbox: API, XML schema, presets, examples
pybox/  inference/   Pybox handler protocol; Inference Builder
_source_md/          raw Markdown conversions of all 84 help pages (ground-truth fallback)
_build/              scripts that regenerated this library from the HTML download
```

## Core rules for agents (all sourced; details in linked files)

1. **`import flame`** is only available inside Flame (hooks, Python console, scripts run by Flame). Classes cannot be instantiated except `PyTime`, `PyResolution`, `PyExporter`; obtain objects from singletons (`flame.projects.current_project`, `flame.batch`, `flame.media_panel`, `flame.timeline`, …).
2. **Attributes return `PyAttribute` wrappers.** Use `.get_value()` to get a real Python value and `.set_value(v)` (or assignment) to write. See [api/object-model.md §5](api/object-model.md).
3. **The pydoc class reference predates part of the 2027 API.** Class files with 2027 changes carry a banner; always check [guides/whats-new-2027.md](guides/whats-new-2027.md). `PyMetadataNode`, `PyMetadataTimelineFX`, `PyNodeMarker` exist only there.
4. **Hooks block the UI.** Keep them fast; use threads (pattern in hooks docs) or `flame.schedule_idle_event()` for main-thread callbacks; use `flame.execute_command()` instead of `subprocess` (avoids forking Flame; env vars are not forwarded).
5. **Hook signatures:** the help documents argument names and `info` keys but rarely full `def` lines. The installed no-op hook files in `/opt/Autodesk/<PRODUCT>_<VERSION>/python/` are the definitive signatures — read them on a Flame machine when available.
6. **Autodesk's own samples contain bugs** (syntax errors, wrong attribute names). The examples and shader files flag each one next to the sample; don't copy flagged lines blindly.
7. Python version per the 2027 docs: see [guides/getting-started.md](guides/getting-started.md) (Pybox page still says 2.7 — likely stale; see [pybox/README.md](pybox/README.md)).

## Known source limitations

- Undocumented in the help: full hook `def` signatures, per-menu `selection` contents for custom UI actions, export-hook `info` keys, Pybox JSON payload schema, Inference `ColourSpace` allowed values.
- Inconsistent in the help: Open Clip format `version` (7/8/9), export hook name spelling, `ResDependant`/`ResDependent`, `PopUp`/`Popup`.
Each file's "Source notes"/"ambiguities" section lists specifics. When behaviour matters, verify at runtime (`obj.attributes`, `PyAttribute.values`, `flame.batch.node_types`, `dir(flame)`).
