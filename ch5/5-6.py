import pandas as pd
from numpy.linalg import inv
import numpy as np

# 데이터를 로드합니다
df = pd.read_csv('https://bit.ly/3goOAnt', delimiter=",")

# 입력 변수를 추출합니다(마지막 열은 제외)
X = df.values[:, :-1].flatten()

# 절편(intercept)을 위해 "1"로 채워진 열을 추가합니다
X_1 = np.vstack([X, np.ones(len(X))]).T

# 출력 값(마지막 열)을 추출합니다
Y = df.values[:, -1]

# 기울기와 절편 계수를 계산합니다
beta = inv(X_1.transpose() @ X_1) @ (X_1.transpose() @ Y)
print(beta) # [1.93939394, 4.73333333]

# y 값을 예측합니다
y_predict = X_1.dot(beta)
