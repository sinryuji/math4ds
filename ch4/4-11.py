from numpy import array

# 변환 1
i_hat1 = array([0, 1])
j_hat1 = array([-1, 0])
transform1 = array([i_hat1, j_hat1]).transpose()

# 변환 2
i_hat2 = array([1, 0])
j_hat2 = array([1, 1])
transform2 = array([i_hat2, j_hat2]).transpose()

# 변환 통합
combined = transform2 @ transform1

print("COMBINED MATRIX:\n {}".format(combined))

v = array([1, 2])
print(combined.dot(v)) # [-1 1]

rotated = transform1.dot(v)
sheared = transform2.dot(rotated)
print(sheared) # [-1 1]
