<!-- source: Autodesk Flame Family 2027 Help _ Pybox _ Autodesk.html -->
# Pybox

Pybox is a tool available in Batch and the Timeline.

---

## What Pybox Is

Pybox allows third-party applications, renderers in most cases, to integrate into Batch compositing pipeline, similar to how Matchbox allows GLSL snippets to integrate the same pipeline: a Batch node with user interface that can load a handler. This node allows a Flame artist to essentially radio-control the third-party renderer from within Batch.

One could create a Pybox that uses Maya to render content, and then have that content fed back into the Batch pipeline. Seamlessly. The artist simply adds a Pybox node to the Batch schematic, and selects the correct handler.

Finally, a Pybox can execute any code in Batch the pipeline. It is not limited to producing images.

---

## What Pybox is Not

Although Pybox is a very flexible, there are some important constraints:

---

## Pybox is not a Tool to Render in Real Time

Pybox was not designed to render real-time images from other applications. A Pybox node fully expects external processes to take their time to render anything, and in most cases this means less than real-time speeds. So, playback of a pipeline containing any number of Pybox nodes cannot be guaranteed to be real-time.

---

## Pybox was not Designed to be a Caching Mechanism

The Batch pipeline already has its caching mechanism, and this mechanism is used by Pybox at the node level.

---

## Pybox is not an API to Access the Rendering Pipeline

Pybox is not intended to be an API access to the rendering pipeline. There is no direct access to the renderers. Pybox is essentially a mechanism to inject back information *into* the pipeline, not a mechanism to extract info.

---

## Pybox Development Requirements

Pybox handlers are written in Python 2.7.

A Python handler should use the Pybox Python module `pybox_v1`. Flame automatically loads this module at launch. The following line is sufficient to load the Pybox module from your Python script.

`python
import pybox_v1 as pybox
`

You can read `pybox_v1.py` in `/opt/Autodesk/shared/presets/pybox/`. API documentation for the module can be downloaded from this location.

To import additional python modules you develop, copy them to the `pybox_v1.py` directory (`/opt/Autodesk/shared/presets/pybox`). Standard Python extensions (`os`, `sys`, `tempfile`…) can be imported as usual and do not need to be relocated.

You can find Pybox handler samples in `/opt/Autodesk/presets/<version>/pybox/`.

### Distributing and Installing Pybox Handlers

There is no special packaging for Pybox handlers: simply distribute the python file. Any Flame artist can load it from anywhere through a Pybox node or Timeline FX.

There is one important exception: if you create custom modules, these modules must be co-located with pybox_v1.py, in `/opt/Autodesk/shared/presets/pybox`.

---

## Batch Overview

Batch provides a flow graph environment for procedural compositing with integrated access to almost all Flame effects and image-processing commands. A Flame artist uses the Batch tab to enter the Batch view. He can switch between tabs such as Timeline and Tools without losing any current work in Batch.

A Flame artist uses the Batch processing environment to assemble a process tree of clips and nodes, where the result of each operation serves as the source for the next one. A Batch pipeline is never fixed, giving the flexibility to reorder and edit nodes as necessary to achieve an effect.

A process tree begins with a clip, contains at least one node, and ends with a Render, Write File, or BFX Output node (a BFX tree invariably ends with a BFX Output node).

Nodes have one or more colour-coded input and output points (also called tabs) used for connecting to clips and to other nodes. All nodes have an output tab. For example, a Colour Correct node can accept a Front, Matte, and Back connection, whereas a 2D Histogram node accepts a Front connection.

When adding nodes, the Flame artist connects them to the process tree by linking the result from one node and using it as a source (front, matte, or back) for the next node in the process tree.

To connect nodes, the Flame artist uses the coloured tabs on the node's left side known as source tabs. The colours of the source tabs represent different input types. The yellow tab on the right side of the node is called the Result tab (for some nodes, a blue tab is also present on the right side, this is the OutMatte tab). The Flame artist uses the Result tab of a node to connect its result to the input tab of another node.

### Loading a Pybox

