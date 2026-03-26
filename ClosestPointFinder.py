from polygenerator import random_polygon
import matplotlib.pyplot as plt
import random
import numpy as np
from numpy.linalg import norm
from scipy.spatial.transform import Rotation
from mpl_toolkits.mplot3d import Axes3D

def pointsList(info):
    pointList = []
    for group in info:
        for plane in group:
            for pt in plane:
                pointList.append(pt)   
    return(pointList) 

"""All three inputs are list, this is so that we can do
recursion with the function. connectedCoords and coordPlanes are both
empty lists to start"""
def findClosestPoints(coords, connectedCoords, cordPlanes):
    #First check the length of coords
    if len(coords) == 0:
        return(cordPlanes)
    #This check is to make sure the number of coords left to connect is still
    #larger than the random iterations value for now just return
    if len(coords) < 10:
        return(cordPlanes)
    point = []
    
