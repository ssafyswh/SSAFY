# import sys
# sys.stdin = open('input.txt')


def dice(n=0, k=0):     # n: 현재 위치한 칸, k: 현재 주사위를 던진 횟수
    global result       # result의 최댓값을 계속 갱신
    if k == K:          # 주사위를 정해진 횟수만큼 던졌을 때 재귀 종료
        result = max(n, result)
        return
    for i in range(1, 7):       # 현재 위치에서 주사위를 굴렸을 때 가능한 경우의 수를 탐색
        if n + i >= N:          # 마지막 칸에 도달할 수 있다면 result를 최댓값으로 고정하고 종료
            result = N
            return
        if board[n + i] and board[n + i] >= N:  # 이동한 칸에 화살표가 있고 도착점에 갈수 있을 경우 result 고정 후 종료
            result = N
            return
        elif board[n + i]:                      # 이동한 칸에 화살표가 있을 경우
            if not visited[board[n + i]]:      # visited를 사용하여 한 루트 내의 중복 탐색을 회피
                result = max(board[n + i], result)
                visited[board[n + i]] = 1
                dice(board[n + i], k + 1)       # 이동한 위치와 주사위 횟수 + 1을 입력값으로 함수 호출
                visited[board[n + i]] = 0
            continue
        else:
            result = max(n, result)     # 화살표 이동이 없었을 경우의 함수 호출
            if not visited[n + i]:
                visited[n + i] = 1
                dice(n + i, k + 1)      # 다음 주사위 굴림에 대한 호출
                visited[n + i] = 0


T = int(input())
for case_num in range(1, 1 + T):
    N, K, E = map(int, input().split())
    board = [0] * (N + 1)       # 각 칸의 화살표 정보를 저장. (출발 전 위치는 0번 칸)
    for e in range(E):
        start, end = map(int, input().split())
        board[start] = end
    result = 0
    visited = [0] * (N + 1)     # 중복 탐색을 막기 위해 탐색 과정을 저장할 배열
    dice()      # 재귀함수 실행
    print(f'#{case_num} {result}')
