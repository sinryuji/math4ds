from sympy import *

# 심파이에 변수를 선언합니다
x, i, n = symbols('x i n')

# 함수와 범위를 선언합니다
f = x**2 + 1
lower, upper = 0, 1

# 상자의 너비와 "i" 위치에 있는 직사각형의 높이를 계산합니다
delta_x = ((upper - lower) / n)
x_i = (lower + delta_x * i)
fx_i = f.subs(x, x_i)

# "n" 개의 직사각형을 순환하면서 면적을 더합니다
n_rectangles = Sum(delta_x * fx_i, (i, 1, n)).doit()

# 직사각형의 개수 "n"을 무한대로 늘려 면적을 계산합니다
area = limit(n_rectangles, n, oo)

print(area)
