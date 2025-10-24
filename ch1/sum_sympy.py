from sympy import *

i,n = symbols('i n')

# 1부터 n까지 i를 반복하면서
# 2를 곱하고 더합니다
summation = Sum(2 * i,(i, 1, n))

# n을 5로 지정하면
# 숫자 1에서 5까지 반복합니다
up_to_5 = summation.subs(n, 5)
print(up_to_5.doit())
