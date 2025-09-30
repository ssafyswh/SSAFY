# 절차 지향 사고
# 예: 변수와 함수를 별개로 다룸
name = 'Alice'
age = 25


def introduce(name, age):
    print(f'안녕하세요, {name}입니다. 나이는 {age}살입니다.')


introduce(name, age)


# 객체 지향 사고
# 예: 사람(객체) 안에 name, age와 이와 관련된 기능(메서드) 포함
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        print(f'안녕하세요, {self.name}입니다. 나이는 {self.age}살입니다.')


alice = Person('Alice', 25)
alice.introduce()  # 객체가 자신의 정보를 출력
