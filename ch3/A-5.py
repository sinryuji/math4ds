import math

def normal_pdf(x: float, mean: float, std_dev: float) -> float:
    return (1.0 / (2.0 * math.pi * std_dev ** 2) ** 0.5) * math.exp(-1.0 * ((x - mean) ** 2 / (2.0 * std_dev ** 2)))

def approximate_integral(a, b, n, f):
    delta_x = (b - a) / n
    total_sum = 0

    for i in range(1, n + 1):
        midpoint = a + (i - 0.5) * delta_x
        total_sum += f(midpoint)

    return total_sum * delta_x

p_between_61_and_62 = approximate_integral(61, 62, 7, lambda x: normal_pdf(x, 64.43, 2.99))

print(p_between_61_and_62) # 0.0825344984983386
