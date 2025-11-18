import pandas as pd
import numpy as np

# 데이터를 로드합니다
data = pd.read_csv('https://bit.ly/2KF29Bd', header=0)

X = data.iloc[:, 0].values
Y = data.iloc[:, 1].values

n = data.shape[0]  # rows

# 계수를 초기화합니다
m = 0.0
b = 0.0

sample_size = 1  # 샘플 크기
L = .0001  # 학습률
epochs = 1_000_000  # 경사 하강법을 수행할 반복 횟수

# 확률적 경사 하강법을 수행합니다
for i in range(epochs):
    idx = np.random.choice(n, sample_size, replace=False)
    x_sample = X[idx]
    y_sample = Y[idx]

    # 예측한 Y 값
    Y_pred = m * x_sample + b

    # m에 대한 그레이디언트
    D_m = (-2 / sample_size) * sum(x_sample * (y_sample - Y_pred))

    # b에 대한 그레이디언트
    D_b = (-2 / sample_size) * sum(y_sample - Y_pred)
    m = m - L * D_m  # Update m
    b = b - L * D_b  # Update b

    # 진행 과정 출력
    if i % 10000 == 0:
        print(i, m, b)

print("y = {0}x + {1}".format(m, b)) # y = 1.941193689277049x + 4.753357775711016
