import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

A = np.array([[0.5, -3], [-2, 1]]) #this is what the unit vectors will transform into i --> 0.5, -2   j --> -3, 1
iHat = np.array([1,0])
jHat = np.array([0,1])

iHatT = iHat @ A
jHatT = jHat @ A

ticks = np.arange(-5, 6)
horizontal_lines = []
vertical_lines = []

fig, ax = plt.subplots() #stop forgetting this
ax.set_aspect('equal')
ax.grid(False)

ax.set_xlim(-3, 3)
ax.set_ylim(-3, 3)


quiver_i = ax.quiver(0,0,1,0, angles='xy', scale_units='xy', scale=1, color='red', label='î')
quiver_j = ax.quiver(0,0,0,1, angles='xy', scale_units='xy', scale=1, color='green', label='ĵ')


def animate(i):
    t = i/100
    i_middle = (1-t)*iHat + t*iHatT
    j_middle = (1-t)*jHat + t*jHatT
    quiver_i.set_UVC(i_middle[0], i_middle[1])
    quiver_j.set_UVC(j_middle[0], j_middle[1])
    return quiver_i, quiver_j

ani = FuncAnimation(fig, animate, frames=101, blit=True, interval=31, repeat=False)

# Show the plot
plt.show()

#saveAll?