from polygenerator import random_polygon
import matplotlib.pyplot as plt
import random
import numpy as np
from numpy.linalg import norm
from scipy.spatial.transform import Rotation
from mpl_toolkits.mplot3d import Axes3D

#Takes a list of lists of lists and turns it into a list of points (x, y, z) and returns that list
def pointsList(info):
    pointList = []
    for group in info:
        for plane in group:
            for pt in plane:
                pointList.append(pt)   
    return(pointList) 

#Takes a list of points, determines their magnitude and orders them
#in the size of their magnitude with respect to the origin
#Need to change this to distance from point
def distanceFromOrigin(coords):
    magnitude = []
    for point in coords:
        mag = np.linalg.norm(point)
        magnitude.append(mag)
    zipped = zip(magnitude, coords)
    sortedZip = sorted(zipped, key=lambda x: x[0], reverse=True)
    sortedMags, sortedCoords = zip(*sortedZip)
    return(sortedCoords)

###
#Will replace distanceFromOrigin func, as the initial point will just become (0,0,0)
#Just make sure that you are passing to this function the coords list that doesn't have the initialPoint in it
def distanceFromPoint(initialPoint, coords):
    if np.linalg.norm(initialPoint) == 0:
        magnitude = []
        for point in coords:
            mag = np.linalg.norm(point)
            magnitude.append(mag)
        zipped = zip(magnitude, coords)
        sortedZip = sorted(zipped, key=lambda x: x[0], reverse=True)
        sortedMags, sortedCoords = zip(*sortedZip)
        return(sortedCoords)
    vectList = []
    for point in coords:
        vect = [(initialPoint[0]-point[0], initialPoint[1]-point[1], initialPoint[2]-point[2])]
        vectList.append(vect)
    vectMag = []
    for point in vectList:
        mag = np.linalg.norm(point)
        vectMag.append(mag)
    zipped = zip(vectMag, coords)
    sortedZip = sorted(zipped, key=lambda x: x[0], reverse=True)
    sortedMags, sortedCoords = zip(*sortedZip)
    return(sortedCoords)



def connectedCoords(numConns, initialPoint, coords):

    return()

def planeMaker(coords, connectedCoords, planeCoords):
    #Determining if the function has finished and will break out of the recursion
    if len(coords) == 0:
        return planeCoords
    #Statement for making sure that there are enough points remaining that can be connected with the random number generated for connected points
    if len(coords) < 7:
        #connect remaining points
        return
    
    #First things first, we need to determine everything's distance from the origin
    newCoords = distanceFromOrigin(coords)
    #Make a random number of points for the chosen point to connect to
    randConnectedPoints = random.randint(4, 7)
    #Take our first point
    pointToBeConnected = coords[0]
    #Remove chosen point from the coords list
    del coords[0]
    #Make a list for the points to be connected
    #Needs to find the number of points closest to it based off the random int pulled
    #Use another func to do this
    #Func needs to take in the random number, the list of coords, and the connected coord



    return(coords)


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
    
    
