from scipy.stats import norm

mean = 64.43
std_dev = 2.99

x = 1 - norm.cdf(70, mean, std_dev)

print(x)
