import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

v = np.array([2,-3])
scalar = -0.5

def scale_value(t, scalar):
    return (1 - t) * 1 + t * scalar
#gradual transform

fig, ax = plt.subplots()
ax.set_aspect('equal')
ax.grid(True)

quiver = ax.quiver(0,0,0,0, angles='xy', scale_units='xy', scale=1, color='red')

def init():
    quiver.set_UVC(0,0)
    return quiver,

def animate(i):
    t = i/100
    s = scale_value(t, scalar)
    scaled_v = s * v

    quiver.set_UVC(scaled_v[0], scaled_v[1])
    ax.set_xlim(-3, 3)
    ax.set_ylim(-3, 3)
    ax.set_title(f"Vector scaled by {s:.2f}")
    return quiver,

ani = FuncAnimation(fig, animate, frames=101, init_func=init, blit=True, interval=30, repeat=False)
plt.show()