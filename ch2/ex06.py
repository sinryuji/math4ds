from scipy.stats import beta

p = 1.0 - beta.cdf(0.5, 15, 4) # 19번 던졌는데 앞면 15, 뒷면 4번 나올 확률이 50% 보다 클 확률

print(p)