From the artist's point of view, Pybox consists of two elements: the node and the handler. The node is provided by the Flame application, and is accessible from both Timeline and Batch environments. From this node, the artist loads a Handler. This Handler is the Python file you will have coded and that actually interacts with the external process.

So, when is a Pybox loaded? When the artist clicks Load in the handler browser. That browser appears whenever a Pybox node is loaded, or when the artist clicks Change Handler in the Pybox node UI. This means that every time a handler is selected, it is reloaded from disk, even if the same handler is selected. So when developing a handler, there is no need to restart Flame between iterations: simply reload the handler.

Also, a handler is also loaded whenever a Pybox is duplicated by the artist.

### Unloading a Pybox

At the other end of the Pybox loading is the Pybox unloading. A handler is unloaded whenever the Pybox that loaded it is removed from the Batch schematic or from the Timeline.

A handler is also unloaded when another handler is loaded in its place in a Pybox.

---

## Writing a Simple Pybox

A Pybox python script consists at least of a main() creating a Pybox object.

### Minimal Pybox

This is what a minimalist Pybox handler looks like. Minimalist as it does nothing, but does illustrate the structure of a Pybox handler.

`python
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
`

A few comments regarding the above code sample:

-
`import pybox_v1 as pybox`: It is highly recommended that you use the `pybox_v1` Python module provided with Flame. This module is installed in `/opt/Autodesk/shared/presets/pybox`. You do not have to worry about this path resolving at runtime: it is automatically added to Flame's Python environment path when Flame is started.

-
`p.dispatch`: Execute each of the `initialize()`, `setup_ui()`, `execute()` or `teardown()` methods, based in on the current state set by `self.state_id()`.

-
`p.write_to_disk`: Writes to disk the JSON file so it can be read by Flame.

 Important: The above example will load correctly in Pybox, but will display errors in the log since it has no defined output socket. This is expected.

### `def initialize`: Setting Inputs and Outputs

In the example below, `initialize()` sets the image format used for the export, and initialize the input and output sockets of the Pybox node.

`python
def initialize(self):
    self.set_img_format("exr")

    self.set_in_socket(0, "Front", "/tmp/in_front.exr")
    self.set_in_socket(1, "Matte", "/tmp/in_matte.exr")

    self.set_out_socket(0, "Result", "/tmp/in_front.exr")
    self.set_out_socket(1, "OutMatte", "/tmp/in_matte.exr")

    self.set_state_id("setup_ui")
    self.setup_ui()
`

A few comments regarding the above code sample:

-
`set_img_format()`: You must tell Flame what format to use when exporting the image files.

-
`set_in_socket()`: Defines the sockets available to the Pybox node. Each Input socket must be provided index, data type, and the path to write the image file. Flame must have write-access to this path. In Batch, an Input socket is used by the Flame artist to connect the Pybox node into the Batch pipeline and pulls RGB data from an upstream node.

-
`set_out_socket()`: Defines the Output sockets available to the Pybox node. Each Output socket must be provided index, data type, and a path to read the image file from. Flame must have read-access to this path. In Batch, an Output socket is used by the Flame artist to connect the Pybox node the Batch pipeline. pulls RGB data from an upstream node.

-
`set_state_id()`: Signifies to Flame that the Handler is moving to the user interface setup phase.

-
`setup_ui()`: Calls the `setup_ui()` method as the next step. The handler does not move to the next step unless told to. That is, Flame does not drive the handler, the handler does. Remember, Flame only looks at and communicates through the JSON payload, it does not execute the script.

### Forcing the Colour Space of an Output

By default, Flame tags the frames of an output socket with the default colour space for that socket type. For example, frames from an `OutMatte` socket are tagged with the **Matte** data colour space. A handler can override the tagged colour space of an output socket. This is useful when the external application outputs frames in a known colour space or outputs data rather than colour, such as a depth pass.

In the example below, the `Result` output is tagged as **ACEScg** and the `OutMatte` output is tagged as **Matte**.

`python
def initialize(self):
    self.set_img_format("exr")

    self.set_in_socket(0, "Front", "/tmp/in_front.exr")

    self.set_out_socket(0, "Result", "/tmp/out_result.exr", colour_space="ACEScg")
    self.set_out_socket(1, "OutMatte", "/tmp/out_matte.exr", colour_space="Matte")

    self.set_state_id("setup_ui")
    self.setup_ui()
`

