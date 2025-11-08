from scipy.stats import norm

# 감기의 회복 기간은 평균 18일이고 표준 편차는 1.5일입니다.
mean = 18
std_dev = 1.5

# 16 이하일 확률
p1 = norm.cdf(16, mean, std_dev)

# 20 이상일 확률
p2 = 1.0 - norm.cdf(20, mean, std_dev)

p_value = p1 + p2

print(p_value) # 0.18242243945173575
