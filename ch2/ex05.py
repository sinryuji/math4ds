from scipy.stats import binom

n = 137
p = 0.40

answer = 0

for x in range(50, 137 + 1):
    answer += binom.pmf(x, n, p)

print(answer)
