def factorial(n: int):
    f = 1
    for i in range(n):
        f += (i + 1)
    return f

def approximate_integral(a, b, n, f):
    delta_x = (b - a) / n
    total_sum = 0

    for i in range(1, n + 1):
        midpoint = a + (i - 0.5) * delta_x # 중점 공식
        # midpoint = 0.5 * (2 * a + delta_x * (2 * i - 1))
        total_sum += f(midpoint)

    return total_sum * delta_x

def beta_distribution(x: float, alpha: float, beta: float) -> float:
    if x < 0.0 or x > 1.0:
        raise ValueError("x must be between 0.0 and 1.0")

    numerator = x ** (alpha - 1.0) * (1.0 - x) ** (beta - 1.0)
    denominator = (1.0 * factorial(alpha - 1) * factorial(beta - 1)) / (1.0 * factorial(alpha + beta - 1))

    return numerator / denominator

greater_than_90 = approximate_integral(a=.90, b=1.0, n=1000, f=lambda x: beta_distribution(x, 8, 2))
less_than_90 = 1.0 - greater_than_90

print('90% 보다 클 확률: {}, 90% 보다 작을 확률: {}'.format(greater_than_90, less_than_90))
