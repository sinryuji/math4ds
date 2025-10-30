from scipy.stats import beta

p = 1.0 - beta.cdf(0.5, 15, 4)

print(p)