The following `pybox_v1.BaseClass` methods set and query the forced colour space of an output socket.

| Method | Description |
|---|---|
| `set_out_socket(idx, socket_type, path, colour_space="")` | Defines the output socket at index `idx`. The optional `colour_space` argument forces the tagged colour space of the socket. |
| `add_out_socket(socket_type, path, colour_space="")` | Adds an output socket at the next available index. The optional `colour_space` argument forces the tagged colour space of the socket. |
| `get_out_socket_colour_space(idx)` | Returns the colour space forced on the output socket at index `idx`, or an empty string when no colour space is forced. |
| `set_out_socket_colour_space(idx, colour_space)` | Forces the tagged colour space of the existing output socket at index `idx`. An empty string clears a previously forced colour space. |

The `colour_space` argument accepts the names displayed in the **Tagged Colour Space** drop-down of the Pybox node, as well as the following data colour spaces: **3D-Motion**, **Matte**, **Motion**, **Normals**, **Position**, **UV**, and **Z-Depth**. An empty string, the default, keeps the default colour space of the socket type. A name that Flame does not recognise is ignored: the socket keeps its default colour space, and a warning is written to the application log.

A forced colour space takes precedence over the colour space selected by the Flame artist in the **Tagged Colour Space** section of the Pybox node. When the handler forces the colour space of the `Result` output socket, and **Output Resolution** is set to **User-Defined**, the **Tagged Colour Space** section displays the forced colour space as a non-editable value instead of the drop-down.

The `no_op.py` handler sample includes a commented example of a forced colour space.

### `def setup_ui`: Creating the Pybox Node UI

`setup_ui()` is the method where the Pybox user interface is created. In the example below, a numeric field named Blur Amount is created in the tab Main Page of the Pybox node, under the Blur Settings heading. The Blur Amount field has a default value of 0, with minimum value of 0 and maximum value of 100.

`python
def setup_ui(self):
    blurAmount = pybox.create_float_numeric( "Blur Amount", value=0.0, min=0.0, max=100.0 )
    self.add_render_elements(blurAmount)

    page = pybox.create_page( "Main Page", "Blur Settings" )
    self.set_ui_pages(page)

    self.set_state_id("execute")
    self.execute()
`

A few comments regarding the above code sample:

1.
`add_render_elements`: Every user interface element created in a Pybox handler must be assigned to either the render or the global pool of user interface elements. A user interface element added to the render pool is only queried when Pybox node is requested a render: its Result view is displayed, or a node downstream in Batch is requesting a frame. A global element, in the other hand, always triggers a Python call. Generally speaking, a render element affects the render, whereas a global element affects the Pybox itself. Setting a blur amount affects the render of the image, and is assigned to the render pool. Opening a browser to select a setup, not so much, and is assigned to the global pool.

2.
`create_page`: Creates the JSON object that defines the first argument is the name of the page, the second, the heading of the first column.

3.
`set_ui_pages`: Required for the page to appear in the Pybox node's UI.

The following user interface elements are supported in Pybox nodes.

| User Interface Element | `pybox_v1` function to display the element in the Pybox node |
|---|---|
| Floating Point field | `create_float_numeric()` |
| Floating Point numeric - 2 fields | `create_vector_numeric()` with `size = 2` |
| Floating Point numeric - 3 fields | `create_vector_numeric()` with `size = 3` |
| Drop-down | `create_popup()` |
| Colour pot | `create_color()` |
| Button (toggle) | `create_toggle_button()` |
| File Browser field and button | `create_file_browser()` |

---

## Important Pybox Features

The Pybox processing pipeline is stateless and synchronous.

### `init/setup_ui/execute/teardown`

Flame never changes a Pybox state by itself: Flame is not aware of anything beyond the JSON payload it monitors (in the context on Pybox at least). You, the python developer, are responsible for the state's transition. Once you set the Pybox's state using set_state_id(), and once Flame receives the information through the JSON payload, Flame always calls the Pybox handler using the same state.

