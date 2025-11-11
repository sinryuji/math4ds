import numpy as np
import matplotlib.pyplot as plt

# 두 벡터
v1 = np.array([1, 0])
v2 = np.array([1, 1])

# 평행사변형 꼭짓점
origin = np.array([0, 0])
p1 = v1
p2 = v2
p3 = v1 + v2

# 행렬식 = 평행사변형 면적
matrix = np.column_stack((v1, v2))
area = abs(np.linalg.det(matrix))
print("면적(행렬식 절대값):", area)

plt.figure(figsize=(6,6))

# 벡터 그리기: quiver 사용
plt.quiver(*origin, *v1, angles='xy', scale_units='xy', scale=1)
plt.quiver(*origin, *v2, angles='xy', scale_units='xy', scale=1)

# 평행사변형 채우기
polygon = np.array([origin, p1, p3, p2])
plt.fill(polygon[:,0], polygon[:,1], alpha=0.3)

# 축 범위
xmin = min(0, v2[0]) - 1
xmax = max(0, v2[0]) + 4
ymin = min(0, v2[1]) - 1
ymax = max(0, v2[1]) + 4
plt.xlim(xmin, xmax)
plt.ylim(ymin, ymax)

# 눈금 1 단위
plt.xticks(range(int(xmin), int(xmax)+1))
plt.yticks(range(int(ymin), int(ymax)+1))

# 보조 설정
plt.axhline(0, color='black', linewidth=1)
plt.axvline(0, color='black', linewidth=1)
plt.gca().set_aspect('equal', adjustable='box')
plt.grid(True)
plt.show()
