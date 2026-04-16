from polygenerator import random_polygon
import matplotlib.pyplot as plt
import random
import numpy as np
from numpy.linalg import norm
from scipy.spatial.transform import Rotation
from mpl_toolkits.mplot3d import Axes3D
import math
import pickle

#Returns a list with all of the included points as tuples
def listCompression(listOfLists):
    newListOfTuples = []
    for point in listOfLists:
        newListOfTuples.append(tuple(point))
    return(newListOfTuples)

#This set of instructions generates a list of coordinates for a 2d polygon
#The list has two sets of points for each one generted by the random polygon generator
#One with a z value of zero and one with a z value of one so as to effectively extrude the polygon to three dimensions
x_coords, y_coords = zip(*random_polygon(num_points = random.randint(3,7)))
x_coords = list(x_coords) + [x_coords[0]]
y_coords = list(y_coords) + [y_coords[0]]
listOfCoords = []
for k in range(len(x_coords)):
        coords = [x_coords[k], y_coords[k], 0]
        coordsZ = [x_coords[k], y_coords[k], 1]
        listOfCoords.append(coords)
        listOfCoords.append(coordsZ)
tupleCoords = listCompression(listOfCoords)
print(f"Here's the list: {tupleCoords}")

with open('listOf2dCoordsExtruded.pkl', 'wb') as f:
    pickle.dump(tupleCoords, f)
