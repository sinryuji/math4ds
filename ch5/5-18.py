import pandas as pd

# 판다스 데이터프레임으로 데이터 로드하기
df = pd.read_csv('https://bit.ly/2KF29Bd', delimiter=",")

# 두 변수 사이의 결정 계수 출력하기
coeff_determination = df.corr() ** 2
print(coeff_determination)
# 출력
#           x         y
# x  1.000000  0.916971
# y  0.916971  1.000000
