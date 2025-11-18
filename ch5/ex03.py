import pandas as pd
from scipy.stats import t
from math import sqrt

# 데이터를 로드합니다.
points = list(pd.read_csv('https://bit.ly/3C8JzrM', delimiter=",").itertuples())

n = len(points)

# 모델 파라미터를 초기화합니다.
m = 1.75919315
b = 4.69359655

# x = 50에 대한 예측 구간을 계산합니다.
x_0 = 50
x_mean = sum(p.x for p in points) / len(points)

t_value = t(n - 2).ppf(.975)

standard_error = sqrt(sum((p.y - (m * p.x + b)) ** 2 for p in points) / (n - 2))

margin_of_error = t_value * standard_error * \
                  sqrt(1 + (1 / n) + (n * (x_0 - x_mean) ** 2) / \
                       (n * sum(p.x ** 2 for p in points) - \
                            sum(p.x for p in points) ** 2))

predicted_y = m*x_0 + b

print(predicted_y - margin_of_error, predicted_y + margin_of_error)
