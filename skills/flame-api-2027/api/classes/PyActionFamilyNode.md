# class `flame.PyActionFamilyNode`(PyNode)

> **2027 additions not shown below.** Autodesk's published pydoc predates some Flame 2027 API changes. New/renamed/deprecated members for this class (or its bases) are in What's New: [PyActionFamilyNode](../../guides/whats-new-2027.md#pyactionfamilynode), [PyNode](../../guides/whats-new-2027.md#pynode). Treat those as authoritative where they differ.

Class derived from PyNode. Represents an Action Family node object.

**Method resolution order:** PyActionFamilyNode → PyNode → PyFlameObject

> Cannot be instantiated from Python (obtained from other API objects).

## Methods

### `clear_schematic`

```python
clear_schematic( (PyActionFamilyNode)arg1) -> bool
```

Clear the Action/Image/GMaskTracer schematic of all nodes.

### `connect_nodes`

```python
connect_nodes( (PyActionFamilyNode)arg1, (PyFlameObject)parent_node, (PyFlameObject)child_node [, (str)link_type='Default']) -> bool
```

Connect two nodes in the Action/Image/GMaskTracer schematic.

Keyword argument:

type -- The type of link used to connect the nodes (default, look at, gmask, gmask exclusive, light, light exclusive, mimic)

### `create_node`

```python
create_node( (PyActionFamilyNode)arg1, (str)node_type [, (str)file_path='' [, (bool)is_udim=False [, (int)tile_resolution=0]]]) -> object
```

Add an Action/Image/GMaskTracer object node to the Action/Image/GMaskTracer schematic.

Keyword argument:

file_path -- Required by nodes that load an asset, such as Matchbox.

### `disconnect_nodes`

```python
disconnect_nodes( (PyActionFamilyNode)arg1, (PyFlameObject)parent_node, (PyFlameObject)child_node [, (str)link_type='Default']) -> bool
```

Disconnect two nodes in the Action/Image/GMaskTracer schematic.

Keyword argument:

type -- The type of link used to connect the nodes (default, look at, gmask, gmask exclusive, light, light exclusive, mimic)

### `encompass_nodes`

```python
encompass_nodes( (PyActionFamilyNode)arg1, (list)node_list) -> object
```

Create a compass including the node list given as argument

Keyword argument:

node_list -- a list of nodes (either string or node objects)

output_type -- the created compass node

### `get_node`

```python
get_node( (PyActionFamilyNode)arg1, (str)node_name) -> object
```

Get a node by node name. Doesn't select it in the UI.

### `organize`

```python
organize( (PyActionFamilyNode)arg1) -> bool
```

Clean up the Action/Image/GMaskTracer schematic.

## Read-only properties defined here

### `all_tabs`

Return a list of the object tabs.

### `cursor_position`

Return a tuple that provides the cursor position in the Action/Image/GMaskTracer schematic.

### `left_tabs`

Return a list of the object left tabs.

### `media_layers`

Return a list of the Media layers of the Action/Image/GMaskTracer node.

### `node_types`

Return a list of the node types available in the Action/Image/GMaskTracer schematic.

### `nodes`

Return a list of Action/Image/GMaskTracer nodes used in the Action/Image/GMaskTracer schematic.

### `right_tabs`

Return a list of the object right tabs.

## Inherited members

- **Static methods inherited from PyNode:** `delete`, `duplicate`, `load_node_setup`, `save_node_setup`, `set_context`
- **Read-only properties inherited from PyNode:** `input_sockets`, `output_sockets`, `sockets`
- **Read-only properties inherited from PyFlameObject:** `attributes`, `parent`
