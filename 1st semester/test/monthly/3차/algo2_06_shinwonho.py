# import sys
# sys.stdin = open('algo2_sample_in.txt')


def find(node):
    if root[node] == node:
        return root[node]
    return find(root[node])


def union(a, b):
    a = find(a)
    b = find(b)
    if a == b:
        return
    if a < b:
        root[b] = a
    elif a > b:
        root[a] = b
    return

# MST problem
# 간선의 개수가 충분히 적고(최대 465개) heapq를 사용할 수 없으므로
# 크루스칼 알고리즘 채택, union-find 사용
T = int(input())
for case_num in range(1, 1 + T):
    V, E = map(int, input().split())
    edges = []
    for _ in range(E):
        u, v, e = map(int, input().split())
        edges.append((e, u, v))
    # 간선의 가중치 순으로 정렬
    # 정렬에 용이하게끔 간선의 가중치를 튜플의 0번 인덱스에 받는다.
    edges.sort()
    count = 0
    index = -1
    root = list(range(V + 1))
    result = 0
    # 노드의 개수가 V + 1이므로 필요 간선 수 는 V
    # V <= E가 보장되므로 예외 처리 조건은 만들지 않는다.
    while count < V:
        index += 1
        edge = edges[index]
        # 이미 같은 집합이라면 continue
        if find(edge[1]) == find(edge[2]):
            continue
        union(edge[1], edge[2])
        result += edge[0]
        count += 1
    print(f'#{case_num} {result}')

