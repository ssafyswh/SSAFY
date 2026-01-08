# while문 기본
a = 0

while a < 3:
    print(a)
    a += 1


# while문 작동 원리
# input_value = ''
# while input_value != 'exit':  # exit 를 입력하면 반복 종료
#     input_value = input("Enter a value: ")
#     print(input_value)


# while문 사용자 입력에 따른 반복
number = int(input('양의 정수를 입력해주세요.: '))

while number <= 0:
    if number < 0:
        print('음수를 입력했습니다.')
    else:
        print('0은 양의 정수가 아닙니다.')

    number = int(input('양의 정수를 입력해주세요.: '))

print('잘했습니다!')
