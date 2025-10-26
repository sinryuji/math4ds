from sympy import *

x = symbols('x')
f = 3 * x ** 2 + 1

ans = integrate(f, (x, 0, 2))
print(ans)
