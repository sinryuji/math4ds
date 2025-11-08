from scipy.stats import norm

# 감기의 회복 기간은 평균 18일이고 표준 편차는 1.5일입니다.
mean = 18
std_dev = 1.5

# 누적 면적 5%에 해당하는 x 값은 얼마인가요?
x = norm.ppf(0.05, mean, std_dev)

print(x) # 15.53271955957279
