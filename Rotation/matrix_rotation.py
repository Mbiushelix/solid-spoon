import numpy as np
from math import cos , sin , sqrt, pi
from numpy import linspace
import matplotlib.pyplot as plt

def matrix_rotation(points,angle):
    point_matrices = [np.array([i[0],i[1]]) for i in points]
    rotation_matrix = np.array([[cos(angle),-sin(angle)],
                             [sin(angle),cos(angle)]])
    
    result = [np.dot(rotation_matrix,i) for i in point_matrices]
    return [(i[0], i[1]) for i in result]


def gen_cube(x,y,length, height):
    x = linspace(x - length/2, x + length/2, 20)
    h_y = linspace(y - height/2, y+ height/2, 20)
    
    h1_points = list(zip([x[0]]*len(h_y),h_y))
    h2_points = list(zip([x[-1]]*len(h_y), h_y))
    l1_points = list(zip(x,[h_y[0]]*len(x)))
    l2_points = list(zip(x,[h_y[-1]]*len(x)))
    
    return h1_points + h2_points + l1_points + l2_points 

points= matrix_rotation(gen_cube(0,0,10,10), pi)
print(points)

x, y = zip(*points)
plt.scatter(x,y)
plt.show()