from scipy.stats import norm

# 감기의 회복 기간은 평균 18일이고 표준 편차는 1.5일입니다.
mean = 18
std_dev = 1.5

# 16보다 작거나 같은 확률
p_value = norm.cdf(16, mean, std_dev)

print(p_value) # 0.09121121972586788
