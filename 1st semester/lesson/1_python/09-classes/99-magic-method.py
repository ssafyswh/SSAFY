class Circle:
    def __init__(self, radius):
        self.radius = radius

    # __str__ 메서드 정의
    # 인스턴스를 문자열로 표현할 때 호출됨
    # print(c1) 호출 시 사용됨
    # 이 메서드를 정의하면 인스턴스를 print()로 출력할 때 더 읽기 쉬운 형식으로 출력됨
    # __str__ 메서드는 문자열을 반환해야 함
    def __str__(self):
        return f'원의 반지름: {self.radius}'


c1 = Circle(10)
c2 = Circle(1)

print(c1)  # 원의 반지름: 10
print(c2)  # 원의 반지름: 1
