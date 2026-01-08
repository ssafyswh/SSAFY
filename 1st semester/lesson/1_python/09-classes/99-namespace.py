class Person:
    name = 'unknown'

    def talk(self):
        print(self.name)


# p1 인스턴스 생성
p1 = Person()
p1.talk()  # unknown

# p2 인스턴스 생성 (인스턴스 변수 설정 전)
p2 = Person()
p2.talk()  # unknown

# p2 인스턴스 변수 설정 후
p2.name = 'Kim'
p2.talk()  # Kim

# 클래스 변수 name 값이 변경된 것이 아님(클래스 변수 name은 여전히 'unknown')
print(Person.name)  # unknown
# p2의 name은 인스턴스 변수로 설정된 값
print(p2.name)  # Kim
# 인스턴스는 독립적이므로 p1의 name은 여전히 'unknown'
print(p1.name)  # unknown
