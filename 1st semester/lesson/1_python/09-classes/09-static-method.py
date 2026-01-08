class MathUtils:
    # 정적 메서드
    # 클래스나 인스턴스에 의존하지 않고 독립적으로 동작
    # 정적 메서드는 클래스나 인스턴스의 상태를 변경하지 않음
    @staticmethod
    def add(a, b):
        return a + b


# 정적 메서드 호출
print(MathUtils.add(3, 5))  # 8
