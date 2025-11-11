# 역행렬은 행렬에 곱했을 때 항등 행렬로 만드는 행렬이다.
from numpy import array
from numpy.linalg import inv

A = array([
    [3, 1, 0],
    [2, 4, 1],
    [3, 1, 8]
])

A_inv = inv(A)

print(A_inv)
