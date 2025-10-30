from scipy.stats import beta

p7 = beta.cdf(0.7, 15, 4)
p8 = beta.cdf(0.8, 15, 4)

print(p8 - p7)
