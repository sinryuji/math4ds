from sympy import *

A = Matrix([
    [2, 1],
    [6, 3]
])

print(det(A))

# 행렬 A의 행렬식을 구해보면 0이 나오므로 이는 선형 종속이다.
