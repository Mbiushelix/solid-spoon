import pyqtgraph.opengl as gl
import sys
import sympy as sp
from math import cos, sin
import numpy as np
from pyqtgraph.Qt import QtGui


def polar_coordinate3D(num):
    return np.array([num * cos(num) * cos(num), num * cos(num) * sin(num), num * sin(num)])


n = 200000
primes = list(sp.primerange(0, n))
points = np.array([polar_coordinate3D(p) for p in primes])

app = QtGui.QApplication([])
w = gl.GLViewWidget()
w.show()
g = gl.GLGridItem()
w.addItem(g)

# Create the scatter plot and add it to the view
scatter = gl.GLScatterPlotItem(pos=points, size=0.5, color=(1, 0, 0, 1), pxMode=False)
w.addItem(scatter)

sys.exit(app.exec_())
