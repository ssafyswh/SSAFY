# import sys

# sys.stdin = open('input.txt')

from heapq import heappush, heappop

House = 0
Path = []

def init(N, K, sBuilding, eBuilding, mDistance):
    global House, Path
    House = N
    Path = [[]for _ in range(N)]
    for i in range(K):
        Path[sBuilding[i]].append((eBuilding[i],mDistance[i]))
        Path[eBuilding[i]].append((sBuilding[i],mDistance[i]))
    return


def add(sBuilding, eBuilding, mDistance):
    Path[sBuilding].append((eBuilding,mDistance))
    Path[eBuilding].append((sBuilding,mDistance))
    return


def calculate(M, mCoffee, P, mBakery, R):
    INF = 21e8
    Cafe_Weight = [INF] * House
    Bakery_Weight = [INF] * House

    # 상점 위치 기록 (상점 제외 조건용)
    is_shop = [False] * House

    Cafe_Q = []
    for m in range(M):
        node = mCoffee[m]
        Cafe_Weight[node] = 0
        is_shop[node] = True
        heappush(Cafe_Q, (0, node))

    Bakery_Q = []
    for p in range(P):
        node = mBakery[p]
        Bakery_Weight[node] = 0
        is_shop[node] = True
        heappush(Bakery_Q, (0, node))

    # Cafe 다익스트라 (R 제한 추가)
    while Cafe_Q:
        w, n = heappop(Cafe_Q)
        if w > Cafe_Weight[n]: continue
        for nn, dw in Path[n]:
            next_w = w + dw
            if next_w <= R and next_w < Cafe_Weight[nn]:
                Cafe_Weight[nn] = next_w
                heappush(Cafe_Q, (next_w, nn))

    # Bakery 다익스트라 (R 제한 추가)
    while Bakery_Q:
        w, n = heappop(Bakery_Q)
        if w > Bakery_Weight[n]: continue
        for nn, dw in Path[n]:
            next_w = w + dw
            if next_w <= R and next_w < Bakery_Weight[nn]:
                Bakery_Weight[nn] = next_w
                heappush(Bakery_Q, (next_w, nn))

    res = INF
    for i in range(House):
        if is_shop[i]: continue  # 상점인 노드는 제외
        if Cafe_Weight[i] <= R and Bakery_Weight[i] <= R:
            res = min(res, Cafe_Weight[i] + Bakery_Weight[i])

    return -1 if res >= INF else res