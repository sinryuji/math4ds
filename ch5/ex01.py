import pandas as pd
from sklearn.linear_model import LinearRegression

df = pd.read_csv('https://bit.ly/3C8JzrM', delimiter=',')

X = df.values[:, :-1]
y = df.values[:, -1]

linear = LinearRegression()
his = linear.fit(X, y)

m = his.coef_
b = his.intercept_

print('m: ', m)
print('b: ', b)
