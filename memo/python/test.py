import sys
sys.stdin = open('input.txt')
# sys.stdout = open('output.txt', 'w', encoding='UTF-8')

import sys

import sys
from collections import deque

N = int(input())
parent = [0] * N
children = [[] for _ in range(N)]
for _ in range(N - 1):
    a, b = map(int, sys.stdin.readline().split())
    parent[b] = a
    children[a].append(b)

levels = [0] * N
for n in range(N):
    node = n
    level = 0
    while node != 0:
        node = parent[node]
        level += 1
    levels[n] = level

H = int(input())
max_level = max(levels)
result = 0
while max_level > H:
    V = levels.index(H - 1)
    parent[V] = levels.index(H + 1)
    shommed = [False] * N
    shommed[V] = True
    q = deque([V])
    while q:
        now = q.popleft()
        for child in children[now]:
            if not shommed[child]:
                shommed[child] = True
                q.append(child)
    for n in range(N):
        if shommed[n]:
            levels[n] -= 2
    result += 1
print(result)