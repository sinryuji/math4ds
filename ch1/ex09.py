from math import exp

p = 1000
r = 0.05
t = 3
n = 12

a = p * (1 + r / n) ** (t * n)

print(a)
