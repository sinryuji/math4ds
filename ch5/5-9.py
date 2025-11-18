import pandas as pd

# CSV에서 데이터를 로드합니다
points = list(pd.read_csv("https://bit.ly/2KF29Bd").itertuples())

# 계수를 초기화합니다
m = 0.0
b = 0.0

# 학습률
L = .001

# 반복 횟수
iterations = 100_000

n = float(len(points))  # X에 있는 원소 개수

# 경사 하강법 수행
for i in range(iterations):

    # m에 대한 그레이디언트
    D_m = sum(2 * p.x * ((m * p.x + b) - p.y) for p in points)

    # b에 대한 그레이디언트
    D_b = sum(2 * ((m * p.x + b) - p.y) for p in points)

    # m과 b를 업데이트합니다
    m -= L * D_m
    b -= L * D_b

print("y = {0}x + {1}".format(m, b)) # y = 1.9393939393939548x + 4.733333333333227
