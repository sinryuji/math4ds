import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# 데이터를 로드합니다.
df = pd.read_csv('https://bit.ly/3goOAnt', delimiter=',')

# 입력 변수를 추출합니다(마지막 열은 제외)
X = df.values[:, :-1]

# 출력값(마지막 열)을 추출합니다.
Y = df.values[:, -1]

# 이 데이터로 선형 회귀를 훈련합니다.
fit = LinearRegression().fit(X, Y)

# m = 1.7867224, b = -16.51923513
m = fit.coef_.flatten()
b = fit.intercept_.flatten()
print("m = {0}".format(m))
print("b = {0}".format(b))

# 그래프를 그립니다.
plt.plot(X, Y, 'o') # 산점도
plt.plot(X, m * X + b) # 직선
plt.show()
