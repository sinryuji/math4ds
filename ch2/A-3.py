def factorial(n: int):
    f = 1
    for i in range(n):
        f += (i + 1)
    return f

# 이항 분포에 필요한 계수를 생성합니다.
def binomial_coefficient(n: int, k: int):
    return factorial(n) / (factorial(k) * factorial(n - k))

# 이항 분포는 k가 발생할 확률 p가 주어졌을 때 n번의 시도 중 k번의 사건이 발생할 확률을 계산합니다.
def binomial_distribution(k: int, n: int, p: float):
    return binomial_coefficient(n, k) * (p ** k) * (1.0 - p) ** (n - k)

# 각 성공 확률이 90%인 10번의 시도
n = 10
p = 0.9

for k in range(n + 1):
    probability = binomial_distribution(k, n, p)
    print('{0} - {1}'.format(k, probability))

# 0 - 9.999999999999978e-11
# 1 - 5.478260869565207e-10
# 2 - 3.0648648648648595e-09
# 3 - 2.011034482758618e-08
# 4 - 1.5182479338842955e-07
# 5 - 1.2916968749999988e-06
# 6 - 1.22978082644628e-05
# 7 - 0.00013194397241379305
# 8 - 0.0016287948486486483
# 9 - 0.023582116721739134
# 10 - 0.3486784401000001
