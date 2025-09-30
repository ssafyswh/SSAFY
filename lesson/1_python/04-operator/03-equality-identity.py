# == 연산자
print(2 == 2.0)  # True
print(2 != 2)  # False
print('HI' == 'hi')  # False
print(1 == True)  # True

# is 연산자
# SyntaxWarning: "is" with a literal. Did you mean "=="?
print(1 is True)  # False
print(2 is 2.0)  # False

# 왜 is 대신 ==를 사용해야 하나?
# 1(정수)과 True(불리언)는 다른 객체이다.
print(1 is True)  # False
# 1과 True의 '값'은 논리적으로 같다.
print(1 == True)  # True

# 2(정수)와 2.0(실수)은 다른 객체이다.
print(2 is 2.0)  # False
# 2와 2.0의 '값'은 논리적으로 같다.
print(2 == 2.0)  # True

# is 연산자는 언제 사용하는가?
# 싱글턴 객체 비교할 때
x = None
# 권장
if x is None:
    print('x는 None입니다.')
# 비권장
if x == None:
    print('x는 None입니다.')


x = True
y = True
print(x is y)  # True
print(True is True)  # True
print(False is False)  # True
print(None is None)  # True


# 리스트나 객체 비교 시 주의사항
a = [1, 2, 3]
b = [1, 2, 3]
print(a == b) # True (두 리스트의 값은 동일)
print(a is b) # False (서로 다른 리스트 객체)

# b가 a를 그대로 참조하도록 할 경우
b = a
print(a is b) # True (같은 객체를 가리키므로 True)
