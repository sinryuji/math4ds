import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import beta

# 파라미터
a, b = 9, 3  # 성공 8, 실패 2, uniform prior(1,1) 반영

# x축: 성공 확률 p (0~1)
p = np.linspace(0, 1, 1000)
y = beta.pdf(p, a, b)

plt.plot(p, y)
plt.title("Beta(9, 3) Distribution (8 successes, 2 failures)")
plt.xlabel("Success Probability (p)")
plt.ylabel("Density")
plt.show()
