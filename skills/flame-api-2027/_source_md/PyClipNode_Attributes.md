<!-- source: Autodesk Flame Family 2027 Help _ PyClipNode Attributes _ Autodesk.html -->
# PyClipNode Attributes

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

## Related pages

- Autodesk Flame Python: flame module
