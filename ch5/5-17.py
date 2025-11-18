from scipy.stats import t
from math import sqrt

# 샘플 크기
n = 10

lower_cv = t(n-1).ppf(.025)
upper_cv = t(n-1).ppf(.975)

# 데이터(https://bit.ly/2KF29Bd)에서 계산한 결정 계수
r = 0.957586

# 검정 수행
test_value = r / sqrt((1-r**2) / (n-2))

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
# 출력
# 검정값: 9.399564671312076
# 임계 범위: -2.262157162740992, 2.262157162740991
# 상관 관계가 입증되어 귀무 가설을 거부합니다
# P 값: 5.9763860877914965e-06
