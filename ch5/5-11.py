import pandas as pd
from sympy import *

# CSV에서 데이터를 로드합니다
points = list(pd.read_csv("https://bit.ly/2KF29Bd").itertuples())

m, b, i, n = symbols('m b i n')
x, y = symbols('x y', cls=Function)

sum_of_squares = Sum((m*x(i) + b - y(i)) ** 2, (i, 0, n))

d_m = diff(sum_of_squares, m) \
    .subs(n, len(points) - 1).doit() \
    .replace(x, lambda i: points[i].x) \
    .replace(y, lambda i: points[i].y)

d_b = diff(sum_of_squares, b) \
    .subs(n, len(points) - 1).doit() \
    .replace(x, lambda i: points[i].x) \
    .replace(y, lambda i: points[i].y)

# 계산 속도를 높이기 위해 lambdify로 컴파일합니다
d_m = lambdify([m, b], d_m)
d_b = lambdify([m, b], d_b)

# 모델 계수를 초기화합니다
m = 0.0
b = 0.0

# 학습률
L = .001

# 반복 횟수
iterations = 100_000

# 경사 하강법을 수행합니다
for i in range(iterations):

    # m과 b를 업데이트합니다
    m -= d_m(m,b) * L
    b -= d_b(m,b) * L

print("y = {0}x + {1}".format(m, b))
# y = 1.939393939393954x + 4.733333333333231
