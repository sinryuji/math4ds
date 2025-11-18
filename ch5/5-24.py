import pandas as pd
from sklearn.linear_model import LinearRegression

# 데이터를 로드합니다.
df = pd.read_csv('https://bit.ly/2X1HWH7', delimiter=",")

# (마지막 열을 제외한 모든 열을) 입력 변수로 추출합니다.
X = df.values[:, :-1]

# 마지막 열을 출력으로 추출합니다.
Y = df.values[:, -1]

# 모델을 훈련합니다.
fit = LinearRegression().fit(X, Y)

# 파라미터를 출력합니다.
print("계수 = {0}".format(fit.coef_))
print("절편 = {0}".format(fit.intercept_))
print("z = {0} + {1}x + {2}y".format(fit.intercept_, fit.coef_[0], fit.coef_[1]))
# 출력
# 계수 = [2.00672647 3.00203798]
# 절편 = 20.10943282003595
# z = 20.10943282003595 + 2.006726472512807x + 3.0020379766466934y
