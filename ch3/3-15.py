# 균등 분포에서 뽑은 표본의 평균은 정규 분포가 됩니다.
import random
import plotly.express as px

sample_size = 1
sample_count = 1000

# 중심 극한 정리, 크기가 31인 1000개의 표본
# 0.0과 1.0 사이의 난수
x_values = [(sum([random.uniform(0.0, 1.0) for i in range(sample_size)]) / sample_size) for _ in range(sample_count)]
y_values = [1 for _ in range(sample_count)]

px.histogram(x=x_values, y=y_values, nbins=20).show()
