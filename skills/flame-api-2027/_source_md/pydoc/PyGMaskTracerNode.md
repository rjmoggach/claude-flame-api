# class `flame.PyGMaskTracerNode`(PyActionFamilyNode)

Class derived from PyActionFamilyNode. Represents a GMask Tracer node object.

**Method resolution order:** PyGMaskTracerNode → PyActionFamilyNode → PyNode → PyFlameObject

## Methods

> Cannot be instantiated from Python (obtained from other API objects).

### `disable_output`

```python
disable_output( (PyActionFamilyNode)arg1, (str)output_type) -> bool
```

Disable the render output_type for the GMask Tracer node.

Keyword argument:

output_type -- The output to enable. (Comp, Matte, 3D Motion, Albedo, AO, Background, Emissive, GMask, Lens Flare, Motion Vectors, Normals, Object ID, Occluder, Position, Projectors Matte, Reflection, Roughness, Shadow, Specular, UV, Z-Depth HQ, Z-Depth)

### `enable_output`

```python
enable_output( (PyActionFamilyNode)arg1, (str)output_type) -> bool
```

Enable the render output_type for the GMask Tracer node.

Keyword argument:

output_type -- The output to enable. (Comp, Matte, 3D Motion, Albedo, AO, Background, Emissive, GMask, Lens Flare, Motion Vectors, Normals, Object ID, Occluder, Position, Projectoars Matte, Reflection, Roughness, Shadow, Specular, UV, Z-Depth HQ, Z-Depth)

### `export_fbx`

```python
export_fbx( (PyActionFamilyNode)arg1, (str)file_path [, (bool)only_selected_nodes=False [, (float)pixel_to_units=0.10000000149011612 [, (str)frame_rate='23.976 fps' [, (bool)bake_animation=False [, (bool)export_axes=True [, (bool)export_point_locators=False [, (bool)combine_material=True [, (bool)duplicate_material=False]]]]]]]]) -> bool
```

Export GMask Tracer nodes to an FBX file.

Keyword argument:

file_path -- Path to the output FBX file. Mandatory.

### `import_abc`

```python
import_abc( (PyActionFamilyNode)arg1, (str)file_path [, (bool)lights=True [, (bool)cameras=True [, (bool)models=True [, (bool)normals=True [, (bool)mesh_animations=True [, (str)frame_rate='23.976 fps' [, (bool)auto_fit=False [, (float)unit_to_pixels=10.0 [, (bool)consolidate_geometry=True [, (bool)create_object_group=False]]]]]]]]]]) -> list
```

Import an Alembic (ABC) file into the GMask Tracer schematic using the GMask Tracer Objects mode.

Keyword argument:

file_path -- Path to the ABC file. Mandatory.

### `import_fbx`

```python
import_fbx( (PyActionFamilyNode)arg1, (str)file_path [, (bool)lights=True [, (bool)cameras=True [, (bool)models=True [, (bool)normals=True [, (bool)mesh_animations=True [, (bool)keep_frame_rate=True [, (bool)bake_animation=False [, (bool)object_properties=True [, (bool)auto_fit=False [, (float)unit_to_pixels=10.0 [, (bool)create_media=True [, (bool)is_udim=False [, (bool)relink_material=True]]]]]]]]]]]]]) -> list
```

Import an FBX file into the GMask Tracer schematic using the GMask Tracer Objects mode.

Keyword argument:

file_path -- Path to the FBX file. Mandatory.

### `read_abc`

```python
read_abc( (PyActionFamilyNode)arg1, (str)file_path [, (bool)lights=True [, (bool)cameras=True [, (bool)models=True [, (bool)normals=True [, (bool)mesh_animations=True [, (str)frame_rate='23.976 fps' [, (bool)auto_fit=False [, (float)unit_to_pixels=10.0 [, (bool)consolidate_geometry=True [, (bool)create_object_group=False]]]]]]]]]]) -> object
```

Import an Alembic (ABC) file into the GMask Tracer schematic using the Read File mode.

Keyword argument:

file_path -- Path to the ABC file. Mandatory.

### `read_fbx`

```python
read_fbx( (PyActionFamilyNode)arg1, (str)file_path [, (bool)lights=True [, (bool)cameras=True [, (bool)models=True [, (bool)normals=True [, (bool)mesh_animations=True [, (bool)keep_frame_rate=True [, (bool)bake_animation=False [, (bool)object_properties=True [, (bool)auto_fit=False [, (float)unit_to_pixels=10.0 [, (bool)is_udim=False [, (bool)relink_material=True]]]]]]]]]]]]) -> object
```

Import an FBX file into the GMask Tracer schematic using the Read File mode.

Keyword argument:

file_path -- Path to the FBX file. Mandatory.

## Read-only properties defined here

### `output_types`

Return a list of the output types available to the GMask Tracer node.

## Inherited members

- **Static methods inherited from PyActionFamilyNode:** `clear_schematic`, `connect_nodes`, `create_node`, `disconnect_nodes`, `encompass_nodes`, `get_node`, `organize`
- **Read-only properties inherited from PyActionFamilyNode:** `all_tabs`, `cursor_position`, `left_tabs`, `media_layers`, `node_types`, `nodes`, `right_tabs`
- **Static methods inherited from PyNode:** `delete`, `duplicate`, `load_node_setup`, `save_node_setup`, `set_context`
- **Read-only properties inherited from PyNode:** `input_sockets`, `output_sockets`, `sockets`
- **Read-only properties inherited from PyFlameObject:** `attributes`, `parent`
