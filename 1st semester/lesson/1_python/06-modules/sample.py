## 사용자 정의 모듈
import my_math

# from my_math import add

print(my_math.add(1, 2))
# print(add(1, 2))


## 사용자 정의 패키지
from my_package.math import my_math
from my_package.statistics import tools


print(my_math.add(1, 2))
print(tools.mod(1, 2))
