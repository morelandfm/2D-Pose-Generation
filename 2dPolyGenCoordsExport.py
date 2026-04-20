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

#Takes in a list of lists of tuples, averages and returns a points at the average "centroid"
def centroid(points):
    xCoords, yCoords, zCoords = separateCoords(points)
    avgX = sum(xCoords) / len(xCoords)
    avgY = sum(yCoords) / len(yCoords)
    return(avgX, avgY)

#Separates the list of lists of tuples into their respective coordinates and returns the list
def separateCoords(polyInfo):
    x, y, z = [], [], []
    for pt in polyInfo:
        x.append(pt[0])
        y.append(pt[1])
        z.append(pt[2])
    return x, y, z 

#Adjusts all of the values so that the centroid of the object wrt the xy plane is at zero
def center(points):
    centeredCoords = []
    cx, cy = centroid(points)
    for coord in points:
        centeredCoords.append((coord[0] - cx, coord[1] - cy, coord[2]))
    return centeredCoords

#Takes in a list of tuples and orders them CCW
def ccwOrder(listOfTuples):   
    return sorted(listOfTuples, key=lambda p: math.atan2(p[1], p[0]))

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
centeredTupleCoords = center(tupleCoords)
#orderedTuples = ccwOrder(centeredTupleCoords)
orderedTuples = ccwOrder(centeredTupleCoords)
print(f"Here's the list: {orderedTuples}")
print(f"Other list to compare: {centeredTupleCoords}")

#with open('listOf2dCoordsExtruded.pkl', 'wb') as f:
    #pickle.dump(tupleCoords, f)

