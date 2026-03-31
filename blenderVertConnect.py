#Lesson here https://www.youtube.com/watch?v=N3U2noAHgBo
import bpy
import bmesh
import math

"""What we are doing here is everything that you can do from the actual user interface
just with the code, this makes it a little more intuitive for me"""

#Naming the object
obj_name = "my shape"
#Adding mesh to the object
mesh_data = bpy.data.meshes.new(f"{obj_name}_data")
#Adding mesh object using mesh data
mesh_obj = bpy.data.objects.new(obj_name, mesh_data)
#Links the mesh to my shape and adds it to the scene
bpy.context.scene.collection.objects.link(mesh_obj)

bm = bmesh.new()

"""bmesh.ops.create_icosphere(bm, subdivisions = 1, radius = 2.0)


In console can write

import bmesh

bmesh.ops.create_ then press tab to see options
"""

vert_coords = [
    (1.0, 1.0, 0.0),
    (1.0, -1.0, 0.0),
    (-1.0, -1.0, 0.0),
    (-1.0, 1.0, 0.0),
    (0.0, 0.0, 1.0),
]

for coord in vert_coords:
    bm.verts.new(coord)

bm.verts.ensure_lookup_table()   

face_vert_indices = [
    (0, 1, 2, 3),
    (4, 1, 0),
    (4, 2, 1),
    (4, 3, 2),
    (4, 0, 3)
    ]

for vert_indices in face_vert_indices:
    bm.faces.new([bm.verts[index] for index in vert_indices])

#Writes bmesh data into the mesh data
bm.to_mesh(mesh_data)

#Update the mesh data, this helps with redrawing the mesh in the viewport
mesh_data.update()

#Clean up and free memory that was allocated for the bmesh
bm.free()

#Other stuff from the end of the video to play with 

"""
What this does it let you pick vertices on your object
and once you have highlighted them, it will print
a list showing exactly which verts have been selected

mesh_obj = bpy.context.active_object

bm = bmesh.from_edit_mesh(mesh_obj_data)

selected_verts = []

for vert in bm.verts:
    if vert.select:
        selected_verts.append(vert)
        
print("selected vert")
for ver in selected_verts:
    print(f"{vert_index}")

bm.free()"""

"""Alright so here we are going to kind of write the sudo code for creating the objects from the lists in the connectedCoords program
So the first thing to know is that we are receiving a list of tuples. Similarly to how this program does it up above we need to independently go 
through each list of tuples and then connect all of the points in that list to each other.

To start:
#We have our working list of tuples
connectingCoordTuple = listCompression(connectedCoords)
Want to break the list of lists of tuples into individual lists of tuples
for tup in connectingCoordTuple:
    vertObjs = [bm.verts.new(coord) for coord in tup]
    bm.verts.ensure_lookup_table()
    #Make sure that the first item in the list is the connected point
    firstVert = vertObjs[0]
    for i in range(1, len(vertObjs) -1):
        bm.faces.new((firstVert, vertObjs[i], vertObjs[i+1]))
    bm.faces.new((firstVert, vertObjs[-1], vertObjs[1]))
        
    
"""
