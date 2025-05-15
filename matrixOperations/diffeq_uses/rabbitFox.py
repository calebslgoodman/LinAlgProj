import numpy as np
import matplotlib.pyplot as plt

rabbit2fox = 8 #fox per rabbit equilibirum
rabbits = 1000 #given number of rabbits that we want to start at
foxes = rabbits/rabbit2fox

carryingCapacity = 10000 #maximum amount of rabbits that can survive: logistic model

#x is rabbit y is fox
if rabbits > carryingCapacity:
    x, y = np.meshgrid(np.linspace(0.1, 2*carryingCapacity, 20), np.linspace(0.1, 2*carryingCapacity/rabbit2fox, 20))
else:
    x, y = np.meshgrid(np.linspace(0.1, 2*rabbits, 20), np.linspace(0.1, 2*foxes, 20))

dx = x * (1 - y/foxes) * (1-x/carryingCapacity)
dy = -y * (1 - x/rabbits)

plt.streamplot(x, y, dx, dy)
plt.xlabel('Rabbits')
plt.ylabel('Foxes')
plt.title('Predator-Prey Phase Diagram')
plt.show()

#this shows how, given a starting point, you go around a circle lol