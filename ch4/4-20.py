from numpy import array, diag
from numpy.linalg import eig, inv

A = array([
    [1, 2],
    [4, 5]
])

eigenvals, eigenvecs = eig(A)

print('고윳값')
print(eigenvals)
print('\n고유 벡터')
print(eigenvecs)
