import sys
sys.stdin = open('input.txt')
from collections import deque

import sys
import heapq

import sys

def floyd():
    INF = 10 ** 7
    temp_result = [[INF] * n for _ in range(n)]

    for i in range(n):
        temp_result[i][i] = 0
    for i in range(1, n + 1):
        for target in bus[i]:
            temp_result[i - 1][target[0] - 1] = min(temp_result[i - 1][target[0] - 1], target[1])

    for k in range(n):
        for i in range(n):
            for j in range(n):
                temp_result[i][j] = min(temp_result[i][j], temp_result[i][k] + temp_result[k][j])

    return temp_result


n = int(input())
m = int(input())
bus = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b, c = map(int, sys.stdin.readline().split())
    bus[a].append((b, c))

result = floyd()
for r in range(n):
    for c in range(n):
        if result[r][c] == 10 ** 7:
            result[r][c] = 0

for row in result:
    print(*row)
