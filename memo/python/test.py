import sys
sys.stdin = open('input.txt')
# sys.stdout = open('output.txt', 'w', encoding='UTF-8')

import sys
from collections import deque

sys.setrecursionlimit(10**7)

def find(node, route):
    if node == 1:
        route.append(node)
        return route
    route.append(node)
    return find(parent[node], route)
    
N = int(input())
tree = [[] for _ in range(N + 1)]
for _ in range(N - 1):
    a, b = map(int, sys.stdin.readline().split())
    tree[a].append(b)
    tree[b].append(a)

parent = [-1] * (N + 1)
parent[1] = 1
q = deque([1])
while q:
    now = q.popleft()
    for target in tree[now]:
        if parent[target] != -1:
            continue
        parent[target] = now
        q.append(target)
        
M = int(input())
for _ in range(M):
    u, v = map(int, sys.stdin.readline().split())
    ancestor_u, ancestor_v = find(u, []), find(v, [])
    ancestor_v = set(ancestor_v)
    for nod in ancestor_u:
        if nod in ancestor_v:
            print(nod)
            break
    