For example, Pybox is in the `initialize` state. Flame will not call Pybox with an execute state. If the Pybox wants to be called with an execute state, it must call `set_state_id("execute")`. The only thing Flame can do is query the state, and return user interface object values.

You can always call other functions from anywhere, just make sure that you have all the information needed to successfully do your task. Remember, Pybox is stateless and as such does not know where it's at unless you tell it. For example, you call `self.execute()` from the `initialize()` method, completely bypassing `setup_ui()`: you might not have the input images you need to produce a valid render. While this is not wrong per se, you might just end up without an output.

### Interacting with Flame

There are three components used to interact with Flame: image file output from Flame, image file input from the external processor, and the JSON payload.

The Pybox is just a script that connects Flame to the external processor. But the script does not interact directly with Flame. Everything is passed through a temporary JSON file, which is itself completely stateless. And it is this JSON payload that is read by Flame.

#### JSON Payload File

The JSON file is what the handler and Flame use to communicate with each other. Flame is not aware of the external processor: only the handler is expected to interact with the processor.

---

## Pybox Performance

Many factors affect the performance of a Pybox node. Of course, CPU, GPU, and RAM are all important to speed at which the external renderer returns a result to Flame. But the most important bottleneck is disk IO operations: Flame exchanges image files with the external processor by writing and reading from disk: there is no reading from RAM.

This means that to ensure best performance, consider using fast storage as the destination for the files written and read by Flame. For best performance, set up and use a RAM disk.

---

## Accessing Frame-Related Metadata

The following methods can be used to access Flame-related metadata.

| Metadata | `pybox_v1.BaseClass` method |
|---|---|
| The bit depth of the current batch default | `get_bit_depth()` |
| The colour space of the project | `get_colour_space()` |
| Today's date | `get_date()` |
| Today's day | `get_date_day()` |
| Today's month | `get_date_month()` |
| Today's year | `get_date_year()` |
| The current Batch frame | `get_frame()` |
| The frame ratio of the current batch default | `get_frame_ratio()` |
| The frame rate | `get_framerate()` |
| The height of the current batch default | `get_height()` |
| The image format as set by the `set_img_format` method | `get_img_format()` |
| The nickname of the user | `get_nickname()` |
| The name of the node in Batch, defined in the Node Name field in the Batch user interface | `get_node_name()` |
| The name of the Flame Project | `get_project()` |
| The nickname of the Flame Project | `get_project_nickname()` |
| The record timecode of the current frame | `get_record_time_code()` |
| The `width`, `bit_depth`, `frame_ratio`, and `height` of the current batch default | `get_resolution()` |
| The source timecode of the current frame | `get_source_time_code()` |
| The name of the current user | `get_user()` |
| The width of the current batch default | `get_width()` |
| The name of the workstation where Flame currently runs | `get_workstation()` |

---

## Managing Errors in a Pybox Handler

You can always interrupt a Pybox from within Flame with the Esc key.

Because a Pybox node processes whenever it is requested a frame, displaying anything but its Result view (F4) prevents it from processing a frame. This can be especially important when testing out a Pybox and you don't want to lose interactivity while troubleshooting.

In the Pybox node, Change Handler loads a handler from scratch: there is no caching. This means that whenever you edit a handler, Change Handler to reload the handler and test it immediately in Flame.

Error trapping is essential to debug and troubleshoot. Using the Pybox API, you can send (set) a message to Flame and read (get) messages from Flame. As always, all information is passed through the JSON payload.

| Read | Write |
|---|---|
| `get_error_msg()` | `set_error_msg()` |
| `get_warning_msg()` | `set_warning_msg()` |
| `get_notice_msg()` | `set_notice_msg()` |
| `get_debug_msg()` | `set_debug_msg()` |

In the above table, the messages are organized by severity, from highest to lowest.

Messages are displayed in Flame's message console, and in the application's shell and log.

You should also use `try…except` statements to trap exceptions in your Pybox handlers. This is outside the scope of this document, but the Python Software Foundation covers this topic.

---

## Pybox Examples

You will find handler samples in `/opt/Autodesk/presets/<version>/pybox/`.

