import pandas as pd
from sympy.solvers.diophantine.diophantine import sum_of_squares

# 데이터 로드하기
points = pd.read_csv('https://bit.ly/3goOAnt', delimiter=',').itertuples()

# 직선 방정식의 계수
m = 1.93939
b = 4.73333

sum_of_squares = 0.0

# 잔차를 계산합니다.
for p in points:
    y_actual = p.y
    y_predict = m * p.x + b
    residual_squared = (y_predict - y_actual) ** 2
    sum_of_squares += residual_squared

print("제곱 합 = {}".format(sum_of_squares))
