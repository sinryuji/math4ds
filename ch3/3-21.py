from scipy.stats import norm

# 감기의 회복 기간은 평균 18일이고 표준 편차는 1.5일입니다.
mean = 18
std_dev = 1.5

# 누적 면적 2.5%에 해당하는 x 값을 얼마인가요?
x1 = norm.ppf(0.025, mean, std_dev)

# 누적 면적 97.5%에 해당하는 x 값을 얼마인가요?
x2 = norm.ppf(0.975, mean, std_dev)

print(x1) # 15.060054023189918
print(x2) # 20.93994597681008
