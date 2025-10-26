from sympy import *

x, y = symbols('x y')


# 첫 번째 함수의 도함수
# 충돌을 피하기 위해 _y로 씁니다
_y = x**2 + 1
dy_dx = diff(_y)

# 두 번째 도함수
z = y**3 - 2
dz_dy = diff(z)

# 연쇄 법칙을 사용한 경우와
# 대체 방식을 사용한 경우 도함수 계산
dz_dx_chain = (dy_dx * dz_dy).subs(y, _y)
dz_dx_no_chain = diff(z.subs(y, _y))

# 두 값이 같다는 것을 보임으로써 연쇄 법칙을 증명합니다
print(dz_dx_chain) # 6*x*(x**2 + 1)**2
print(dz_dx_no_chain) # 6*x*(x**2 + 1)**2
