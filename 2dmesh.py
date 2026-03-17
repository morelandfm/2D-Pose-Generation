#!/home/devpi/Desktop/2dMesh/2dvenv/bin python
from polygenerator import random_polygon
import matplotlib.pyplot as plt
import pygmsh

def coordsTo3dLol(xcoords, ycoords):
    if len(xcoords) != len(ycoords):
        print("Error, number of x coords and y coords not equal")
    listOfCoords = []
    for i in range(len(xcoords)):
        coords = [xcoords[i], ycoords[i], 0]
        listOfCoords.append(coords)
    return(listOfCoords)





vertices = random_polygon(num_points=4)

x_coords, y_coords = zip(*vertices)
x_coords = list(x_coords) + [x_coords[0]]
y_coords = list(y_coords) + [y_coords[0]]

totCoords = coordsTo3dLol(x_coords, y_coords)
plt.plot(x_coords, y_coords, marker = 'o')
plt.title("Random Test")
plt.xlabel("X Coords")
plt.ylabel("Y Coords")
plt.grid(True)
plt.show()
print(totCoords)