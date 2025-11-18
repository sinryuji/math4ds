import random

def f(x):
    return (x - 3) ** 2 + 4

def dx_f(x):
    return 2 * (x - 3)

# 학습률
L = 0.001

# 경사 하강법을 수행할 반복 횟수
iterations = 100_000

# 무작위한 x에서 시작합니다.
x = random.randint(-15, 15)

for i in range(iterations):
    # 경사를 구합니다.
    d_x = dx_f(x)

    # (learning rate) * (slope)를 빼서 x를 업데이트합니다.
    x -= L * d_x

print(x, f(x)) # 2.999999999999889 4.0
