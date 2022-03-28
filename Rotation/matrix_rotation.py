import numpy as np
from math import cos, sin, pi
import matplotlib.pyplot as plt


def matrix_rotation(points, angle):
    point_matrices = [np.array([i[0], i[1]]) for i in points]
    rotation_matrix = np.array([[cos(angle), -sin(angle)],
                                [sin(angle), cos(angle)]])

    result = [np.dot(rotation_matrix, i) for i in point_matrices]
    return [(i[0], i[1]) for i in result]


# Example
fig, ax = plt.subplots()
ax.axis('equal')
ax.set_facecolor((0,0,0))
fig.patch.set_facecolor((0,0,0))
points = [(x, y) for x in range(-5, 6) for y in range(-5, 6)]
points = matrix_rotation(points, pi / 6)

x, y = zip(*points)
plt.scatter(x, y)
plt.show()
