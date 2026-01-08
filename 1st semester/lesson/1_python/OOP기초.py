# class 라는 것을 왜 쓸까?
# - 중복된 코드를 많이 줄일 수 있다

# 전사, 궁수, 마법사
# - 공통: 체력, 마나, 공격력
# - 기능: 공격하기, 걷기, 상태확인
# 전사만 할 수 있는 것: 칼로때리기(), 강하게소리지르기()
# 궁수만 할 수 있는 것: 활쏘기(), 자세히살펴보기()
# 마법사만 할 수 있는 것: 마법쓰기(), 똑똑해지기()

# 상황1. 전체 캐릭터의 수를 관리해야 한다
# - 전역변수로 관리
#  -> Character class 와 관련된 변수인데, 외부에 값을 관리
#  --> 유지보수가 어려워진다.

class Character:
    total_players = 0  # 클래스 변수
                       # 모든 인스턴스가 공유하는 값
    double_event = True  # ex) 경험치 2배 이벤트

    # self : 인스턴스 자기자신을 가리킨다
    # 생성자에 전달되는 값 : 인스턴스의 초기값
    def __init__(self, hp, mp, power, name):
        self.hp = hp
        self.mp = mp
        self.power = power
        self.name = name
        Character.increase_character()

    # 인스턴스 메서드
    def attack(self):
        print(f"{self.power}의 데미지로 공격!")

    def walk(self):
        print(f'{self.name}이(가) 앞으로 걸어간다.')

    def status(self):
        print('=' * 20)
        print(f'이름: {self.name}')
        print(f'HP: {self.hp}')
        print(f'Mp: {self.mp}')
        print(f'공격력: {self.power}')
        print('=' * 20)

    @classmethod
    def increase_character(cls):
        cls.total_players += 1

    @staticmethod
    def critical_rate(basic_power):
        import random
        if random.random() < 0.2:
            print('Critical!')
            return basic_power * 2
        return basic_power

# 클래스명() => 클래스의 생성자를 호출해라고 정해놓음
character1 = Character(100, 50, 10, 'Ina') # 1번 캐릭터 (인스턴스)
character2 = Character(500, 200, 100, 'Flare')  # 2번 캐릭터 (인스턴스)

character1.attack()
character2.attack()

character1.walk()
character2.walk()

character1.status()
character2.status()

# 인스턴스를 통해서도 클래스 변수에 접근 가능!
# --> 하지마라!
# print(f'전체 캐릭터 수 = {character1.total_players}')
print(f'전체 캐릭터 수 = {Character.total_players}')

# 내일 배울 것: 상속
class Warrior(Character):
    def slash_blast(self):
        print(f'{self.name} used slash blast.')
        return(self.power * 1.2)

    def dragon_roar(self):
        print(f'{self.name} used dragon roar.')
        self.power = self.power * 1.2
        return self.power

warrior1 = Warrior(200, 300, 50, 'doro')
print(warrior1.hp, warrior1.mp)

class Archer:
    def sharp_eyes(self):

        pass


class Wizard:
    def magic_guard():
        pass
    
    def magic_claw():
        pass

# 내일 실습 할 것 : 인스턴스 메서드 추가해보기, 클래스 메서드, 스태틱 메서드
# - 상속 실습

class Operator:
    def __init__(self):
        self.permission_level = 'administrator'

    def kick (self, target):
        print(f'{target} is kicked.')

class OperatorWarrior(Operator, Warrior):
    def __init__(self, hp, mp, power, name):
        super().__init__()
    pass

print(OperatorWarrior.__mro__)
oper1 = OperatorWarrior(100, 100, 100, 'ptg')
print(oper1.permission_level)
print(oper1.hp)