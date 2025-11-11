from numpy import array

# i-hat과 j-hat으로 구성된 기저 행렬을 만듭니다.
basis = array(
    [[3, 0],
    [0, 2]]
)

# 벡터 v를 정의합니다.
v = array([1, 1])

# 점 곱으로 v에 변환을 적용해 새로운 벡터를 만듭니다.
new_v = basis.dot(v)

print(new_v)
