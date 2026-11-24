<!-- source: Autodesk Flame Family 2027 Help _ Write Your First Python API Script _ Autodesk.html -->
# Write Your First Python API Script

In this section, you will be guided step-by-step using basic functions to successfully write and run your first Python API script. Comments in the code are denoted by the '#' symbol and are there to explain each step with greater detail.

The first thing in any Python API script is the declaration of the python module. This sets up your environment to use the Flame module functions, without it your code will not run.

`python
import flame
`

We can begin using some basic Flame module commands to construct a Batch group and create a small Batch setup.

To create the Batch group we need the name of the reels, and to know our desired start frame and duration values. Building upon the declaration of the Flame module:

`python
import flame

schematicReels = [ 'SchematicReel1', ' SchematicReel2', 'SchematicReel3', 'SchematicReel4' ] #create/name schematic reels
shelfReels = [ 'ShelfReel1', 'ShelfReel2', 'ShelfReel3' ] #create/name shelf reels

#Create batch group with name, start_frame value, duration value, set of schematic reel names, set of shelf reel names
flame.batch.create_batch_group( 'BatchGroupName',
start_frame = 1,
duration = 99,
reels = schematicReels,
shelf_reels = shelfReels )
`

Now that the Batch group is made, we can start on creating our Batch setup with the Python API. A useful command is "Flame.batch.go_to()" which will switch Flame into the Batch tab.

`python
import flame

schematicReels = [ 'SchematicReel1', ' SchematicReel2', 'SchematicReel3', 'SchematicReel4' ] #create/name schematic reels
shelfReels = [ 'ShelfReel1', 'ShelfReel2', 'ShelfReel3' ] #create/name shelf reels

#Create batch group with name, start_frame value, duration value, set of schematic reel names, set of shelf reel names
flame.batch.create_batch_group( 'TheName',
start_frame = 1,
duration = 99,
reels = schematicReels,
shelf_reels = shelfReels )

#use this command to switch to the batch tab
flame.batch.go_to()
`

As a simple example, we will create a Comp Node and a Write File node and connect the output of the Comp Node into the input of the Write File Node. This can be done with a script in 3 lines. To understand this example it must be noted that we can create a node within a script and store a reference to that node within a variable the script so that we can then access it for further operations.

`python
import flame

schematicReels = [ 'SchematicReel1', ' SchematicReel2', 'SchematicReel3', 'SchematicReel4' ] #create/name schematic reels
shelfReels = [ 'ShelfReel1', 'ShelfReel2', 'ShelfReel3' ] #create/name shelf reels

#Create batch group with name, start_frame value, duration value, set of schematic reel names, set of shelf reel names
flame.batch.create_batch_group( 'TheName',
start_frame = 1,
duration = 99,
reels = schematicReels,
shelf_reels = shelfReels )

#use this command to switch to the batch tab
flame.batch.go_to()

#create a comp and writefile node
comp = flame.batch.create_node("Comp") #store the newly created node in a variable called comp
writeFile = flame.batch.create_node("Write File") #store the newly created node in a variable called writeFile

#Connect nodes: flame.batch.connect_nodes(nodename1, "socketname1", nodename2, "socketname2")
flame.batch.connect_nodes(comp, "Result", writeFile, "Front")
#Error msg: Invalid socket name(<type 'exceptions.RuntimeError'>) can occur if the socket name is not exactly what is presented within Flame, the name is case sensitive.
`

A good final step when working with the Python API is to organize your setup. This is because the Python API creates new nodes in the same position, which will lead to overlapping nodes in the Batch Schematic. There are two major ways to fix this.

The first is using the built in function "flame.batch.organize()" which will automatically separate and position all the nodes in the Batch based on connection.

The second method is to assign the positions manually by accessing the nodes X and Y position with the schematic (in the Flame module you can access a nodes position with the 'pos_x' and 'pos_y' attributes).

Using the first method, we end up with this completed script:

`python
import flame

schematicReels = [ 'SchematicReel1', ' SchematicReel2', 'SchematicReel3', 'SchematicReel4' ] #create/name schematic reels
shelfReels = [ 'ShelfReel1', 'ShelfReel2', 'ShelfReel3' ] #create/name shelf reels

#Create batch group with name, start_frame value, duration value, set of schematic reel names, set of shelf reel names
flame.batch.create_batch_group( 'TheName',
start_frame = 1,
duration = 99,
reels = schematicReels,
shelf_reels = shelfReels )

#use this command to switch to the batch tab
flame.batch.go_to()

#create a comp and writefile node
comp = flame.batch.create_node("Comp") #store the newly created node in a variable called comp
writeFile = flame.batch.create_node("Write File") #store the newly created node in a variable called writeFile

#Connect nodes: flame.batch.connect_nodes(nodename1, "socketname1", nodename2, "socketname2")
flame.batch.connect_nodes(comp, "Result", writeFile, "Front")
#Error msg: Invalid socket name(<type 'exceptions.RuntimeError'>) can occur if the socket name is not exactly what is presented within Flame, the name is case sensitive.

#by default, all created nodes are placed at the centre (0,0) on top of each other
#organize automatically sets the position of all nodes in the batch group to avoid overlap
flame.batch.organize()
`

The last step is to run this script, this can be done by clicking the 'Play' button within the Python Console.

As an extra step, using the execution methods shown in Python Console and How to Execute Scripts, you can execute this script when Flame starts and the project is loaded.

For this extra step, you must first save your Python script using the Save icon, keep the file path of where you have saved this script. Then using the `startApplication` command in the terminal, append the `-s` argument and pass your file path to the saved Python script.

The startApplication command example: `/opt/Autodesk/<version>/bin/startApplication -s /home/user/scripts/onStart.py`

## Related pages

- Python API
