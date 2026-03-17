from polygenerator import random_polygon
import matplotlib.pyplot as plt

vertices = random_polygon(num_points=10)

x_coords, y_coords = zip(*vertices)
x_coords = list(x_coords) + [x_coords[0]]
y_coords = list(y_coords) + [y_coords[0]]

plt.plot(x_coords, y_coords, marker = 'o')
plt.title("Random Test")
plt.xlabel("X Coords")
plt.ylabel("Y Coords")
plt.grid(True)
plt.show()