import sympy as sp
import matplotlib.pyplot as plt
from math import cos, sin
from mpl_toolkits.mplot3d import Axes3D


def polar_coordinate3D(num):
    return num * cos(num) * cos(num), num * cos(num) * sin(num), num * sin(num)


# Actual code
primes = list(sp.primerange(0, 10e3))
integers = list(range(0, 2000))
multiplets = [1, 2, 3, 5, 7, 11, 13]
disp_num = ["1", "2", "3", "5", "7", "11", "13", "Primes"]

for i, x in enumerate(multiplets):
    multiplets[i] = list(map(lambda m: m * multiplets[i], integers))
    multiplets[i] = [polar_coordinate3D(k) for k in multiplets[i]]

prime_points = [polar_coordinate3D(p) for p in primes]
multiplets.append(prime_points)

# Plotting
fig = plt.figure()
ax = fig.add_subplot(projection='3d')
ax.set_facecolor((0, 0, 0))

k = 1
for i, x in enumerate(multiplets):
    ax.cla()
    ax.set_axis_off()
    if disp_num[i] == "Primes":
        plt.title(f"Primes")
    else:
        plt.title(f"$n= {disp_num[i]}k, where \; k \in [0, \; 2 \cdot 10³]$")
    x, y, z = zip(*multiplets[i])
    ax.scatter(x, y, z, s=1)

    for angle in range(0, 360):
        ax.view_init(30, angle)
        plt.draw()
        plt.pause(.0000001)
        k+=1
