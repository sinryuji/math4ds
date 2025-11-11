import matplotlib.pyplot as plt

v = [3, 2]
w = [2, -1]

plt.figure(figsize=(6,6))

# 벡터 v
plt.quiver(0, 0, v[0], v[1], angles='xy', scale_units='xy', scale=1, label='v')

# 벡터 w
plt.quiver(0, 0, w[0], w[1], angles='xy', scale_units='xy', scale=1, color='red', label='w')

# 좌표축 범위
xmin = min(0, v[0], w[0]) - 1
xmax = max(v[0], w[0]) + 1
ymin = min(0, v[1], w[1]) - 1
ymax = max(v[1], w[1]) + 1
plt.xlim(xmin, xmax)
plt.ylim(ymin, ymax)

# 눈금을 1 단위로
plt.xticks(range(int(xmin), int(xmax)+1))
plt.yticks(range(int(ymin), int(ymax)+1))

# 축 표시
plt.axhline(0, color='black', linewidth=1)
plt.axvline(0, color='black', linewidth=1)

plt.gca().set_aspect('equal', adjustable='box')
plt.grid(True)
plt.show()
