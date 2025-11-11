from numpy import array
from numpy.linalg import det

i_hat = [1, 0]
j_hat = [2, 2]

basis = array([i_hat, j_hat]).transpose()

determinant = det(basis)

print(determinant)
