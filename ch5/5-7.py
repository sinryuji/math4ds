import pandas as pd
from numpy.linalg import qr, inv
import numpy as np

# 데이터를 로드합니다
df = pd.read_csv('https://bit.ly/3goOAnt', delimiter=",")

# 입력 변수를 추출합니다(마지막 열은 제외)
X = df.values[:, :-1].flatten()

# 절편(intercept)을 위해 "1"로 채워진 열을 추가합니다
X_1 = np.vstack([X, np.ones(len(X))]).transpose()

# 출력 값(마지막 열)을 추출합니다
Y = df.values[:, -1]

# QR 분해를 사용해 기울기와 절편 계수를 계산합니다
Q, R = qr(X_1)
b = inv(R).dot(Q.transpose()).dot(Y)

print(b)
