from polygenerator import random_polygon
import matplotlib.pyplot as plt
import random
import numpy as np
from numpy.linalg import norm
from scipy.spatial.transform import Rotation

def planeTransform(numLayers):
    rotVects = [[1.0, 0.0, 0.0], [0.0, 1.0, 0.0], [0.0, 0.0, 1.0]]
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