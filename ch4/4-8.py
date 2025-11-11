from numpy import array

# i-hat과 j-hat을 선언합니다.
i_hat = array([2, 0])
j_hat = array([0, 3])

# i-hat과 j-hat을 사용해 기저 행렬을 만들고 열과 행을 바꿔야 합니다.
basis = array([i_hat, j_hat]).transpose()

# 벡터 v를 선언합니다.
v = array([1, 1])

# 점 곱으로 v에 변환을 적용해 새로운 벡터를 만듭니다.
new_v = basis.dot(v)

print(new_v)
