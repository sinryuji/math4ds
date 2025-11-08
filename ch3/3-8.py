from math import sqrt

data = [0, 1, 5, 7, 9, 10, 14]

def variance(values, is_sample: bool = False):
    mean = sum(values) / len(values)
    _variance = sum((v - mean) ** 2 for v in values) / (len(values) - (1 if is_sample else 0))

    return _variance

def std_dev(values, is_sample: bool = False):
    return sqrt(variance(values, is_sample))

print("분산 = {}".format(variance(data, is_sample=True))) # 24.95238095238095
print("표준 편차 = {}".format(std_dev(data, is_sample=True))) # 4.99523582550223
