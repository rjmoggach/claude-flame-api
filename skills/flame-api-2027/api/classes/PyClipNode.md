# class `flame.PyClipNode`(PyNode)

> **2027 additions not shown below.** Autodesk's published pydoc predates some Flame 2027 API changes. New/renamed/deprecated members for this class (or its bases) are in What's New: [PyClipNode](../../guides/whats-new-2027.md#pyclipnode), [PyNode](../../guides/whats-new-2027.md#pynode). Treat those as authoritative where they differ.

Class derived from PyNode. This class represents a Clip node.

**Method resolution order:** PyClipNode → PyNode → PyFlameObject

> Cannot be instantiated from Python (obtained from other API objects).

## Methods

### `set_version_uid`

```python
set_version_uid( (PyClipNode)arg1, (str)version_uid) -> bool
```

Set the clip node's current version unique ID.

Keywords argument:

version_uid -- version unique ID.

## Read-only properties defined here

### `clip`

The associated PyClip or PySequence of the clip node.

### `version_uid`

The clip node's list of available version unique IDs.

### `version_uids`

The clip node's list of available version unique IDs.

### `colour_space`

The clip colour space at current frame for primary output.

## Inherited members

- **Static methods inherited from PyNode:** `delete`, `duplicate`, `load_node_setup`, `save_node_setup`, `set_context`
- **Read-only properties inherited from PyNode:** `input_sockets`, `output_sockets`, `sockets`
- **Read-only properties inherited from PyFlameObject:** `attributes`, `parent`

## Attributes (documented values)

Source: "PyClipNode Attributes" help page. Access via `obj.<attr>`; most return a `PyAttribute` — use `.get_value()` / `.set_value()` (see PyAttribute.md).

Use the following commands to set or get attributes for a Clip node.

| Command | Type | Description |
|---|---|---|
| `PyClipNode>.shot_name` | string | The shot name of a node in the Batch schematic, resolving tokens if any are present. |
| `PyClipNode>.tokenized_shot_name` | string | The shot name of a clip node in the Batch schematic, including any unresolved tokens, if present. |
| `PyClipNode>.dynamic_shot_name` | bool | The Dynamic attribute of a clip node in the Batch schematic. Automatically disabled when the shot_name attribute is set.<br><br>One of the following must be passed as the argument when the attribute is set: • True • False |
| `PyClipNode>.head_media` | string | Used set or get the Head Media option.<br><br>One of the following must be passed as the argument when the attribute is set: • Repeat First • No Media • Use Black |
| `PyClipNode>.gap_media` | string | Used set or get the Gap Media option.<br><br>One of the following must be passed as the argument when the attribute is set: • No Media • Use Black |
| `PyClipNode>.tail_media` | string | Used set or get the Head Media option.<br><br>One of the following must be passed as the argument when the attribute is set: • Repeat First • No Media • Use Black |
| `PyClipNode>.timing_offset` | integer | Used set or get the Timing Offset. An integer number must be passed as an argument. |
| `PyClipNode>.locked_frame` | integer | Used to get or set the Locked frame.<br><br>One of the following must be passed as the argument when the attribute is set: • **None** to disabled the Locked Frame option. • An integer number representing the frame to be locked. |
