# class `flame.PyActionNode`(PyActionFamilyNode)

> **2027 additions not shown below.** Autodesk's published pydoc predates some Flame 2027 API changes. New/renamed/deprecated members for this class (or its bases) are in What's New: [PyNode](../../guides/whats-new-2027.md#pynode), [PyActionFamilyNode](../../guides/whats-new-2027.md#pyactionfamilynode). Treat those as authoritative where they differ.

Class derived from PyActionFamilyNode. Represents an Action node object.

**Method resolution order:** PyActionNode → PyActionFamilyNode → PyNode → PyFlameObject

> Cannot be instantiated from Python (obtained from other API objects).

## Methods

### `add_media`

```python
add_media( (PyActionFamilyNode)arg1) -> object
```

Add a Media layer to the Batch Action node.

Also instantiates a matching Surface node (and Axis) in the Action node schematic.

### `disable_output`

```python
disable_output( (PyActionFamilyNode)arg1, (str)output_type) -> bool
```

Disable the render output_type for the Action node.

Keyword argument:

output_type -- The output to enable. (Comp, Matte, 3D Motion, Albedo, AO, Background, Emissive, GMask, Lens Flare, Motion Vectors, Normals, Object ID, Occluder, Position, Projectors Matte, Reflection, Roughness, Shadow, Specular, UV, Z-Depth HQ, Z-Depth)

### `enable_output`

```python
enable_output( (PyActionFamilyNode)arg1, (str)output_type) -> bool
```

Enable the render output_type for the Action node.

Keyword argument:

output_type -- The output to enable. (Comp, Matte, 3D Motion, Albedo, AO, Background, Emissive, GMask, Lens Flare, Motion Vectors, Normals, Object ID, Occluder, Position, Projectoars Matte, Reflection, Roughness, Shadow, Specular, UV, Z-Depth HQ, Z-Depth)

### `export_fbx`

```python
export_fbx( (PyActionFamilyNode)arg1, (str)file_path [, (bool)only_selected_nodes=False [, (float)pixel_to_units=0.10000000149011612 [, (str)frame_rate='23.976 fps' [, (bool)bake_animation=False [, (bool)export_axes=True [, (bool)export_point_locators=False [, (bool)combine_material=True [, (bool)duplicate_material=False]]]]]]]]) -> bool
```

Export Action nodes to an FBX file.

Keyword argument:

file_path -- Path to the output FBX file. Mandatory.

### `import_abc`

```python
import_abc( (PyActionFamilyNode)arg1, (str)file_path [, (bool)lights=True [, (bool)cameras=True [, (bool)models=True [, (bool)normals=True [, (bool)mesh_animations=True [, (str)frame_rate='23.976 fps' [, (bool)auto_fit=False [, (float)unit_to_pixels=10.0 [, (bool)consolidate_geometry=True [, (bool)create_object_group=False]]]]]]]]]]) -> list
```

Import an Alembic (ABC) file into the Action schematic using the Action Objects mode.

Keyword argument:

file_path -- Path to the ABC file. Mandatory.

### `import_fbx`

```python
import_fbx( (PyActionFamilyNode)arg1, (str)file_path [, (bool)lights=True [, (bool)cameras=True [, (bool)models=True [, (bool)normals=True [, (bool)mesh_animations=True [, (bool)keep_frame_rate=True [, (bool)bake_animation=False [, (bool)object_properties=True [, (bool)auto_fit=False [, (float)unit_to_pixels=10.0 [, (bool)create_media=True [, (bool)is_udim=False [, (bool)relink_material=True [, (str)input_colour_space='']]]]]]]]]]]]]]) -> list
```

Import an FBX file into the Action schematic using the Action Objects mode.

Keyword argument:

file_path -- Path to the FBX file. Mandatory.

### `import_psd`

```python
import_psd( (PyActionFamilyNode)arg1, (str)file_path [, (str)input_colour_space='']) -> list
```

Import a PSD file into the Action schematic.

Keyword arguments:

file_path -- Path to the PSD file. Mandatory.

input_colour_space -- The colour space used as input. Optional.

### `read_abc`

```python
read_abc( (PyActionFamilyNode)arg1, (str)file_path [, (bool)lights=True [, (bool)cameras=True [, (bool)models=True [, (bool)normals=True [, (bool)mesh_animations=True [, (str)frame_rate='23.976 fps' [, (bool)auto_fit=False [, (float)unit_to_pixels=10.0 [, (bool)consolidate_geometry=True [, (bool)create_object_group=False]]]]]]]]]]) -> object
```

Import an Alembic (ABC) file into the Action schematic using the Read File mode.

Keyword argument:

file_path -- Path to the ABC file. Mandatory.

### `read_fbx`

```python
read_fbx( (PyActionFamilyNode)arg1, (str)file_path [, (bool)lights=True [, (bool)cameras=True [, (bool)models=True [, (bool)normals=True [, (bool)mesh_animations=True [, (bool)keep_frame_rate=True [, (bool)bake_animation=False [, (bool)object_properties=True [, (bool)auto_fit=False [, (float)unit_to_pixels=10.0 [, (bool)is_udim=False [, (bool)relink_material=True [, (str)input_colour_space='']]]]]]]]]]]]]) -> object
```

Import an FBX file into the Action schematic using the Read File mode.

Keyword argument:

file_path -- Path to the FBX file. Mandatory.

## Read-only properties defined here

### `media_nodes`

Return a list of the Media nodes attached to the Action node.

### `output_types`

Return a list of the output types available to the Action node.

## Inherited members

- **Static methods inherited from PyActionFamilyNode:** `clear_schematic`, `connect_nodes`, `create_node`, `disconnect_nodes`, `encompass_nodes`, `get_node`, `organize`
- **Read-only properties inherited from PyActionFamilyNode:** `all_tabs`, `cursor_position`, `left_tabs`, `media_layers`, `node_types`, `nodes`, `right_tabs`
- **Static methods inherited from PyNode:** `delete`, `duplicate`, `load_node_setup`, `save_node_setup`, `set_context`
- **Read-only properties inherited from PyNode:** `input_sockets`, `output_sockets`, `sockets`
- **Read-only properties inherited from PyFlameObject:** `attributes`, `parent`

## Attributes (documented values)

Source: "PyActionNode Attributes" help page. Access via `obj.<attr>`; most return a `PyAttribute` — use `.get_value()` / `.set_value()` (see PyAttribute.md).

#### `pos_x (type 'int')`

The x position of a node in the Batch schematic.

Value range:

- Min: -2147483647
- Max: 2147483647

#### `pos_y (type 'int')`

The y position of a node in the Batch schematic.

Value range:

- Min: -2147483647
- Max: 2147483647

#### `name (type 'str')`

The name of the node in the Batch schematic.

#### `collapsed (type 'bool')`

The collapsed status of a node in the Batch schematic.

Value range:

- True
- False

#### `note (type 'str')`

The Node's note.

#### `note_collapsed (type 'bool')`

The collapsed status of a note in the Batch schematic.

Value range:

- True
- False

#### `selected (type 'bool')`

Select a Node in the Batch schematic.

Value range:

- True
- False

#### `type (type 'str')`

Return the type of the node.

#### `selected_nodes (type 'list')`

The list of Action object nodes that are currently selected in the Action schematic.

#### `current_node (class 'flame.PyCoNode')`

Return the currently selected action object node in the Action schematic.
