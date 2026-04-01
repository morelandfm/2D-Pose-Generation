#Next steps: Determining a better rotation method to get points further into the z plane
from polygenerator import random_polygon
import matplotlib.pyplot as plt
import random
import numpy as np
from numpy.linalg import norm
from scipy.spatial.transform import Rotation
from mpl_toolkits.mplot3d import Axes3D
import math

#Take in 2d coordinates and transform them across either the x or y axis and
#return the list
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

#Used to graph/visuallize the list by splitting the list
#into its x, y and z values before being passed to a graphing func
def separateCoords(polyInfo):
    x, y, z = [], [], []
    for group in polyInfo:
        for plane in group:
            for pt in plane:
                x.append(pt[0])
                y.append(pt[1])
                z.append(pt[2])
    return x, y, z     

#Returns a single list with all of the included points
def pointsList(info):
    pointList = []
    for group in info:
        for plane in group:
            for pt in plane:
                pointList.append(pt)   
    return(pointList)

"""Take in a number of connections to iterate over, an initial point that will be used to determine the connections
and then a list of coords from the reamining list"""
def connectedCoords(numConns, initialPoint, coords):
    # Get neighbors sorted by distance from the initial point
    sortedNeighbors = distanceFromPoint(initialPoint, coords, 1)    
    # Start the list with the initial point
    coordsToConnect = [initialPoint]
    # Append the closest N neighbors
    coordsToConnect.extend(sortedNeighbors[:numConns])
    return coordsToConnect

"""Here is the big one, take in a list of coord and return an appended list of coords without the newly connected point, and the new list to be connected
"""
def planeMaker(coords, polyConnectCoords=None):
    if polyConnectCoords is None:
        polyConnectCoords = []
    #Determining if the function has finished and will break out of the recursion
    if len(coords) == 0:
        return print("Error, no coords in the arguement")
    #Statement for making sure that there are enough points remaining that can be connected with the random number generated for connected points
    if len(coords) < 7:
        #Makes a list of coords by distance from zero, ordered highest to lowest
        newCoords = distanceFromPoint([(0,0,0)],coords, 0)
        #Take our first point which is the furthest point from the origin
        pointToBeConnected = newCoords[0]
        #Remove chosen point from the coords list
        newNewCoords =  newCoords[:1]
        #Make an empty list to be done, could also just change newCoords to be an empty list
        emptyList = []
        #connect remaining points
        #Make a list for the points to be connected, ensure to use the 1 so that it returns the list of points closest to the pointToBeConnected
        orderedListFromConnectingPointToConnectedPoints = distanceFromPoint(pointToBeConnected, newNewCoords, 1)
        #List of points that will actually be getting connected to each other
        polyConnectCoords.append(connectedCoords(len(coords), pointToBeConnected, orderedListFromConnectingPointToConnectedPoints))
        return(emptyList, polyConnectCoords)
    
    #First things first, we need to determine everything's distance from the origin, this will give us an ordered list from high to low
    newCoords = distanceFromPoint([(0,0,0)],coords, 0)
    #Take our first point which is the furthest point from the origin
    pointToBeConnected = newCoords[0]
    #Remove chosen point from the coords list
    newNewCoords =  newCoords[1:]
    #Make a list for the points to be connected, ensure to use the 1 so that it returns the list of points closest to the pointToBeConnected
    orderedListFromConnectingPointToConnectedPoints = distanceFromPoint(pointToBeConnected, newNewCoords, 1)
    #List of points that will actually be getting connected to each other
    polyConnectCoords.append(connectedCoords(random.randint(4,7), pointToBeConnected, orderedListFromConnectingPointToConnectedPoints))
    return(planeMaker(newNewCoords, polyConnectCoords))

#Determining the distance each point is from the origin with its magnitude and then ordering the points from highest to lowest and 
#returning the list of points
def distanceFromOrigin(coords):
    magnitude = []
    for point in coords:
        mag = np.linalg.norm(point)
        magnitude.append(mag)
    zipped = zip(magnitude, coords)
    sortedZip = sorted(zipped, key=lambda x: x[0], reverse=True)
    sortedMags, sortedCoords = zip(*sortedZip)
    return(sortedMags,sortedCoords)

