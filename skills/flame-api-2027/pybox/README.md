> Source: Autodesk Flame Family 2027 Help — "Pybox" (code verified against the original HTML). Cross-reference: "Flame Python API Code Samples" (`create_node("Pybox", …)`).

# Pybox — reference

Pybox lets third-party applications (usually renderers) integrate into the Batch compositing pipeline — the Python counterpart of Matchbox. The artist adds a **Pybox node** (Batch) or **Pybox Timeline FX** and loads a **handler** (your Python file). The handler builds the node UI, declares input/output sockets, exchanges image files with the external process, and communicates with Flame only through a **JSON payload file**. A Pybox can execute any code; it is not limited to producing images.

The full module API is **not** reproduced in the help page: read `/opt/Autodesk/shared/presets/pybox/pybox_v1.py` (and the API doc linked from the help page: `http://www.autodesk.com/pybox-api-doc`). This file documents everything the help page states; anything not listed here must be checked in `pybox_v1.py`.

## Contents

- [Constraints](#what-pybox-is-not) · [Requirements & install](#development-requirements) · [Lifecycle](#loading--unloading) · [Protocol & states](#protocol-json-payload-and-states) · [Minimal handler](#minimal-handler) · [Sockets](#sockets-initialize) · [Colour space](#forcing-output-colour-space) · [UI](#ui-setup_ui) · [Metadata](#frame-related-metadata-getters) · [Messages](#messages--errors) · [API summary](#api-summary) · [Samples](#shipped-samples) · [Nuke](#nuke-handler-example) · [Glossary](#glossary)

## What Pybox is not

- **Not real-time**: external processes are expected to take time; playback of a pipeline with Pybox nodes is not guaranteed real-time.
- **Not a caching mechanism**: Batch's caching is already used by Pybox at the node level.
- **Not an API to the rendering pipeline**: no direct access to renderers; Pybox injects information *into* the pipeline, it does not extract it.

## Development requirements

- Docs state: "Pybox handlers are written in **Python 2.7**." (See Ambiguities — likely outdated.)
- Use the module `pybox_v1`, loaded automatically by Flame at launch; its directory is added to Flame's Python path at startup:
  ```python
  import pybox_v1 as pybox
  ```
- Module location: `/opt/Autodesk/shared/presets/pybox/pybox_v1.py`.
- **Custom modules** you write must be copied next to `pybox_v1.py` in `/opt/Autodesk/shared/presets/pybox` (the one exception to "no packaging"). Standard library modules (`os`, `sys`, `tempfile`, …) import normally.
- Handler samples: `/opt/Autodesk/presets/<version>/pybox/`.
- **Distribution**: no special packaging — distribute the `.py` handler; artists can load it from anywhere via a Pybox node or Timeline FX.
- Python API: `flame.batch.create_node("Pybox", "sendmail.py")` creates a Pybox node with a handler from the default path.

## Loading / unloading

- A handler is **loaded** when the artist clicks **Load** in the handler browser (shown when a Pybox node is created or on **Change Handler**). It is **reloaded from disk every time**, even if the same handler is selected — no need to restart Flame between iterations; there is no caching.
- A handler is also loaded when the Pybox is **duplicated**.
- A handler is **unloaded** when its Pybox is removed from the Batch schematic or Timeline, or when another handler is loaded in its place.

## Protocol: JSON payload and states

- Three components: image files written by Flame (inputs), image files written by the external processor (outputs), and the **JSON payload**.
- The handler does not interact with Flame directly. Everything goes through a temporary JSON file created by Flame. Flame "only looks at and communicates through the JSON payload, it does not execute the script" (i.e., Flame invokes the handler; the handler reads/writes the payload — see Minimal handler).
- The pipeline is **stateless and synchronous**.
- States: `initialize` → `setup_ui` → `execute` → `teardown` (method names on your `pybox.BaseClass` subclass).
- **Flame never changes the state by itself.** The handler sets it with `set_state_id("<state>")`; once Flame reads it from the payload, Flame always calls the handler with that same state. E.g. in `initialize`, Flame will not call with `execute` unless the handler called `set_state_id("execute")`. Flame can only query the state and return UI object values.
- "The handler does not move to the next step unless told to. That is, Flame does not drive the handler, the handler does."
- You may call methods out of order (e.g. `self.execute()` from `initialize()`, bypassing `setup_ui()`), but you may lack the inputs needed for a valid render.

State ids used in the docs (strings): `"setup_ui"`, `"execute"`, `"teardown"`; the initial state is referred to as `initialize`.

## Minimal handler

Does nothing, but shows the structure (verbatim):

```python
import sys
import pybox_v1 as pybox

class HelloWorld(pybox.BaseClass):

    def initialize(self):
        self.set_state_id("setup_ui")
        self.setup_ui()

    def setup_ui(self):
        self.set_state_id("execute")
        self.execute()

    def execute(self):
        self.set_state_id("teardown")
        self.teardown()

    def teardown(self):
        pass

def _main(argv):

    p = HelloWorld(argv[0])
    p.dispatch()
    p.write_to_disk(argv[0])

if __name__ == '__main__':
    _main(sys.argv[1:])
```

- `pybox.BaseClass(argv[0])`: the handler object is constructed from the first script argument.
- `p.dispatch()`: executes `initialize()`, `setup_ui()`, `execute()` or `teardown()` according to the current state (docs: "set by `self.state_id()`" — the setter shown everywhere is `set_state_id()`).
- `p.write_to_disk(argv[0])`: writes the JSON file to disk so Flame can read it.
- This loads correctly but logs errors because it defines no output socket — expected.

> Agent note (inferred, not stated): since the same `argv[0]` is passed to the constructor and to `write_to_disk`, it is evidently the path of the JSON payload file that Flame passes on the command line. Keep the `_main` boilerplate exactly as shown.

## Sockets (`initialize`)

```python
def initialize(self):
    self.set_img_format("exr")

    self.set_in_socket(0, "Front", "/tmp/in_front.exr")
    self.set_in_socket(1, "Matte", "/tmp/in_matte.exr")

    self.set_out_socket(0, "Result", "/tmp/in_front.exr")
    self.set_out_socket(1, "OutMatte", "/tmp/in_matte.exr")

    self.set_state_id("setup_ui")
    self.setup_ui()
```

- `set_img_format(fmt)` — **required**: the image format Flame uses when exporting image files (e.g. `"exr"`). Read back with `get_img_format()`.
- `set_in_socket(idx, type, path)` — input socket: index, data type, and the path **Flame writes** the image to (Flame needs write access). In Batch, connects upstream RGB data.
- `set_out_socket(idx, type, path, colour_space="")` — output socket: index, data type, and the path **Flame reads** the image from (Flame needs read access).
- Socket type strings in the docs: inputs `"Front"`, `"Matte"`; outputs `"Result"`, `"OutMatte"`. (No exhaustive list is given; e.g. whether `"Back"` is valid is not stated.)
- Note: in this sample the outputs point at the *input* files (`/tmp/in_front.exr`, `/tmp/in_matte.exr`), i.e. a pass-through. Real handlers point outputs at the files the external process writes.
- Performance: the main bottleneck is disk I/O (no RAM exchange). Put these paths on fast storage — ideally a **RAM disk**.

## Forcing output colour space

By default output frames are tagged with the default colour space of the socket type (e.g. `OutMatte` → **Matte** data colour space). A handler can force it:

```python
def initialize(self):
    self.set_img_format("exr")

    self.set_in_socket(0, "Front", "/tmp/in_front.exr")

    self.set_out_socket(0, "Result", "/tmp/out_result.exr", colour_space="ACEScg")
    self.set_out_socket(1, "OutMatte", "/tmp/out_matte.exr", colour_space="Matte")

    self.set_state_id("setup_ui")
    self.setup_ui()
```

| Method (`pybox_v1.BaseClass`) | Description |
|---|---|
| `set_out_socket(idx, socket_type, path, colour_space="")` | Define output socket `idx`; optional `colour_space` forces its tagged colour space. |
| `add_out_socket(socket_type, path, colour_space="")` | Add an output socket at the next available index; optional `colour_space`. |
| `get_out_socket_colour_space(idx)` | Forced colour space of output `idx`, or `""` if none. |
| `set_out_socket_colour_space(idx, colour_space)` | Force the colour space of existing output `idx`; `""` clears it. |

- `colour_space` accepts names shown in the Pybox node's **Tagged Colour Space** drop-down, plus data colour spaces: `3D-Motion`, `Matte`, `Motion`, `Normals`, `Position`, `UV`, `Z-Depth`.
- `""` (default) keeps the socket type's default. An unrecognised name is ignored (default kept) and a warning is logged.
- A forced colour space overrides the artist's **Tagged Colour Space** choice. If `Result` is forced and **Output Resolution** = **User-Defined**, the section shows the forced space as a non-editable value.
- `no_op.py` contains a commented example.

## UI (`setup_ui`)

```python
def setup_ui(self):
    blurAmount = pybox.create_float_numeric( "Blur Amount", value=0.0, min=0.0, max=100.0 )
    self.add_render_elements(blurAmount)

    page = pybox.create_page( "Main Page", "Blur Settings" )
    self.set_ui_pages(page)

    self.set_state_id("execute")
    self.execute()
```

- Creates a numeric field **Blur Amount** (default 0, min 0, max 100) in page **Main Page** under the column heading **Blur Settings**.
- Every UI element must be assigned to the **render pool** or the **global pool**:
  - Render pool (`self.add_render_elements(...)`): queried only when the node is asked to render (its Result view is displayed or a downstream node requests a frame). Use for things that affect the render (e.g. blur amount).
  - Global pool: always triggers a Python call; affects the Pybox itself (e.g. a button opening a browser to select a setup). **The method name for adding global elements is not given on the help page** — check `pybox_v1.py`.
- `pybox.create_page(name, first_column_heading)`: creates the JSON object defining a page (arg 1 = page name, arg 2 = heading of the first column).
- `self.set_ui_pages(page)`: required for the page to appear.

Supported UI elements (`pybox_v1` module-level functions):

| UI element | Function |
|---|---|
| Floating point field | `create_float_numeric()` (signature seen: `create_float_numeric(name, value=…, min=…, max=…)`) |
| Floating point numeric, 2 fields | `create_vector_numeric()` with `size = 2` |
| Floating point numeric, 3 fields | `create_vector_numeric()` with `size = 3` |
| Drop-down | `create_popup()` |
| Colour pot | `create_color()` |
| Button (toggle) | `create_toggle_button()` |
| File browser field and button | `create_file_browser()` |

Parameters of these functions (other than the `create_float_numeric` example and `size`) are not documented on the help page. Reading UI values back is described only as "Flame can … return user interface object values" through the payload; see the `event_handling` / `random_ui.py` samples and `pybox_v1.py`.

## Frame-related metadata getters

`pybox_v1.BaseClass` methods:

| Metadata | Method |
|---|---|
| Bit depth of the current batch default | `get_bit_depth()` |
| Colour space of the project | `get_colour_space()` |
| Today's date | `get_date()` |
| Today's day | `get_date_day()` |
| Today's month | `get_date_month()` |
| Today's year | `get_date_year()` |
| Current Batch frame | `get_frame()` |
| Frame ratio of the current batch default | `get_frame_ratio()` |
| Frame rate | `get_framerate()` |
| Height of the current batch default | `get_height()` |
| Image format set by `set_img_format` | `get_img_format()` |
| Nickname of the user | `get_nickname()` |
| Node name (Batch Node Name field) | `get_node_name()` |
| Flame project name | `get_project()` |
| Flame project nickname | `get_project_nickname()` |
| Record timecode of the current frame | `get_record_time_code()` |
| `width`, `bit_depth`, `frame_ratio`, `height` of the current batch default | `get_resolution()` |
| Source timecode of the current frame | `get_source_time_code()` |
| Current user name | `get_user()` |
| Width of the current batch default | `get_width()` |
| Workstation name | `get_workstation()` |

Return types/formats are not documented (`get_resolution()` evidently returns a structure with keys/fields `width`, `bit_depth`, `frame_ratio`, `height`; exact type not stated).

## Messages & errors

Messages go through the JSON payload and appear in Flame's message console, the shell, and the log. Ordered by severity, highest first:

| Read | Write |
|---|---|
| `get_error_msg()` | `set_error_msg()` |
| `get_warning_msg()` | `set_warning_msg()` |
| `get_notice_msg()` | `set_notice_msg()` |
| `get_debug_msg()` | `set_debug_msg()` |

Debugging tips from the docs:
- **Esc** interrupts a Pybox from within Flame.
- A Pybox processes whenever a frame is requested; showing anything other than its Result view (**F4**) prevents processing — useful to keep interactivity while troubleshooting.
- **Change Handler** reloads from scratch (no caching) — use it after every edit.
- Wrap code in `try…except`.

## API summary

Everything the help page names. Signatures beyond those shown are not documented there.

| Name | Kind | Purpose |
|---|---|---|
| `pybox_v1` | module | Import as `pybox`. |
| `pybox.BaseClass` | class | Subclass it; construct with `argv[0]`. |
| `initialize`, `setup_ui`, `execute`, `teardown` | methods you implement | State handlers. |
| `dispatch()` | BaseClass | Run the method for the current state. |
| `write_to_disk(path)` | BaseClass | Write the JSON payload for Flame. |
| `set_state_id(state)` | BaseClass | Set next state (`"setup_ui"`, `"execute"`, `"teardown"`). |
| `set_img_format(fmt)` / `get_img_format()` | BaseClass | Image exchange format. |
| `set_in_socket(idx, type, path)` | BaseClass | Declare input socket. |
| `set_out_socket(idx, socket_type, path, colour_space="")` | BaseClass | Declare output socket. |
| `add_out_socket(socket_type, path, colour_space="")` | BaseClass | Append output socket. |
| `get_out_socket_colour_space(idx)` / `set_out_socket_colour_space(idx, colour_space)` | BaseClass | Forced output colour space. |
| `add_render_elements(element)` | BaseClass | Add UI element(s) to the render pool (docs only show a single element argument; multi-argument form not documented). |
| `set_ui_pages(page)` | BaseClass | Register UI page(s). |
| `create_page(name, column_heading)` | module | Page JSON object. |
| `create_float_numeric`, `create_vector_numeric`, `create_popup`, `create_color`, `create_toggle_button`, `create_file_browser` | module | UI element constructors. |
| `get_*` metadata methods | BaseClass | See table above. |
| `get/set_error_msg`, `get/set_warning_msg`, `get/set_notice_msg`, `get/set_debug_msg` | BaseClass | Messaging. |

## Shipped samples

In `/opt/Autodesk/presets/<version>/pybox/`:

| Handler | Demonstrates |
|---|---|
| `event_handling` | Handling UI changes after user input; dynamic UI page whose objects are labelled with the event they trigger. |
| `image_magick.py` | Blur via ImageMagick (must be installed; not installed by default on Rocky Linux). |
| `image_magick_polaroid.py` | Polaroid effect via ImageMagick (same requirement). |
| `no_op.py` | Simplest handler: pass-through (front → result, matte forwarded); includes a commented forced-colour-space example. |
| `print_process_infos.py` | Getting processing information and printing it to the shell. |
| `random_ui.py` | Variation of `event_handling.py` with random UI; shows helper functions outside the `pybox.BaseClass` subclass. |
| `sendmail.py` | A Pybox with no input or output sockets, generating/processing arbitrary information. |

## Nuke handler example

Illustrative, not a complete solution. Files:

- `/opt/Autodesk/presets/<version>/pybox/nuke_px.py` — the handler loaded in the Pybox node.
- `/opt/Autodesk/shared/presets/pybox/nuke_parse_io.py` — manages IO.
- `/opt/Autodesk/shared/presets/pybox/nuke_parse_ui.py` — manages UI interactions.
- `/opt/Autodesk/shared/presets/pybox/nuke_parse_exec.py`

Setup: edit `nuke_px.py` — set `NUKE_PATH` to your Nuke install; on macOS make sure `PAYLOAD_PATH` resolves. If slow, change the `filename` variable in `nuke_parse_io.py` and `nuke_exec.py` (sic) from the OS temp dir to fast storage:

```python
filename = tempfile.gettempdir() + "/" + node.name() + ".exr"
```

to e.g.:

```python
filename = "/path/to_directory/on_fast_storage/" + node.name() + ".exr"
```

Exposing Nuke knobs in the Pybox UI: a Nuke node whose name starts with `adsk_` has its knobs exposed if the knob names also start with `adsk_`:

```text
Group {
 name adsk_UI
 xpos -282
 ypos -31
 addUserKnob {20 User}
 addUserKnob {41 adsk_translate l translate T Transform1.translate}
 addUserKnob {41 adsk_scale l scale T Transform1.scale}
 addUserKnob {41 adsk_saturation l saturation T ColorCorrect1.saturation}
 addUserKnob {41 adsk_contrast l contrast T ColorCorrect1.contrast}
 addUserKnob {41 adsk_gamma l gamma T ColorCorrect1.gamma}
 addUserKnob {41 adsk_gain l gain T ColorCorrect1.gain}
}
```

Write node requirements: named `adsk_1_result` or `adsk_2_matte` (per the prose; the sample uses `adsk_1_Result` and `adsk_2_OutMatte`); fed by a Shuffle; must output **8- or 16-bit RGB** (RGBA not supported).

```text
set N614d650 [stack 0]
Shuffle {
 red alpha
 green alpha
 blue alpha
 name Shuffle2
 xpos 22
 ypos 17
}
Write {
 in_colorspace linear
 out_colorspace linear
 name adsk_2_OutMatte
 xpos 180
 ypos 17
}
push $N614d650
Shuffle {
 alpha white
 name Shuffle1
 xpos 29
 ypos -62
}
Write {
 in_colorspace linear
 out_colorspace linear
 name adsk_1_Result
 xpos 177
 ypos -62
}
```

## Glossary

- **Pybox**: (1) the feature letting artists use third-party applications in a Batch Group or Timeline as part of Flame's pipeline; (2) the Batch node / Timeline FX itself (as opposed to the handler).
- **Flame Artist**: the Flame user (not the handler developer).
- **Handler**: the Python file written by a developer and loaded in a Pybox node/Timeline FX; creates the UI, reads/writes the JSON payload, interacts with the third-party application.
- **JSON Payload**: temporary file created by Flame and used to communicate with the handler.

## Batch context (from the docs)

A Batch process tree starts with a clip, contains nodes, and ends with a Render, Write File, or BFX Output node. Inputs (source tabs, left, colour-coded: front, matte, back) and the yellow **Result** output tab (some nodes also have a blue **OutMatte** tab). Pybox sockets map onto these.

## Ambiguities in the source

- **Python version**: the page says handlers are written in Python 2.7 and links the Python 2 tutorial for `try…except`. No other page in the 2027 help set states a Python version. The statement may be stale; check the shipped `pybox_v1.py` and samples for the syntax actually expected (code valid in both 2 and 3 is the safe choice).
- `dispatch` description references `self.state_id()`; the documented setter is `set_state_id()`. A getter is not documented.
- The global-pool method name is not given.
- Nuke Write node names: prose `adsk_1_result` / `adsk_2_matte` vs sample `adsk_1_Result` / `adsk_2_OutMatte`; prose mentions `nuke_exec.py` while the file list has `nuke_parse_exec.py`.
- `no_op.py` description says "the input matte is forwarded to the result output" (probably meant OutMatte).
- In the first `initialize` example, outputs point at the input file paths.
- The JSON payload schema is not documented; only interact with it through `pybox_v1`.
