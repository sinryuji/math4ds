import pandas as pd

df = pd.read_csv('https://bit.ly/3C8JzrM', delimiter=',')

correlations = df.corr(method='pearson')
print(correlations)

from scipy.stats import t
from math import sqrt

# 표본 크기
n = df.shape[0]
print(n)
lower_cv = t(n-1).ppf(.025)
upper_cv = t(n-1).ppf(.975)

r = correlations['y']['x']

# 상관 계수 추출
test_value = r / sqrt((1 - r ** 2) / (n - 2))

print("검정값: {}".format(test_value))
print("임계 범위: {}, {}".format(lower_cv, upper_cv))


if test_value < lower_cv or test_value > upper_cv:
    print("상관 관계가 입증되어 귀무 가설을 거부합니다")
else:
    print("상관 관계가 입증되지 않아 귀무 가설을 거부하지 못합니다")

# p 값 계산
if test_value > 0:
    p_value = 1.0 - t(n-1).cdf(test_value)
else:
    p_value = t(n-1).cdf(test_value)

# 양측 검정이므로 2를 곱합니다
p_value = p_value * 2
print("P 값: {}".format(p_value))
