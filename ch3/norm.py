import plotly.graph_objects as go
import numpy as np
from scipy.stats import norm

# 예시 데이터 (평균 0, 표준편차 1)
x = np.linspace(-4, 4, 200)
y = norm.pdf(x, 0, 1)

fig = go.Figure()
fig.add_trace(go.Scatter(x=x, y=y, mode='lines'))
fig.show()
