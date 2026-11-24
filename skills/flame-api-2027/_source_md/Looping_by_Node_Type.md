<!-- source: Autodesk Flame Family 2027 Help _ Looping by Node Type _ Autodesk.html -->
# Looping by Node Type

A basic functionality of any programming language is the capability to loop through several objects. This functionality can be used within the Python API to speed up a user's workflow.

This example uses the `flame.batch.nodes` function to obtain a list of all nodes within the Batch schematic. We can then use a *for-loop* to cycle through each node. In this case, while we cycle through each node we are checking for a certain conditions using an *if* statement. This allows us to apply changes to the desired type of node.

The first example finds all Action media nodes within the Batch schematic and changes their position if they do not meet a certain condition.

`python
import flame

for i in flame.batch.nodes: #for every node in the batch group
    if i.type == "Action Media" and i.pos_y < 99: #if the node is an Action Media node and lower than 99 from centre
        i.pos_y -= 100 #move the media node by subtracting 100 from current ypos
`

The second example has been featured in our Working With Python Scripting video on *The Flame Learning Channel*. It finds all Comp nodes within the batch schematic and changes their blend mode to "Add".

`python
import flame

for n in flame.batch.nodes:
    if n.type == "Comp":
        n.flame_blend_mode = "Add"
`

## Related pages

- Python API Examples
