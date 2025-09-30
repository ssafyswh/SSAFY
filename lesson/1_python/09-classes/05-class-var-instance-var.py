class Circle:
    pi = 3.14

    def __init__(self, radius):
        self.radius = radius


c1 = Circle(5)
c2 = Circle(10)

print(c1.radius)  # 5
print(c2.radius)  # 10

# c1이 본인 인스턴스 변수 pi를 생성
c1.pi = 100

print(c1.pi)  # 100
print(Circle.pi)  # 3.14

# 반면 c2는 인스턴스 변수 pi가 없음. 그래서 클래스에 pi를 찾아가서 조회
print(c2.pi)  # 3.14
