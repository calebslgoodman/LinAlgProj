import numpy as np

def dot(A, B):
    return np.dot(A, B) # only 1 vector per matrix

def cross(A, B):
    return np.cross(A, B) # this is also giving a weird response [-40, 10]. usually only one column

def inverse(A):
    return np.linalg.inv(A) # only squares

def det(A):
    return np.linalg.det(A) # linear independence, dimensions later

def rank(A):
    return np.linalg.matrix_rank(A) # see determinant

# numpy.linalg.tensorsolve, later


n1 = np.array([[1, 3], [-2, 0]])
n2 = np.array([5, -7, 2])
n3 = np.array([[10, -10], [8, -5]])
n4 = np.array([1, 3, 45])
'''
print(dot(n1, n3))
print(inverse(n1))
'''