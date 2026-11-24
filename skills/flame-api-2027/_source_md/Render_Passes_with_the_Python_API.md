<!-- source: Autodesk Flame Family 2027 Help _ Render Passes with the Python API _ Autodesk.html -->
# Render Passes with the Python API

This example has been featured in our Working With Python Scripting video on *The Flame Learning Channel*. This script automates the workflow within Batch of a multi-pass render. It does so by importing several clips and making the proper connection between them and several "Comp" nodes.

To use this script, you must change the import clip file locations with your own media's location and adjust the render pass setup according to your media.

`python
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
`

## Related pages

- Python API Examples
