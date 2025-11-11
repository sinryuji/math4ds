from numpy import array

y = array([1, 2])

i_hat = array([-2, 1])
j_hat = array([1, -2])

basis = array([i_hat, j_hat])

print(basis.dot(y))
