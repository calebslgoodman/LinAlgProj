import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation


print("Enter a 2x2 matrix A row-by-row, separated by spaces (e.g. '3 1' then '2 4'):")
row1 = list(map(float, input("Row 1: ").split()))
row2 = list(map(float, input("Row 2: ").split()))
A = np.array([row1, row2])

iHat = np.array([1,0])
jHat = np.array([0,1])

iHatT = iHat @ A
jHatT = jHat @ A

ticks = np.arange(-5, 6)
horizontal_lines = []
vertical_lines = []

fig, ax = plt.subplots() #stop forgetting this
ax.set_aspect('equal')
ax.grid(True)

limit = np.max(np.abs(A))
ax.set_xlim(-limit, limit)
ax.set_ylim(-limit, limit)


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