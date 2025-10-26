from sympy import *

# "x"와 스텝 크기 "s" 정의
x, s = symbols('x s')

# 함수 정의
f = x**2

# 간격 "s"만큼 떨어진 두 점을 기울기 공식에 대입합니다
slope_f = (f.subs(x, x + s) - f) / ((x+s) - x)

# 스텝 크기 s가 0에 무한히 가까워질 때 도함수를 계산합니다
result = limit(slope_f, s, 0)

print(result) # 2*x
