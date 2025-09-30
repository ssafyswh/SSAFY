class Animal:
    def eat(self):
        print('Animal이 먹는 중')


class Dog(Animal):
    # 오버라이딩 (부모 클래스 Animal의 eat 메서드를 재정의)
    def eat(self, food):
        print(f'Dog가 {food}를 먹는중')

my_dog = Dog()
my_dog.eat('간식')

# 오버로딩 (파이썬 미지원)
# class Example:
#     def do_something(self, x):
#         print('첫 번째 do_something 메서드:', x)

#     # 파이썬에서는 메서드가 "이름"이 같으면 앞선 정의를 덮어써버림
#     def do_something(self, x, y):
#         print('두 번째 do_something 메서드:', x, y)


# example = Example()
# # TypeError: do_something() missing 1 required positional argument: 'y'
# example.do_something(10)
