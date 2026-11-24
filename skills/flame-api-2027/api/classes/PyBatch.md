# class `flame.PyBatch`(PyFlameObject)

> **2027 additions not shown below.** Autodesk's published pydoc predates some Flame 2027 API changes. New/renamed/deprecated members for this class (or its bases) are in What's New: [PyBatch](../../guides/whats-new-2027.md#pybatch). Treat those as authoritative where they differ.

Class derived from PyFlameObject. This class represents a Batch Group.

**Method resolution order:** PyBatch → PyFlameObject

> Cannot be instantiated from Python (obtained from other API objects).

## Methods

### `append_setup`

```python
append_setup( (PyBatch)arg1, (str)setup_path [, (bool)confirm=True]) -> bool
```

Append a Batch setup file to the existing Batch setup.

Keywords arguments:

setup_path -- A path and a filename must be defined as arguments.

confirm -- Set to True (default) to display a dialog window in case of

### `append_to_batch`

```python
append_to_batch( (PyBatch)arg1, (PyBatchIteration)batch_iteration) -> bool
```

Append a Batch Iteration object to the current Batch Group. A duplicate Batch Iteration object is renamed to the next available *vDD*. Batch Iteration objects are displayed in the Iterations folder. Iterations folder is a user interface construction, not accessible directly.

### `append_to_setup`

```python
append_to_setup( (PyBatch)arg1, (PyBatchIteration)batch_iteration) -> bool
```

Append a Batch Iteration object to the Batch Group's setup.

### `clear`

```python
clear( (PyBatch)arg1 [, (bool)confirm=True]) -> bool
```

Clear the Batch Group.

### `clear_all_contexts`

```python
clear_all_contexts( (PyBatch)arg1) -> bool
```

Clear all registered Context views in the Batch Group.

### `clear_colour`

```python
clear_colour( (PyBatch)arg1, (int)index) -> bool
```

Clear the colour of the Batch Group.

### `clear_context`

```python
clear_context( (PyBatch)arg1, (int)index) -> bool
```

Clear a specific Context view in the Batch Group.

### `clear_setup`

```python
clear_setup( (PyBatch)arg1) -> bool
```

Clear the Batch Group's setup.

### `close`

```python
close( (PyBatch)arg1) -> bool
```

Close the Batch Group. You cannot close the Batch Group currently selected.

Closing a Batch Group frees up the application it occupies when open. The size of the used memory is significant if in Batch Group schematic hosts many Action nodes with textures or 3D geoms.

### `connect_nodes`

```python
connect_nodes( (PyBatch)arg1, (PyNode)output_node, (str)output_socket_name='Default', (PyNode)input_node [, (str)input_socket_name='Default']) -> bool
```

Connect two nodes in the Batch schematic.

Keyword arguments:

output_node -- The Batch node object, the origin of the connection.

output_socket_name -- The name of the output socket where the connector starts; use *Default* to use the first output socket, usually *Result*.

input_node -- The child Batch node object, the target of the connection.

input_socket_name -- The name of the input socket where the connector ends; use *Default* to use the first input socket, usually *Front*. Using *Default* on an Action node connects to the Background socket. To connect to an Action media node, use .media_nodes[].

### `create_batch_group`

```python
create_batch_group( (PyBatch)arg1, (str)name [, (int)nb_reels=4 [, (int)nb_shelf_reels=1 [, (list)reels=[] [, (list)shelf_reels=[] [, (int)start_frame=1 [, (object)duration=None]]]]]]) -> object
```

Create a new Batch Group object in the Desktop catalogue.

Keyword arguments:

name -- Name of the Batch Group.

nb_reels -- Number of reels created. *reels* overrides *nb_reels*.

nb_shelf_reels -- Number of shelf reels. The first shelf reel created is named Batch Renders. *shelf_reels* overrides *nb_shelf_reels*.

reels -- A list of reel names. Overrides *nb_reels*.

shelf_reels -- A list of shelf reel names. Overrides *nb_shelf_reels*.

start_frame -- The Batch Group's start frame. No timecodes, only a frame value.

duration -- The number of frames. Sets the Duration field in the Batch UI. Will be set to the first clip duration when not specified.

### `create_node`

```python
create_node( (PyBatch)arg1, (str)node_type [, (str)file_path='']) -> object
```

Create a Batch node object in the Batch schematic.

Keyword argument:

node_type -- Must be a value from the PyBatch.node_types or the name of a node in the User, Project, or Shared bin.

### `create_reel`

```python
create_reel( (PyBatch)arg1, (str)name) -> object
```

Create a new Schematic Reel in the Batch Gtroup.

### `create_shelf_reel`

```python
create_shelf_reel( (PyBatch)arg1, (str)name) -> object
```

Create a new Shelf Reel in the Batch Group.

### `disconnect_node`

```python
disconnect_node( (PyBatch)arg1, (PyNode)node [, (str)input_socket_name='']) -> bool
```

Disconnect the input links of a given node, given an input socket.

Keyword arguments:

node -- The Batch node object, the origin of the connection.

input_socket_name -- The name of the input socket to disconnect.

### `encompass_nodes`

```python
encompass_nodes( (PyBatch)arg1, (list)nodes) -> object
```

Create a Compass around a list of nodes in the Batch schematic.

Keyword argument:

nodes -- List of strings of node names.

### `frame_all`

```python
frame_all( (PyBatch)arg1) -> bool
```

Set the Batch schematic view to frame all the nodes in the Batch schematic.

### `frame_selected`

```python
frame_selected( (PyBatch)arg1) -> bool
```

Set the Batch schematic view to frame the nodes selected in the Batch schematic.

### `get_node`

```python
get_node( (PyBatch)arg1, (str)node_name) -> object
```

Return a Batch node object with a name matching the parameter. Every node in a Batch schematic has a unique name: no duplicates allowed.

Keyword argument:

node_name -- Node name.

### `go_to`

```python
go_to( (PyBatch)arg1) -> bool
```

Display and set the Batch tab as the active environment.

### `import_clip`

```python
import_clip( (PyBatch)arg1, (str)file_path, (str)reel_name) -> object
```

Import a clip using the Import node, and create a Clip node.

Keyword arguments:

file_path -- The path to the media can be:

- A path to a single media file.

- A path to a sequence of media files (ie "/dir/clip.[100-2000].dpx").

- A pattern to media files (ie "/dir/name_v{version}.{frame}.{extension}").reel_name -- The name of the destination Schematic Reel.

### `import_clips`

```python
import_clips( (PyBatch)arg1, (object)file_paths, (str)reel_name) -> object
```

Import clips using the Import node, and then create Clip nodes in the Schematic Reel.

Keyword arguments:

file_paths -- A path, or a list of paths, to the media that can be:

- A path to a single media file.

- A path to a sequence of media files (ie "/dir/clip.[100-2000].dpx").

- A pattern to media files (ie "/dir/name_v{version}.{frame}.{extension}").reel_name -- The name of the destination Schematic Reel.

### `iterate`

```python
iterate( (PyBatch)arg1 [, (int)index=-1]) -> object
```

Iterate the current Batch Setup, creating a new iteration named BatchSetupName_X, where X is the Batch Iteration's index, and starts at 001.

Keyword argument:

index -- Specifies the iteration's index. If none is specified, the iteration is assigned the next available index (max index + 1). If the index matches that of an existing Batch Iteration, its overwrites the iteration without warning.

### `load_setup`

```python
load_setup( (PyBatch)arg1, (str)setup_path) -> bool
```

Load a Batch setup from disk and replace the current Batch Group's setup.

Keyword argument:

setup_path -- Filepath + Batch Setup filename.

### `mimic_link`

```python
mimic_link( (PyBatch)arg1, (PyNode)leader_node, (PyNode)follower_node) -> bool
```

Create a Mimic Link between two Batch nodes. They must be of the same node_type.

Keyword arguments:

leader_node -- The node being mimicked.

follower_node -- The node doing the mimicking.

### `open`

```python
open( (PyBatch)arg1) -> bool
```

Open the Batch Group and display it in the Batch view.

### `open_as_batch_group`

```python
open_as_batch_group( (PyBatch)arg1 [, (bool)confirm=True]) -> bool
```

Open a Batch Group as a new Batch Group, adding it to PyDesktop.batch_groups. Can only be called from a Library.

### `organize`

```python
organize( (PyBatch)arg1) -> bool
```

Clean up the nodes layout in the Batch schematic.

### `render`

```python
render( (PyBatch)arg1 [, (str)render_option='Foreground' [, (bool)generate_proxies=False [, (bool)include_history=False]]]) -> bool
```

Trigger the rendering of the Batch Group setup. Every active Render and Write File nodes render. If specified render_option is not supported by the workstation, returns an error.

Keyword arguments:

render_option -- Defines the rendering method used. (Foreground, Background Reactor, Burn)

generate_proxies -- Set to True to render at proxy resolution. (Default: False)

include_history -- Set to True to create History with the rendering. (Default:False)

### `replace_setup`

```python
replace_setup( (PyBatch)arg1, (PyBatchIteration)batch_iteration [, (bool)confirm=True]) -> bool
```

Replace the Batch Group setup with the specified Batch Iteration. Cannot be called on the Batch Group currently selected and displayed in the Batch view.

### `save`

```python
save( (PyBatch)arg1) -> object
```

Save the Batch Group to the location defined by PyDesktop.destination.

### `save_current_iteration`

```python
save_current_iteration( (PyBatch)arg1) -> object
```

Save the current Batch Group setup to the location defined by PyDesktop.destination.

### `save_setup`

```python
save_setup( (PyBatch)arg1, (str)setup_path) -> bool
```

Save the Batch Group setup to disk. Includes media paths for clip node object, but not the media files themselves.

Keyword argument:

setup_path -- The filepath includes the filename. File extension must be .batch.

### `select_nodes`

```python
select_nodes( (PyBatch)arg1, (object)nodes) -> bool
```

Select nodes.

Keyword argument:

nodes -- A list of the names of Batch node objects.

### `set_viewport_layout`

```python
set_viewport_layout( (PyBatch)arg1, (object)num_views) -> bool
```

Set the viewport layout for Batch.

Keyword argument:

num_views -- The layout used. (1-Up, 2-Up, 3-Up, 3-Up Split Top, 3-Up Split Left, 3-Up Split Right, 3-Up Split Bottom, 4-Up Split, 4-Up)

## Read-only properties defined here

### `batch_iterations`

Return a list of Batch Iteration objects of the Batch Group.

### `contexts`

Return a dictionary of Context views registered in the Batch Group.

Dictionary {key:value} -- {Context ID : {Batch node name:socket name} }

### `current_iteration`

Return the current Batch Iteration object of the Batch Group.

### `current_iteration_number`

Return the iteration number of the current Batch Iteration.

### `cursor_position`

Return a tuple that provides the cursor position in the Batch Schematic.

### `node_types`

Return a list of the names of the Batch node types available to the Batch schematic.

### `nodes`

Return the list of Batch node objects from the Batch schematic.

### `opened`

Return True if the Batch Group is loaded in memory.

### `reels`

Return the list of reel objects (as Schematic Reels) for the Batch Group.

### `shelf_reels`

Return the list of reel objects (as Shelf Reels) for the Batch Group.

## Inherited members

- **Read-only properties inherited from PyFlameObject:** `attributes`, `parent`

## Attributes (documented values)

Source: "PyBatch Attributes" help page. Access via `obj.<attr>`; most return a `PyAttribute` — use `.get_value()` / `.set_value()` (see PyAttribute.md).

#### `name (type 'str')`

The name of an object in the Media Panel, resolving tokens if any are present.

#### `uid (type 'str')`

The unique identifier of an object in the Media Panel.

#### `token_name (type 'str')`

The tokenized name of an object in the Media Panel.

#### `expanded (type 'bool')`

The expanded state of an object in the Media Panel. If you're expanding/collapsing a Shared Library, you must have exclusive access if you want this property to be persisted.

Value range:

- True
- False

#### `colour (type 'tuple')`

The colour of an object in the Media Panel.

Value range:

- (0.0, 0.0, 0.0)
- (1.0, 1.0, 1.0)

#### `colour_label (type 'str')`

The colour label of an object in the Media Panel.

#### `selected (type 'bool')`

The PyArchiveEntry is selected in the Media Panel.

Value range:

- True
- False

#### `selected_nodes (type 'list')`

The list of Batch object nodes that are currently selected in the Batch schematic.

#### `current_node (class 'flame.PyActionNode')`

Return the Batch node currently selected in the Batch schematic. Use current_node to capture the node selected by the user. In the case of a multi-selection, return the primary selection (yellow ring).

#### `duration (type 'int')`

The duration of Batch Group.

#### `start_frame (type 'int')`

The start frame of the Batch Group.

#### `auto_key (type 'bool')`

The Auto Key status of the Batch Group.

#### `current_frame (type 'int')`

The current frame of the Batch Group.

#### `tags (type 'list')`

The tag list of an object in the Media Panel.
