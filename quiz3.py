import numpy as np

def photos():
    A = np.array([[10,15,40], [1, -1, -1], [0, 1, -2]])
    b = np.array([300, 0, 0])
    x = np.linalg.solve(A, b)
    return x
print(photos())
