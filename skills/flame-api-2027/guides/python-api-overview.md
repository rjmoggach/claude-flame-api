> Source: Python API; Python API Examples — Autodesk Flame Family 2027 Help

# Flame Python API — Overview

## What it is (from the source)

- The Flame Family Python API is a tool for Flame, Flare, and Flame Assist users looking to script workflows and automate tedious tasks.
- The Python API is accessed via the Flame Python Console. This console provides a place to write and execute code while working in Flame.
- The `flame` module is the core of the Python API. This module contains everything needed to use the Flame Python API.
- The Python API uses **Python version 3.13.3**, starting with Flame Family 2027.
- Note: Some functions and attributes may not be available in Flare or Flame Assist.

## New to the Flame Python API?

- *Write Your First Python API Script* provides a small and basic example to get started → [getting-started.md](getting-started.md#write-your-first-script-walkthrough).
- *Flame API Code Samples* contains code snippets that offer ideas on the structure of the API and how to use it → [../examples/README.md](../examples/README.md).
- Examples of scripts can also be found in `/opt/Autodesk/<flame_version>/python_examples`.

## About the examples (from "Python API Examples")

The examples range in difficulty and can be incorporated within any Flame project with some modification. As with any programming language, there are many ways to achieve the same result; the examples may only show one way of performing a task. Comments have been inserted within the scripts to describe parts of the code (Python comments start with `#`).

Example pages: Flame Python API Code Samples, Importing Multi-Channel Clip, Render Passes with the Python API, Looping by Node Type, Colour Management API — all indexed in [../examples/README.md](../examples/README.md).

## Placeholder convention used throughout the docs

In the official samples, bracketed names such as `<PyClip>` are shorthand for objects obtained from the `flame` API (they are not valid Python). See [constants.md](constants.md) ("Defines for the flame Module") for the access path to each object type.

## Map of the Python API documentation pages (source page → this library)

| Official page | Where it lives here |
|---|---|
| Python API (overview) | this file |
| Python API → What's New in 2027 | [whats-new-2027.md](whats-new-2027.md) |
| Python Console and how to Execute Scripts | [getting-started.md](getting-started.md) |
| Write Your First Python API Script | [getting-started.md](getting-started.md) |
| Defines for the flame Module | [constants.md](constants.md) |
| Colour Management API | [colour-management.md](colour-management.md) |
| Python API Examples / Flame Python API Code Samples / Looping by Node Type / Render Passes / Importing Multi-Channel Clip | [../examples/](../examples/README.md) |
| Autodesk Flame Python: flame module | [../api/](../api/) (class reference, module functions, module data) |
| What's New in Previous Releases | not covered in this library (listed as a related page in the source) |

## Key module-level entry points seen in these sources

Agent note — collected from the samples only; see [../api/flame-module-data.md](../api/flame-module-data.md) and [../api/flame-module-functions.md](../api/flame-module-functions.md) for the authoritative lists.

| Entry point | Used for (in samples) |
|---|---|
| `flame.batch` | Current Batch group (`PyBatch`): `create_batch_group`, `create_node`, `connect_nodes`, `import_clip`, `organize`, `go_to`, `get_node`, `nodes`, `current_node`, `current_frame` |
| `flame.projects.current_project` | Current `PyProject`: workspace, libraries, colour-management settings |
| `flame.timeline` | Current timeline: `clip`, `current_segment` |
| `flame.media_panel` | `move`, `copy`, `selected_entries`, `visible`, `full_width`, `full_height`, `dual` |
| `flame.mediahub` | `files.options.set_tagged_colour_space(...)` |
| `flame.users` | `current_user.name`, `current_user.nickname` |
| `flame.import_clips(path, destination)` | Import media into a library / reel |
| `flame.find_by_name(name)` | Returns a list (samples index `[0]`) |
| `flame.execute_shortcut(name)` | Run a keyboard-shortcut action, e.g. `"Overwrite Edit"` |
| `flame.get_current_tab()` / `flame.set_current_tab(name)` | Read / change the active tab, e.g. `"Timeline"` |
| `flame.PyTime(...)` | Time values (timecode + rate, or frame) |
| `flame.clear_unreferenced_cache()`, `flame.clear_graphics_memory()` | New / renamed in 2027 |
