import sys
sys.stdin = open("input.txt")

T = int(input())
for case_num in range(1, T + 1):
    N = int(input())
    trees = list(map(int, input().split()))
    highest = max(trees)
    odd = []
    odd_count = 0
    even = []
    even_count = 0
    for tree in trees:
        grow = highest - tree
        if grow != 0:
            if grow % 2 == 0:
                even.append(grow)
                even_count += 1
            else:
                odd.append(grow)
                odd_count += 1
    result = 0

    print(f'#{case_num} {result}')



