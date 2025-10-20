import sys
sys.stdin = open('input.txt')
# sys.stdout = open('output.txt', 'w', encoding='UTF-8')


import sys
import heapq

def dijkstra(start, goal):
    visited = [float('inf')] * (n + 1)
    q = [(0, start)]
    while q:
        distance, now = heapq.heappop(q)
        if now == goal:
            return distance
        visited[now] = distance
        for target in edges[now]:
            if visited[target[0]] < distance + target[1]:
                continue
            heapq.heappush(q, (distance + target[1], target[0]))
    return False

T = int(input())
for _ in range(T):
    n, m, t = map(int, sys.stdin.readline().split())
    edges = [[] for _ in range(n + 1)]
    s, g, h = map(int, sys.stdin.readline().split())
    for _ in range(m):
        a, b, d = map(int, sys.stdin.readline().split())
        edges[a].append((b, d))
        edges[b].append((a, d))
    candidate = sorted([int(sys.stdin.readline()) for _ in range(t)])
    s_to_g = dijkstra(s, g)
    s_to_h = dijkstra(s, h)
    g_to_c = []
    h_to_c = []
    for candy in candidate:
        g_to_c.append(dijkstra(g, candy))
        h_to_c.append(dijkstra(h, candy))
    print(g_to_c, h_to_c)