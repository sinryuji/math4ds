from scipy.stats import norm

mean = 10345
std_dev = 552

p2 = p1 = 1.0 - norm.cdf(11641, mean, std_dev)
p_value = p1 + p2

print("양측 검정의 p 값: ", p_value)
if p_value <= 0.05:
    print("양측 검정 통과")
else:
    print("양측 검정 실패")
