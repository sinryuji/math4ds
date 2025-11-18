import pandas as pd

# 데이터를 판다스 데이터프레임으로 로드하기
df = pd.read_csv('https://bit.ly/2KF29Bd', delimiter=",")

print(df)

# 변수 간의 상관계수 출력하기
correlations = df.corr()
print(correlations)
# 출력:
#           x         y
# x  1.000000  0.957586
# y  0.957586  1.000000
