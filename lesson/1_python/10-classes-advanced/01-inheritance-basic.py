# 부모 클래스
class Animal:
    def eat(self):
        print('먹는 중')


class Dog(Animal):
    def bark(self):
        print('멍멍')


my_dog = Dog()
my_dog.bark()

# 부모 클래스의 인스턴스 메서드 eat을 호출
my_dog.eat()
