import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import cross_val_score, ShuffleSplit

df = pd.read_csv('https://bit.ly/38XwbeB', delimiter=",")

# (마지막 열을 제외한 모든 열을) 입력 변수로 추출합니다.
X = df.values[:, :-1]

# 마지막 열을 출력으로 추출합니다.
Y = df.values[:, -1]

# 단순 선형 회귀를 수행합니다.
kfold = ShuffleSplit(n_splits=10, test_size=.33, random_state=7)
model = LinearRegression()
results = cross_val_score(model, X, Y, cv=kfold)

print(results)
print("평균=%.3f (표준편차-%.3f)" % (results.mean(), results.std()))
# 출처
# [0.82514286 0.23552344 0.92653455 0.91620594 0.73260142 0.8698865
#  0.55254014 0.89593526 0.91570078 0.82086621]
# 평균=0.769 (표준편차-0.208)
