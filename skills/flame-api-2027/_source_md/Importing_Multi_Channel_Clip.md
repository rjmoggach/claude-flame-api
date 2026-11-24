<!-- source: Autodesk Flame Family 2027 Help _ Importing Multi-Channel Clip _ Autodesk.html -->
# Importing Multi-Channel Clip

This example has been featured in our Working With Python Scripting video on *The Flame Learning Channel*. This script shows how a user can get a quick start within Batch when working with multi-channel clips.

To use this script, you must change the import clip file location to your own media's location and the names of the sockets for each channel when connecting nodes.

`python
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
`

## Related pages

- Python API Examples
