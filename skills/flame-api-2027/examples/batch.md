> Source: Flame Python API Code Samples (sections: Working with Nodes in Batch, Using a Compass in Action); Looping by Node Type; Render Passes with the Python API; Importing Multi-Channel Clip — Autodesk Flame Family 2027 Help

# Examples — Batch and Action

Code is verbatim from the source. Class references: [PyBatch](../api/classes/PyBatch.md), [PyNode](../api/classes/PyNode.md), [PyActionNode](../api/classes/PyActionNode.md), [PyCompassNode](../api/classes/PyCompassNode.md), [PyOFXNode](../api/classes/PyOFXNode.md), [PyClipNode](../api/classes/PyClipNode.md), [PyWriteFileNode](../api/classes/PyWriteFileNode.md).

Full "first script" walkthrough (create batch group → Comp → Write File → connect → organize): [../guides/getting-started.md](../guides/getting-started.md#write-your-first-script-walkthrough). 2027 Batch additions (Metadata node, `get_metadata`, expressions, node markers): [../guides/whats-new-2027.md](../guides/whats-new-2027.md).

Common facts shown by these samples:
- `flame.batch.create_node(type)` returns the new node; `flame.batch.import_clip(path, reel_name)` returns the clip node.
- `flame.batch.connect_nodes(src_node, "output_socket", dst_node, "input_socket")`; socket names are case sensitive.
- New nodes are all placed at (0,0); call `flame.batch.organize()` to lay them out.
- `flame.batch.current_node` is read with `.get_value()` in these samples.

## Working with Nodes in Batch

### Specify a shader from the default path when creating a Matchbox
API: `PyBatch.create_node(type, file)`.

```python
flame.batch.create_node("Matchbox","Blur.mx")
```

### Specify a handler from the default path when creating a Pybox
```python
flame.batch.create_node("Pybox","sendmail.py")
```

### Print the name of the current Matchbox shader
API: `PyBatch.get_node(name)`, Matchbox `shader_name`.

```python
mx = flame.batch.get_node("Matchbox100")
print(mx.shader_name)
```

### Create an OpenFX node and load a plugin in it
API: `PyOFXNode.change_plugin(name)`.

```python
ofx = flame.batch.create_node("OpenFX")
ofx.change_plugin("S_Distort")
```

### Print the name of the current OpenFX plugin
API: `PyOFXNode.plugin_name`.

```python
ofx = flame.batch.get_node("OpenFX100")
print(ofx.plugin_name)
```

### Bypass a node
API: `PyBatch.current_node`, `PyNode.bypass`.

```python
mux = flame.batch.current_node.get_value() mux.bypass = True
```

> Source issue: two statements collapsed onto one line in the official page (invalid Python). Likely intended (reconstruction, line break only):
> ```python
> mux = flame.batch.current_node.get_value()
> mux.bypass = True
> ```

### Set the Before setting of a MUX Range
```python
mux = flame.batch.current_node.get_value()
mux.before_range = "Repeat First"
```

### Set the After setting of a MUX Range
```python
mux = flame.batch.current_node.get_value()
mux.after_range = "Repeat Last"
```

### Freeze the current frame in a MUX node
API: `PyBatch.current_frame`; MUX `range_active`, `range_start`, `range_end`, `before_range`, `after_range`.

```python
frame = flame.batch.current_frame
mux = flame.batch.current_node.get_value()
mux.range_active = True
mux.range_start = frame
mux.range_end = frame
mux.before_range = "Repeat First"
mux.after_range = "Repeat Last"
```

## Using a Compass in Action

`action` is an Action node (e.g. `action = flame.batch.create_node("Action")`); compasses are created inside it.

### Set the Compass colour
API: `PyActionNode.create_node("Compass")`, `PyCompassNode.colour`.

```python
compass = action.create_node("Compass")
compass.colour = (50, 50, 50)
```

### Set the Compass name
```python
compass = action.create_node("Compass")
compass.name = "MyCompass"
```

### Set the Compass width
```python
compass = action.create_node("Compass")
compass.width = 250
```

### Set the Compass height
```python
compass = action.create_node("Compass")
compass.height = 250
```

### Create a Compass around nodes
API: `PyActionNode.encompass_nodes(list)` — list items can be node names or node objects.

```python
action.encompass_nodes(["NodeName1", node3, "NodeName2"])
```

### Get a list of nodes inside a Compass
API: `encompass_nodes` returns the compass; `PyCompassNode.nodes`.

```python
compass = encompass_nodes( ["NodeName1", node3, "NodeName2"] )
print(compass.nodes)
```

> Source issue: `encompass_nodes(...)` is called without the `action.` prefix used in the previous sample.

## Looping by Node Type

`flame.batch.nodes` returns all nodes in the Batch schematic; filter with `node.type`.

### Move Action Media nodes
Finds all Action Media nodes and moves those with `pos_y < 99` down by 100. API: `flame.batch.nodes`, `PyNode.type`, `PyNode.pos_y`.

```python
import flame

for i in flame.batch.nodes: #for every node in the batch group
    if i.type == "Action Media" and i.pos_y < 99: #if the node is an Action Media node and lower than 99 from centre
        i.pos_y -= 100 #move the media node by subtracting 100 from current ypos
```

### Set all Comp nodes to Add blend mode
API: `flame.batch.nodes`, `PyNode.type`, Comp `flame_blend_mode`.

```python
import flame

for n in flame.batch.nodes:
    if n.type == "Comp":
        n.flame_blend_mode = "Add"
```

## Render Passes with the Python API

Automates a multi-pass render comp in Batch: creates a batch group, imports eight EXR pass sequences into schematic reels, chains four Comp nodes (Add / Screen) into a Write File node, and organises the schematic. To use it, change the import file locations to your own media and adjust the render pass setup. APIs: `create_batch_group`, `go_to`, `import_clip`, `create_node`, `connect_nodes`, `organize`; Comp `flame_blend_mode`; clip output socket `"BGR"`.

```python
import flame

schematicReels = [ 'direct_passes', 'indirect_passes', 'reflection', 'Utility_Passes' ] #create/name schematic reels
shelfReels = [ 'Extra_Data', ] #create/name shelf reels

#Create batch group
flame.batch.create_batch_group( 'Learning_RenderPasses',
start_frame = 1001,
duration = 5,
reels = schematicReels,
shelf_reels = shelfReels )

#use this command to switch to the batch tab
flame.batch.go_to()

#import media
clip1 = flame.batch.import_clip("/var/tmp/flc_python/robot/direct_diffuse/robot_direct_diffuse.[025-029].exr", "direct_passes")
clip1.name = "Direct_Diffuse"
clip2 = flame.batch.import_clip("/var/tmp/flc_python/robot/indirect_diffuse/robot_indirect_diffuse.[025-029].exr", "indirect_passes")
clip2.name = "Indirect_Diffuse"
clip3 = flame.batch.import_clip("/var/tmp/flc_python/robot/direct_specular/robot_direct_specular.[025-029].exr", "direct_passes")
clip3.name = "Direct_Specular"
clip4 = flame.batch.import_clip("/var/tmp/flc_python/robot/indirect_specular/robot_indirect_specular.[025-029].exr", "indirect_passes")
clip4.name = "Indirect_Specular"
clip5 = flame.batch.import_clip("/var/tmp/flc_python/robot/reflection/robot_reflection.[025-029].exr", "reflection")
clip5.name = "Reflection"
clip6 = flame.batch.import_clip("/var/tmp/flc_python/robot/P/robot_P.[025-029].exr", "Utility_Passes")
clip6.name = "Position_Map"
clip7 = flame.batch.import_clip("/var/tmp/flc_python/robot/N/robot_N.[025-029].exr", "Utility_Passes")
clip7.name = "Normals_Map"
clip8 = flame.batch.import_clip("/var/tmp/flc_python/robot/Z/robot_Z.[025-029].exr", "Utility_Passes")
clip8.name = "Z-Depth_Map"

#create nodes and set attributes
comp1 = flame.batch.create_node("Comp")
comp1.name = "Diffuse"
comp1.flame_blend_mode = "Add"

comp2 = flame.batch.create_node("Comp")
comp2.name = "Direct_Specular"
comp2.flame_blend_mode = "Add"

comp3 = flame.batch.create_node("Comp")
comp3.name = "Indirect_Specular"
comp3.flame_blend_mode = "Add"

comp4 = flame.batch.create_node("Comp")
comp4.name = "Reflection"
comp4.flame_blend_mode = "Screen"

writeFile = flame.batch.create_node("Write File")
writeFile.name = "MyComp"

#connect the nodes
flame.batch.connect_nodes(clip1, "BGR", comp1, "Front")
flame.batch.connect_nodes(clip2, "BGR", comp1, "Back")
flame.batch.connect_nodes(comp1, "Result", comp2, "Back")
flame.batch.connect_nodes(clip3, "BGR", comp2, "Front")
flame.batch.connect_nodes(comp2, "Result", comp3, "Back")
flame.batch.connect_nodes(clip4, "BGR", comp3, "Front")
flame.batch.connect_nodes(comp3, "Result", comp4, "Back")
flame.batch.connect_nodes(clip5, "BGR", comp4, "Front")
flame.batch.connect_nodes(comp4, "Result", writeFile, "Front")

#by default, all created nodes are placed at the centre (0,0) on top of each other
#organize automatically sets the position of all nodes in the batch group to avoid overlap
flame.batch.organize()
```

> Agent note: `clip6`–`clip8` (Position, Normals, Z-Depth) are imported but not connected in the source. File paths use the `[025-029]` frame-range pattern.

## Importing Multi-Channel Clip

Imports a multi-channel `.clip` into Batch, creates an Action node with five media layers (`add_media()`), connects each channel socket of the clip node (socket names = channel names, e.g. `"robot_direct_diffuse"`) to a media layer, and connects the Action output (`"output1 [ Comp ]"`) to a Write File node. Change the file location and the channel socket names for your media. APIs: `import_clip`, `create_node("Action")`, `PyActionNode.add_media()`, `connect_nodes`, `organize`.

```python
import flame

schematicReels = [ 'Multi-Channel_Clip' ] #create/name schematic reels
shelfReels = [ 'Extra_Data', ] #create/name shelf reels

#Create batch group
flame.batch.create_batch_group( 'Learning_Multi-Channel',
start_frame = 1001,
duration = 5,
reels = schematicReels,
shelf_reels = shelfReels )

#use this command to switch to the batch tab
flame.batch.go_to()

#import media
clip1 = flame.batch.import_clip("/var/tmp/flc_python/robot/robot_CGI.clip", "Multi-Channel_Clip")
clip1.name = "CGI_Render"

#create nodes and set attributes
action1 = flame.batch.create_node("Action")
action1.name = "Comping_CGI"

direct_diffuse = action1.add_media()
direct_diffuse.name = "Direct_Diffuse"
indirect_diffuse = action1.add_media()
indirect_diffuse.name = "Indirect_Diffuse"
direct_specular = action1.add_media()
direct_specular.name = "Direct_Specular"
indirect_specular = action1.add_media()
indirect_specular.name = "Indirect_Specular"
reflection = action1.add_media()
reflection.name = "Reflection"

writeFile = flame.batch.create_node("Write File")
writeFile.name = "MyComp"

#connect the nodes
flame.batch.connect_nodes(clip1, "robot_direct_diffuse", direct_diffuse, "Front")
flame.batch.connect_nodes(clip1, "robot_indirect_diffuse", indirect_diffuse, "Front")
flame.batch.connect_nodes(clip1, "robot_direct_specular", direct_specular, "Front")
flame.batch.connect_nodes(clip1, "robot_indirect_specular", indirect_specular, "Front")
flame.batch.connect_nodes(clip1, "robot_reflection", reflection, "Front")
flame.batch.connect_nodes(action1, "output1 [ Comp ]", writeFile, "Front")

#by default, all created nodes are placed at the centre (0,0) on top of each other
#organize automatically sets the position of all nodes in the batch group to avoid overlap
flame.batch.organize()
```
