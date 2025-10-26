from sympy import *

# 심파이에 'x'를 선언합니다
x = symbols('x')

# 파이썬 표현식을 사용해 함수를 정의합니다
f = x**2 + 1

# x=0과 1 사이의 면적을 구하기 위해
# x에 대해서 함수의 적분을 계산합니다
area = integrate(f, (x, 0, 1))

print(area)
