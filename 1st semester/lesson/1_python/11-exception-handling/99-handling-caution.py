# 아래와 같이 예외를 작성하면 코드는 2번째 except 절에 이후로 도달하지 못함
# ZeroDivisionError 클래스는 Exception 클래스의 하위 클래스 중 하나이므로 ZeroDivisionError를 먼저 작성해야 함
# https://docs.python.org/ko/3/library/exceptions.html#exception-hierarchy
try:
    num = int(input('100으로 나눌 값을 입력하시오 : '))
    print(100 / num)
except Exception:
    print('숫자를 넣어주세요.')
# ZeroDivisionError는 Exception의 하위 클래스이므로 Exception보다 먼저 작성해야 함
except ZeroDivisionError:
    print('0으로 나눌 수 없습니다.')
except:
    print('에러가 발생하였습니다.')


# 옳은 코드
# 가장 구체적인 예외부터 처리하고, 마지막에 범용 예외를 처리하도록 순서를 배치
try:
    num = int(input('100으로 나눌 값을 입력하시오 : '))
    print(100 / num)
# 1) 구체적인 예외부터
except ZeroDivisionError:
    print('0으로 나눌 수 없습니다.')
except ValueError:
    print('숫자를 넣어주세요.')
# 2) 마지막에 광범위한 예외(Exception)
except Exception:
    print('에러가 발생하였습니다.')
