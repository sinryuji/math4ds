from scipy.stats import norm

# 감기의 회복 기간은 평균 18일이고 표준 편차는 1.5일입니다.
mean = 18
std_dev = 1.5

# 15일에서 21일 사이에 회복될 확률은 95%입니다.
x = norm.cdf(21, mean, std_dev) - norm.cdf(15, mean, std_dev)

print(x) # 0.9544997361036416
