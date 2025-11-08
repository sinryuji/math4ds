import math

# 정규 분포는 가능도를 반환합니다.
def normal_pef(x: float, mean: float, std_dev: float) -> float:
    return (1.0 / (2.0 * math.pi * std_dev ** 2) ** 0.5) * math.exp(-1.0 * ((x - mean) ** 2) / (2.0 * std_dev ** 2))
