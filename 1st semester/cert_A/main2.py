import sys
sys.stdin = open("input.txt")

T = int(input())
for case_num in range(1, T + 1):
    N = int(input())
    trees = list(map(int, input().split()))
    highest = max(trees)
    grow = []
    one = 0
    result = 0
    for tree in trees:
        if highest - tree > 1:
            grow.append(highest - tree)
        elif highest - tree == 1:
            one += 1
    temp = 0
    for num in grow:
        temp += num // 2
    if temp < one:
        for i in range(len(grow)):
            while grow[i] > 1 and temp > 1:
                grow[i] -= 2
                temp -= 1
                one -= 1
                result += 2
            if temp < 1:
                break
        one += sum(grow)
        result += (one * 2 - 1)
    else:
        result = (sum(grow) // 3) * 2 + sum(grow) % 3
    print(f'#{case_num} {result}')
