## as 키워드 사용 1
from math import sqrt
from my_math import sqrt as my_sqrt

print(sqrt(4))  # 2.0
print(my_sqrt(4))  # 2.0


## as 키워드 사용 2
## (참고) pandas와 matplotlib 패키지 설치해야 정상 동작
import pandas as pd
import matplotlib.pyplot as plt

# 별칭을 부여하지 않으면 길고 불편함
df = pandas.DataFrame()
matplotlib.pyplot.plot(x, y)

# 별칭을 사용하면 짧고 편리
df = pd.DataFrame()
plt.plot(x, y)
