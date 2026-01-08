class Person:
    population = 0

    def __init__(self, name):
        self.name = name
        Person.increase_population()
        # Person.population += 1

    # 클래스 메서드
    @classmethod
    def increase_population(cls):
        cls.population += 1


# 인스턴스 생성
person1 = Person('Alice')
person2 = Person('Bob')

# 클래스 변수 접근
print(Person.population)  # 2
