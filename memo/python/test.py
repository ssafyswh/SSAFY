import sys
sys.stdin = open('input.txt')
# sys.stdout = open('output.txt', 'w', encoding='UTF-8')

import sys
input = sys.stdin.readline
from heapq import heappush, heappop

N, M = map(int, input().split())
ward = [*map(int, input().split())]
ward[-1] = 0
lane = [[] for _ in range(N)]
for _ in range(M):
    a, b, t = map(int, input().split())
    lane[a].append((b, t))
    lane[b].append((a, t))

INF = float('inf')
result = [INF] * N
hq = [(0, 0)]
while hq:
    now_dist, now_pos = heappop(hq)
    if now_dist > result[now_pos]:
        continue
    if now_pos == N - 1:
        break
    for target in lane[now_pos]:
        nxt_pos, dist = target
        if ward[nxt_pos] == 1:
            continue
        nxt_dist = dist + now_dist
        if nxt_dist < result[nxt_pos]:
            heappush(hq, (nxt_dist, nxt_pos))
            result[nxt_pos] = nxt_dist

print(result[-1] if result[-1] != INF else -1)

