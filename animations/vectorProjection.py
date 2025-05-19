import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

print("Enter two distinct vectors, separated by spaces (e.g. '3 1' then '2 4'):")
A = np.array(list(map(float, input("Row 1: ").split())))
B = np.array(list(map(float, input("Row 2: ").split())))

mag_a = np.linalg.norm(A)
mag_b = np.linalg.norm(B)

cos_theta = np.dot(A, B) / (mag_a * mag_b)

theta_difference = np.arccos(cos_theta)

theta_projection = (np.pi / 2) - theta_difference

projection = cos_theta * B
print(projection)

proj_vector = np.dot(A,B) / (mag_b ** 2) * B

fig, ax = plt.subplots()
ax.set_aspect('equal')
ax.grid(True)

limit = np.max(np.abs(np.concatenate((A, B))))
ax.set_xlim(-limit,limit)
ax.set_ylim(-limit,limit)

line1 = ax.quiver(0,0,A[0],A[1], angles='xy', scale_units='xy', scale=1, color='red')
line2 = ax.quiver(0,0,B[0],B[1], angles='xy', scale_units='xy', scale=1, color='orange')
line3 = ax.quiver(0,0,proj_vector[0],proj_vector[1], angles='xy', scale_units='xy', scale=1, color='blue')
line4 = ax.quiver(proj_vector[0], proj_vector[1], 0, 0,  angles='xy', scale_units='xy', scale=1, color='pink')

def animate(i):
    t = i/100
    tip = (1 - t) * proj_vector + t * A
    change = tip - proj_vector
    line4.set_UVC(change[0], change[1])
    return line4,

ani = FuncAnimation(fig, animate, frames=101, blit=True, interval=31, repeat=False)

# Show the plot
plt.show()

#hehe