from sympy import *

# 4x + 2y + 4z = 44
# 5x + 3y + 7z = 56
# 9x + 3y + 6z = 72

A = Matrix([
    [4, 2, 4],
    [5, 3, 7],
    [9, 3, 6]
])

# A와 그 역행렬의 점 곱은 항등 행렬을 만듭니다.
inverse = A.inv()
identity = inverse * A

print('역행렬: {}'.format(inverse)) # Matrix([[-1/2, 0, 1/3], [11/2, -2, -4/3], [-2, 1, 1/3]])

print('항등 행렬: {}'.format(identity)) # Matrix([[1, 0, 0], [0, 1, 0], [0, 0, 1]])
