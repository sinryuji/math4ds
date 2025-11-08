sample = [90, 80, 63, 87]
weights = [0.20, 0.20, 0.20, 0.40]

weighted_mean = sum(s * w for s, w in zip(sample, weights)) / sum(weights)

print(weighted_mean) # 81.4
