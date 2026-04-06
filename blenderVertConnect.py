import pickle
import bpy
import bmesh
import math
import random





with open('listOfListsOfTuples.pkl', 'rb') as f:
    loadedData = pickle.load(f)


#Naming the object
obj_name = "my shape"
#Adding mesh to the object
mesh_data = bpy.data.meshes.new(f"{obj_name}_data")
#Adding mesh object using mesh data
mesh_obj = bpy.data.objects.new(obj_name, mesh_data)
#Links the mesh to my shape and adds it to the scene
bpy.context.scene.collection.objects.link(mesh_obj)

bm = bmesh.new()
#We have our working list of tuples
connectingCoordTuple = loadedData
#Want to break the list of lists of tuples into individual lists of tuples
for tup in connectingCoordTuple:
    vertObjs = [bm.verts.new(coord) for coord in tup]
    
    if len(vertObjs) >= 3:
        bm.faces.new(vertObjs)
bm.verts.ensure_lookup_table()
        
#Writes bmesh data into the mesh data
bm.to_mesh(mesh_data)

#Update the mesh data, this helps with redrawing the mesh in the viewport
mesh_data.update()

#Clean up and free memory that was allocated for the bmesh
bm.free() 
