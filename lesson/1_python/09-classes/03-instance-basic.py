class Person:
    def __init__(self, name, age):
        self.name = name  # 인스턴스 속성
        self.age = age  # 인스턴스 속성

    def introduce(self):
        print(f'안녕하세요. 저는 {self.name}, 나이는 {self.age}살입니다.')


# 인스턴스 생성
# 인스턴스 = 클래스호출
p1 = Person('Alice', 25)
p2 = Person('Bella', 30)

# 인스턴스 변수 접근 및 출력
print(p1.name)
print(p2.name)

# 메서드 호출
p1.introduce()
p2.introduce()
