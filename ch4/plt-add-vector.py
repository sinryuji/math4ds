import numpy as np
import matplotlib.pyplot as plt

v = np.array([3, 2])
w = np.array([2, -1])
vw = v + w  # [5, 1]

plt.figure(figsize=(6,6))

# 원점
origin = np.array([0, 0])

# v 벡터
plt.quiver(*origin, *v, angles='xy', scale_units='xy', scale=1, color='blue', label='v (3,2)')

# v의 끝점에서 w 벡터
plt.quiver(*v, *w, angles='xy', scale_units='xy', scale=1, color='green', label='w (2,-1)')

# 결과 벡터 v + w
plt.quiver(*origin, *vw, angles='xy', scale_units='xy', scale=1, color='red', label='v + w (5,1)')

# 좌표축 범위 설정
xmin = min(0, v[0], vw[0], w[0]) - 1
xmax = max(v[0], vw[0], w[0]) + 1
ymin = min(0, v[1], vw[1], w[1]) - 1
ymax = max(v[1], vw[1], w[1]) + 1
plt.xlim(xmin, xmax)
plt.ylim(ymin, ymax)

# 눈금 1 단위
plt.xticks(range(int(xmin), int(xmax)+1))
plt.yticks(range(int(ymin), int(ymax)+1))

# 축 표시 및 정비율 유지
plt.axhline(0, color='black', linewidth=1)
plt.axvline(0, color='black', linewidth=1)
plt.gca().set_aspect('equal', adjustable='box')
plt.grid(True)

plt.show()
