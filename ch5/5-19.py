import pandas as pd
from math import sqrt

# 데이터를 로드합니다.
points = list(pd.read_csv('https://bit.ly/2KF29Bd', delimiter=",").itertuples())

n = len(points)

# 모델 파라미터를 초기화합니다.
m = 1.939
b = 4.733

# 추정 표준 오차를 계산합니다.
S_e = sqrt((sum((p.y - (m*p.x +b))**2 for p in points))/(n-2))

print(S_e) # 1.87406793500129
