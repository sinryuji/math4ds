from math import sqrt

sample = [1.78, 1.75, 1.72, 1.74, 1.77]

def mean(values):
    return sum(values) / len(values)

def variance(values):
    m = mean(values)
    return sum((v - m) ** 2 for v in values) / len(values)

def std_dev(values):
    return sqrt(variance(values))

print('mean: ', mean(sample))
print('standard deviation: ', std_dev(sample))
