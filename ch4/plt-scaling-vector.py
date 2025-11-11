import numpy as np
import matplotlib.pyplot as plt

v = np.array([3, 1])
v2 = 2 * v   # [6, 2]
print(v2[0])

plt.figure(figsize=(6,6))

# 원래 벡터 v
plt.quiver(0, 0, v[0], v[1],
           angles='xy', scale_units='xy', scale=1,
           color='blue')

# 스케일된 벡터 2v
plt.quiver(0, 0, v2[0], v2[1],
           angles='xy', scale_units='xy', scale=1,
           color='red')

# 축 범위
xmin = min(0, v2[0]) - 1
xmax = max(0, v2[0]) + 1
ymin = min(0, v2[1]) - 1
ymax = max(0, v2[1]) + 1
plt.xlim(xmin, xmax)
plt.ylim(ymin, ymax)

# 눈금 1 단위
plt.xticks(range(int(xmin), int(xmax)+1))
plt.yticks(range(int(ymin), int(ymax)+1))

# 좌표축/격자/비율
plt.axhline(0, color='black', linewidth=1)
plt.axvline(0, color='black', linewidth=1)
plt.gca().set_aspect('equal', adjustable='box')
plt.grid(True)

plt.show()
