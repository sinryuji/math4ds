from numpy import array, diag
from numpy.linalg import eig, inv

A = array([
    [3, 1, 0],
    [2, 4, 1],
    [3, 1, 8]
])

eigenvals, eigenvecs = eig(A)

print("고윳값: ", eigenvals)
print("고유 벡터: ", eigenvecs)

Q = eigenvecs
R = inv(Q)

L = diag(eigenvals)
B = Q @ L @ R

print(B)
