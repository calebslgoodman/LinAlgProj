import numpy as np

def multiply_matrices(A, B):
    return np.dot(A, B)

print(multiply_matrices([1,2],[3,-2]))

A = np.array([[2, 1], [1, 3]])
print("Matrix A:\n", A)