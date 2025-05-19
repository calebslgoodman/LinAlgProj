import numpy as np
from numpy import linalg as LA
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation


#when you watch this, take a look at how the unit vectors are rotated off their axis but the eigenvectors are not

print("Enter a 2x2 matrix A row-by-row, separated by spaces (e.g. '3 1' then '2 4'):")
row1 = list(map(float, input("Row 1: ").split()))
row2 = list(map(float, input("Row 2: ").split()))
A = np.array([row1, row2])


i_hat = np.array([1,0])
j_hat = np.array([0,1])

i_hat_done = i_hat @ A
j_hat_done = j_hat @ A

eigenvalues, eigenvectors = LA.eig(A)
'''
it took me forever to realize where my scaling was going wrong, and it's because this function returns the normalized values of the eigenvectors
with magnitude 1, rather than the [1,2] and the [1,-1] that i expected. actually, it's even worse because it was going in the entire wrong direction
but that doesn't necessarily matter because any vector on the same line as the 'eigenvector' is itself an eigenvector.
attempting to scale the axes later is going to be horrible, it's been giving me sm trouble as of now. 
'''  

fig, ax = plt.subplots()
ax.set_aspect('equal')
ax.grid(True)

limit = np.max(np.abs(A))  # max absolute value of any input

ax.set_xlim(-limit, limit)
ax.set_ylim(-limit, limit)

i_quiver = ax.quiver(0,0,1,0, angles='xy', scale_units='xy', scale=1, color='red')
j_quiver = ax.quiver(0,0,0,1, angles='xy', scale_units='xy', scale=1, color='red')
e1_quiver = ax.quiver(0,0,eigenvectors[0, 0], eigenvectors[0, 1], angles='xy', scale_units='xy', scale=1, color='green')
e2_quiver = ax.quiver(0,0,eigenvectors[1, 0], eigenvectors[1, 1], angles='xy', scale_units='xy', scale=1, color='green')



def animate(i):
    t = i/100
    i_middle = (1-t)*i_hat + t*i_hat_done #all of these are arrays
    j_middle = (1-t)*j_hat + t*j_hat_done
    e1_scaled = eigenvectors[:, 0] * (1*(1-t) + t * (eigenvalues[0]))
    e2_scaled = eigenvectors[:, 1] * (1*(1-t) + t * (eigenvalues[1]))

    i_quiver.set_UVC(i_middle[0], i_middle[1])
    j_quiver.set_UVC(j_middle[0], j_middle[1])
    e1_quiver.set_UVC(e1_scaled[0], e1_scaled[1])
    e2_quiver.set_UVC(e2_scaled[0], e2_scaled[1])
    return i_quiver, j_quiver, e1_quiver, e2_quiver

ani = FuncAnimation(fig, animate, frames=101, blit=True, interval=20, repeat=False)

# Show the plot
plt.show()
