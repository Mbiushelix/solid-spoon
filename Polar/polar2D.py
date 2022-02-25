import sympy as sp
import matplotlib.pyplot as plt
from math import cos, sin
from matplotlib.animation import FuncAnimation

# Actual code
primes = list(sp.primerange(0, 10e3))
integers = list(range(0, 20000))

multiplets = [1]
multiplets.extend(primes[0:50])

disp_num = [str(x) for x in multiplets]
disp_num.append("Primes")


def polar_coordinate(num):
    return num * cos(num), num * sin(num)


for i, x in enumerate(multiplets):
    multiplets[i] = list(map(lambda m: m * multiplets[i], integers))
    multiplets[i] = [polar_coordinate(k) for k in multiplets[i]]

prime_points = [polar_coordinate(p) for p in primes]
multiplets.append(prime_points)

# Plotting code
fig, ax = plt.subplots()
ax.set_aspect(1)
ax.set_facecolor((0, 0, 0))
plt.rcParams['lines.markersize'] = 1


def animate(i):
    ax.cla()
    if disp_num[i] == "Primes":
        plt.title(f"Primes")
    else:
        plt.title(f"$n= {disp_num[i]}k, where \; k \in [0, \; 2 \cdot 10⁴]$")

    plt.xlim([-10000, 10000])
    plt.ylim([-10000, 10000])
    plt.scatter(*zip(*multiplets[i]))


anim = FuncAnimation(fig, animate, interval=1000)
plt.show()