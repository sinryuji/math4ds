from scipy.stats import t

# 표본 크기가 25일 때
# 95% 신뢰도에 대해 임곗값 범위 구하기

n = 25
lower = t.ppf(0.025, df=n-1)
upper = t.ppf(0.975, df=n-1)

print(lower, upper)
# -2.063898561628021 2.063898561628021
