class Counter:
    def __init__(self):
        self.count = 0

    # 인스턴스 메서드
    def increment(self):
        self.count += 1


c1 = Counter()
c2 = Counter()

# 인스턴스 메서드 호출
c1.increment()
print(c1.count)  # 1
print(c2.count)  # 0
