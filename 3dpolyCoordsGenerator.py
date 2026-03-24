#The actual 3D coords are currently being generated properly
#We don't need a z rotation as that just rotates an already random polygon in the x-y plane in the same plane
    #This has been changed but needs to be tested
#Working on mapping the points
#Next step is to create a .csv file that you can export all of these values to
from polygenerator import random_polygon
import matplotlib.pyplot as plt
import random
import numpy as np
from numpy.linalg import norm
from scipy.spatial.transform import Rotation
#Added libraries for testing here
from matplotlib.tri import Triangulation

def planeTransform(numLayers):
    rotVects = [[1.0, 0.0, 0.0], [0.0, 1.0, 0.0]]
    transLayers = []
    for layer in numLayers:
        transPlanes = []
        for plane in layer:
            transCoords = []
            randVect = random.choice(rotVects)
            angleDeg = random.randint(0, 360)
            rotVector = np.deg2rad(angleDeg) * np.array(randVect)
            rot = Rotation.from_rotvec(rotVector)
            for point in plane:
                transformedCoords = rot.apply(point)
                transCoords.append(transformedCoords)
            transPlanes.append(transCoords)
        transLayers.append(transPlanes)
    return(transLayers)

#Testing for future starting here
#Need to take all of the information and split it into specific x, y, and z values, store them as lists and return the lists
#Try this out to see what you get
def separateCoords(polyInfo):
    x, y, z = [], [], []
    for group in polyInfo:
        for plane in group:
            for pt in plane:
                x.append(pt[0])
                y.append(pt[1])
                z.append(pt[2])
    return x, y, z
         
          
     

def randPolyGenerator(iters):
    listOfLayers = []
    for i in range(iters):
        randPoints = random.randint(3, 7)
        vertices = random_polygon(num_points=randPoints)
        x_coords, y_coords = zip(*vertices)
        x_coords = list(x_coords) + [x_coords[0]]
        y_coords = list(y_coords) + [y_coords[0]]
        listOfCoords = []
        for k in range(len(x_coords)):
                coords = [x_coords[k], y_coords[k], 0]
                listOfCoords.append(coords)
        listOfLayers.append(listOfCoords)
    return(listOfLayers)

randIters = random.randint(3, 7)
layersList = [randPolyGenerator(randIters)]
print(layersList)
randPlane = planeTransform(layersList)
print(f"Plane transform: {randPlane}")

#New for testing plotting the actual points
x_list, y_list, z_list  = separateCoords(randPlane)
ax.scatter(x_list, y_list, z_list)
ax.set_title('3D Scarrter Plot from List')
plt.show()
