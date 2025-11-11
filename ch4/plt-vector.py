import matplotlib.pyplot as plt

# 벡터
v = [3, 2]

plt.figure(figsize=(5,5))

# quiver(x시작, y시작, x방향, y방향)
plt.quiver(0, 0, v[0], v[1], angles='xy', scale_units='xy', scale=1)

# 좌표축 설정
plt.xlim(0, v[0] + 1)
plt.ylim(0, v[1] + 1)
plt.axhline(0, color='black', linewidth=1)
plt.axvline(0, color='black', linewidth=1)

# 눈금을 1 단위로 설정
plt.xticks(range(0, v[0] + 2, 1))
plt.yticks(range(0, v[1] + 2, 1))

plt.gca().set_aspect('equal', adjustable='box')
plt.grid(True)
plt.show()