#### `event_handling`

This Pybox handler shows how you can handle changes in the user interface after user input. This handler creates a dynamic user interface page, and user interface objects are labelled with text that describes the event it triggers.

#### `image_magick.py`

This Pybox handler is a simple blur effect created with ImageMagick. Using this handler requires you to install ImageMagick.

- Note: ImageMagick is no longer installed by default on Rocky Linux.

For additional information on ImageMagick, see ImageMagick website.

#### `image_magick_polaroid.py`

This Pybox handler is a polaroid effect created with ImageMagick. Using this handler requires you to install ImageMagick.

- Note: ImageMagick is no longer installed by default on Rocky Linux.

For additional information on ImageMagick, see ImageMagick website.

#### `no_op.py`

This Pybox handler is a simple passthrough Pybox. The input front is forwarded to the result output and the input matte is forwarded to the result output. The simplest Pybox handler.

#### `print_process_infos.py`

This Pybox handler demonstrates how to get the processing information and print it out to the shell.

#### `random_ui.py`

This Pybox handler is a variation on the event_handling.py Pybox. In random_ui.py, the user interface is created randomly. It demonstrates how you can create functions outside the main `pybox.BaseClass` to be used within the main pybox object.

#### `sendmail.py`

This Pybox handler demonstrates how, without any input or output sockets, a Pybox can be used to generate or process arbitrary information.

### Nuke Handler Example
Important: The purpose of this example is to show you how to create a workflow with Nuke. It is not a complete solution, and requires that you customize the scripts (Python and Nuke) to enhance the workflow.

The Nuke Pybox example consists of the following files:

-
`/opt/Autodesk/presets/<version>/pybox/nuke_px.py`

-
`/opt/Autodesk/shared/presets/pybox/nuke\_parse\_io.py`

-
`/opt/Autodesk/shared/presets/pybox/nuke\_parse\_ui.py`

-
`/opt/Autodesk/shared/presets/pybox/nuke\_parse\_exec.py`

nuke_px.py is Pybox handler: the file the user loads in a Pybox node in Flame. nuke_parse_io.py manages the IO, while nuke_parse_ui.py manages user interface interactions.

To use the Nuke handler, you must first edit nuke_px.py.

1.
Change the value of NUKE_PATH to match your Nuke installation.

2.
On macOS, make sure PAYLOAD_PATH resolves.

If performance is slow, change the `filename`variable in both `nuke_parse_io.py` and `nuke_exec.py` to a fast drive. The default setting uses the OS's temporary directory to read and write the frame. Change the following line:

`python
filename = tempfile.gettempdir() + "/" + node.name() + ".exr"
`

to something similar to the following:

`python
filename = "/path/to_directory/on_fast_storage/" + node.name() + ".exr"
`

#### Controlling Nuke from Flame's Pybox

A Nuke composition node which name starts with `adsk_` can have its knobs exposed in Flame's Pybox node if those knobs also have a name that starts with `adsk_`. The following illustrates such an `adsk_` node in a `.nk` file.

`python
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
`

The Write node in Nuke must also meet some requirements:

-
Named `adsk_1_result` or `adsk_2_matte`.

-
You must have used a Shuffle to output an 8- or 16-bit RGB file. RGBA is not supported.

-
Must output 8- or 16-bit RGB data. RGBA is not supported.

The following illustrates such Shuffle and Write nodes in a `.nk` file.

`python
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
`

---

## Glossary

A few terms defined here to make some things clear:

#### Pybox

1.
The feature that allows Flame artists to use - in a Batch Group or Timeline - third-party applications as if they were part of the Flame image processing pipeline.

2.
The Batch node or Timeline FX the Flame artist adds to a Batch or Timeline segment. As opposed to handler.

#### Flame Artist

In this document, the Flame user, as opposed to the developer who creates the handler.

#### Handler

A handler is a python file written by a developer. This file is loaded in a Pybox node or Pybox timeline FX by the Flame artist. It is this file that creates the Pybox UI, sets and reads values from the JSON payload, and interacts with the third-party application.

#### JSON Payload

A temporary file created by Flame, and used by Flame to communicate with the Python handler.
