sample = [90, 80, 63, 87]
weights = [1.0, 1.0, 1.0, 2.0]

weighted_mean = sum(s * w for s, w in zip(sample, weights)) / sum(weights)

print(weighted_mean) # 81.4
