import sys
sys.stdin = open('input.txt')
# sys.stdout = open('output.txt', 'w', encoding='UTF-8')

import sys
input = sys.stdin.readline

N = int(input())
# LOG = N.bit_length()
# 2^17 > 100000
LOG = 17

tree = [[] for _ in range(N + 1)]
for _ in range(N - 1):
    A, B = map(int, input().split())
    tree[A].append(B)
    tree[B].append(A)

# ancestors[k][node]: node의 2^k번째 조상
ancestors = [[0] * (N + 1) for _ in range(LOG)]
depth = [-1] * (N + 1)

# 각 노드의 직계 부모와 깊이 계산, O(N)
def fill_depth():
    stack = [(1, 0)]
    depth[1] = 0
    while stack:
        now, d = stack.pop()
        for nxt in tree[now]:
            if depth[nxt] != -1:
                continue
            ancestors[0][nxt] = now
            depth[nxt] = d + 1
            stack.append((nxt, d + 1))

fill_depth()

# 희소 배열: node에서 2^n번 이동한 위치를 dp[node][n]와 같이 표기하는 자료구조
# node의 2^n번째 조상 = (node의 2^n-1번째 조상)의 2^n-1번째 좋상
for i in range(1, LOG):
    for j in range(1, N + 1):
        prev_ancestor = ancestors[i - 1][j]
        if prev_ancestor != 0:
            ancestors[i][j] = ancestors[i - 1][prev_ancestor]

def lca(a, b):
    # 더 깊이 있는 노드(b)를 일관적으로 지정
    if depth[a] > depth[b]:
        a, b = b, a

    # 두 노드의 깊이 차 diff를 이진수로 분해한 뒤 그만큼 올려서 깊이를 맞춤
    diff = depth[b] - depth[a]
    for i in range(LOG):
        if (diff >> i) & 1:
            b = ancestors[i][b]

    # 깊이를 맞췄을 때 같은 노드라면 그 노드가 LCA
    if a == b:
        return a

    # 두 노드의 2^i번째 조상이 같다면 pass, 같지 않다면 그만큼 위로 올라간다
    # 최종 도착위치는 LCA의 바로 아래 노드들이 된다
    for i in range(LOG - 1, -1, -1):
        if ancestors[i][a] != ancestors[i][b]:
            a = ancestors[i][a]
            b = ancestors[i][b]

    return ancestors[0][a]

M = int(input())
for _ in range(M):
    u, v = map(int, input().split())
    print(lca(u, v))