###
"""
#This is a list of lists of tuples, going to need to index as such
def ccwOrder(list):
    for lists in list:
        #Now we have a list of tuples, this should be done in the order of the connected points
        #Split the list into the connecting point and all of the other points
        center = lists[0]
        coords = lists[1:]
        #Now center is the connecting coordinate and coords is the rest of the coordinates in the list, but each is a tuple
        #X check to see if x is the biggest
        if center[0] > center[1] and center[0] > center[2]
            #X is the biggest value order by angles in yz plane
            ccwX = []
            for point in coords:
                dy = coords[point[1] - center[1]
                dz = coords[point[2] - center[2]
                rads = math.atan2(dy, dz)
                degs = math.degrees(rads)
                ccwX.append(degs)
        if center[1] > center[0] and center[1] > center[2]
            #Y is the biggest value order by angles in xz plane
            ccwY = []
            for point in coords:
                dx = coords[point[0] - center[0]
                dz = coords[point[2] - center[2]
                rads = math.atan2(dx, dz)
                degs = math.degrees(rads)
                ccwY.append(degs)
        if center[2] > center[1] and center[2] > center[0]
            #Z is the biggest value order by angles in xy plane
            ccwZ = []
            for point in coords:
                dy = coords[point[1] - center[1]
                dx = coords[point[0] - center[0]
                rads = math.atan2(dy, dx)
                degs = math.degrees(rads)
                ccwX.append(degs)"""
def ccwOrder(listOfLists):
    orderedResults = []

    for pointsList in listOfLists:
        center = pointsList[0]
        coords = pointsList[1:]
        
        # 1. Determine which plane to use
        # X is largest: Use YZ plane
        if center[0] > center[1] and center[0] > center[2]:
            # Sort by atan2(dy, dz)
            coords.sort(key=lambda p: math.atan2(p[1] - center[1], p[2] - center[2]))
            
        # Y is largest: Use XZ plane
        elif center[1] > center[0] and center[1] > center[2]:
            # Sort by atan2(dx, dz)
            coords.sort(key=lambda p: math.atan2(p[0] - center[0], p[2] - center[2]))
            
        # Z is largest: Use XY plane
        else:
            # Sort by atan2(dy, dx)
            coords.sort(key=lambda p: math.atan2(p[1] - center[1], p[0] - center[0]))
        
        # Re-combine center with the now-sorted coordinates
        orderedResults.append([center] + coords)
        
    return orderedResults

#Blender makes it shapes from a list of tuples, so we need to convert the list of lists to a list of tuples with this function
def listCompression(listOfLists):
    newListOfTuples = []
    for point in listOfLists:
        listOfTuples = [tuple(sublist) for sublist in point]
        newListOfTuples.append(listOfTuples)
    return(newListOfTuples)

#The initial check is getting an ordered list based on how far they are from the origin and working back towards it,
#the next check is for ordering points based off of how close they are to the one being connected...  Maybe make two different ones
#Returns a sorted list of coordinates based on their distance from the initial point from high to low
def distanceFromPoint(initialPoint, coords, initialCheck):
    if not coords:
        return []
    
    # Use NumPy to calculate distances for the whole list at once (much faster)
    coords_arr = np.array(coords)
    
    if initialCheck == 0:
        # Distance from origin
        distances = np.linalg.norm(coords_arr, axis=1)
        # Sort descending (furthest first)
        indices = np.argsort(-distances)
    else:
        # Distance from initialPoint
        distances = np.linalg.norm(coords_arr - np.array(initialPoint), axis=1)
        # Sort ascending (closest first)
        indices = np.argsort(distances)
        
    return coords_arr[indices].tolist()


#Getting way too many zeros here, gotta figure that out
#Generates a random polygon in x, y and then adds a zero for z val
#Returns the list
#Currently running as intended, could be made more efficient
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

#Random number of iterations for the random polygon
randIters = random.randint(3, 4)
#List of all of the layers generated by the random polygon generator, currently zero z values, hasn't been transformed yet
layersList = [randPolyGenerator(randIters)]
#Now all of the layers have been randomly transformed across the x or y axis with new z values and stored in this list
randPlane = planeTransform(layersList)
#Turn the list of lists into a single list
points = pointsList(randPlane)

###NEW TESTING HERE
emptyList, listOfPlanestoBeAttached = planeMaker(points)
planesAsTuples = listCompression(listOfPlanestoBeAttached)
ccwOrderedListOfListOfTuples = ccwOrder(planesAsTuples)
#print(f"List of prePoints: {points}")
#print(f"List of points: {listOfPlanestoBeAttached}")
#print(f"List of planes as tuples: {planesAsTuples}")
print(f"List of CCW ordered planes as a list of tuples: {ccwOrderedListOfListOfTuples}")
