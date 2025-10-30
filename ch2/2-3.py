from scipy.stats import beta

a = 8
b = 2

p = beta.cdf(0.90, a, b)

print(p) # 0.7748409780000002
