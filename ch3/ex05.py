from math import sqrt
from scipy.stats import norm

def critical_z_value(p):
    norm_dist = norm(loc=0.0, scale=1.0)
    left_tail_area = (1.0 - p) / 2.0
    right_tail_area = 1.0 - ((1.0 - p) / 2.0)

    return norm_dist.ppf(left_tail_area), norm_dist.ppf(right_tail_area)

def confidence_interval(p, sample_mean, std_dev, n):
    lower, upper = critical_z_value(p)
    lower_ci = lower * (std_dev / sqrt(n))
    upper_ci = upper * (std_dev / sqrt(n))

    return sample_mean + lower_ci, sample_mean + upper_ci

sample_mean = 1.715588
std_dev = 0.029252

print(confidence_interval(0.99, sample_mean, std_dev, 34))
