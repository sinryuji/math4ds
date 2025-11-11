from numpy import array

y = array([1, 2])

i_hat = array([2, 0])
j_hat = array([0, 1.5])

basis = array([i_hat, j_hat])

print(basis.dot(y))
