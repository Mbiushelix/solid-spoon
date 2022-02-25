import sys
import sympy as sp
import pyqtgraph as pg
from math import cos, sin


def polar_coordinate(num):
    return num * cos(num), num * sin(num)


n = 20000
primes = list(sp.primerange(0, n))
points = [polar_coordinate(p) for p in primes]
x, y = zip(*points)

# Set white background and black foreground
pg.setConfigOption('background', 'k')
pg.setConfigOption('foreground', 'k')

# Create the main application instance
app = pg.mkQApp()

# Create the view
view = pg.PlotWidget()
view.resize(800, 600)
view.setWindowTitle('Scatter plot of primes in polar form')
view.setAspectLocked(True)
view.show()

# Create the scatter plot and add it to the view
scatter = pg.ScatterPlotItem(pen=pg.mkPen(width=0, color='r'), symbol='o', size=1)
view.addItem(scatter)
scatter.setData(x, y)

sys.exit(app.exec_())
