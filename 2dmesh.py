#Alright, what we need to do is randomly generate multiple 2d polygon planes, then randomly attach the points between them to create the 3d object.
#This is going to take some work
#For determining how the 
#!/home/devpi/Desktop/2dMesh/2dvenv/bin python
from polygenerator import random_polygon
import matplotlib.pyplot as plt
import random

#Creating the randomized points for the polygon, iters is the number of times that the program will run for the sheer amount of layers
#Will need some testing of the layers to determine a good number, speculation: something between 3-8
#We can assign a random integer to each individiual z value, and then order the values in the listOfCoords before being output if we want
def coordsTo2dLol(xcoords, ycoords, iters):
    if len(xcoords) != len(ycoords):
        print("Error, number of x coords and y coords not equal")
    listOfLayers = []
    for k in iters:
        listOfCoords = []
        for i in range(len(xcoords)):
            #Generates a new z value between 0 and 1
            zVal = np.random.rand()
            coords = [xcoords[i], ycoords[i], 0]
            listOfCoords.append(coords)
        listOfLayers.append(listOfCoords)
    return(listOfCoords)


def randPolyGenerator(iters):
    listOfLayers = []
    for i in iters:
        randPoints = random.randint(3, 8)
        vertices = random_polygon(num_points=randPoints)
        x_coords, y_coords = zip(*vertices)
        x_coords = list(x_coords) + [x_coords[0]]
        y_coords = list(y_coords) + [y_coords[0]]
        listOfCoords = []
            for k in range(len(x_coords)):
                coords = [x_coords[k], y_coords[k], 0]
                listOfCoords.append(coords)
        listOfLayers.append(listOfCoords)
        
randPoints = random.randint(3, 8)
randIters = random.randint(3, 8)
vertices = random_polygon(num_points=randPoints)

x_coords, y_coords = zip(*vertices)
x_coords = list(x_coords) + [x_coords[0]]
y_coords = list(y_coords) + [y_coords[0]]

totCoords = coordsTo2dLol(x_coords, y_coords, randIters))
plt.plot(x_coords, y_coords, marker = 'o')
plt.title("Random Test")
plt.xlabel("X Coords")
plt.ylabel("Y Coords")
plt.grid(True)
plt.show()
print(totCoords)
