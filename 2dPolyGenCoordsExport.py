from polygenerator import random_polygon
import matplotlib.pyplot as plt
import random
import numpy as np
from numpy.linalg import norm
from scipy.spatial.transform import Rotation
from mpl_toolkits.mplot3d import Axes3D
import math
import pickle

x_coords, y_coords = zip(*random_polygon(num_points = random.randint(3,7)))
x_coords = list(x_coords) + [x_coords[0]]
y_coords = list(y_coords) + [y_coords[0]]
listOfCoords = []
for k in range(len(x_coords)):
        coords = [x_coords[k], y_coords[k], 0]
        coordsZ = [x_coords[k], y_coords[k], 1]
        listOfCoords.append(coords)
        listOfCoords.append(coordsZ)
print(f"Here's the list: {listOfCoords}")

#with open('listOf2dCoords.pkl', 'wb') as f:
    #pickle.dump(randPoly, f)
