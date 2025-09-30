# from 절 단점
from math import sqrt

math_result = sqrt(16)  # 실수형 4.0


def sqrt(x):  # 사용자가 정의한 sqrt 함수
    return str(x**0.5)


my_result = sqrt(16)  # 문자열 4.0

print(type(math_result), type(my_result))  # <class 'float'> <class 'str'>


# from 절 사용 주의 사항
## 같은 이름인 경우 덮어쓰기 주의
from math import sqrt  # math.sqrt가 먼저 import됨
from my_math import sqrt  # my_math.sqrt가 math.sqrt를 덮어씀

result = sqrt(9)  # math.sqrt가 아닌 my_math.sqrt가 사용됨


# from 절 사용 주의 사항
## 모든 요소를 한 번에 import 하는 * 은 권장하지 않음
from math import *
from my_math import sqrt, tangent  # 어느 함수가 math 모듈과 중복되는지 모름

# 아래는 사용자가 임의로 정의한 변수들
a = 100
c = 200
e = 300  # math 모듈의 자연상수 e를 사용할 수 없게 됨
