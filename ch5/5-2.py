import pandas as pd

# 데이터 로드하기
points = pd.read_csv('https://bit.ly/3goOAnt', delimiter=',').itertuples()

# 직선 방정식의 계수
m = 1.93939
b = 4.73333

# 잔차를 계산합니다.
for p in points:
    y_actual = p.y
    y_predict = m * p.x + b
    residual = y_actual - y_predict
    print(residual)
