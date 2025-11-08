from scipy.stats import norm

mean = 42
std_dev = 8

x = norm.ppf(0.1, mean, std_dev)

print(x)
