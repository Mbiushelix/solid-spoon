# -*- coding: utf-8 -*-

from numpy import real, imag
from math import cos,sin

def complex_rotate(points,angle):
    points = [(p[0]+ p[1]*1j)*(cos(angle)+sin(angle)*1j) for p in points]
    return [(real(p),imag(p)) for p in points]


# An example:
# import matplotlib.pyplot as plt
# from numpy import linspace
# from math import pi
    
# def gen_cube(x,y,length, height):
#     x = linspace(x - length/2, x + length/2, 2000)
#     h_y = linspace(y - height/2, y+ height/2, 2000)
    
#     print([x[0]]*len(h_y))
#     h1_points = list(zip([x[0]]*len(h_y),h_y))
#     h2_points = list(zip([x[-1]]*len(h_y), h_y))
#     l1_points = list(zip(x,[h_y[0]]*len(x)))
#     l2_points = list(zip(x,[h_y[-1]]*len(x)))
    
#     return h1_points + h2_points + l1_points + l2_points 
    
# a = gen_cube(0,0,10,10)
# b = complex_rotate(a,(30*pi)/(180))
# plt.scatter(*zip(*b))
# plt.axis('equal')
# plt.show()
