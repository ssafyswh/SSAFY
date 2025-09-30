def robot(y1, x1, n=0, s=0):    # y1, x1: 현재 위치 좌표, n: 수확한 사과수, s: 이동 거리 합계
    global result
    if n == N:      # 사과를 모두 수확했다면
        distance = y1 + x1      # 농장으로 되돌아오는 거리를 합산
        result = min(result, s + distance)  # 최소값 갱신
        return
    if s >= result:     # 이미 이동한 거리가 현재 최소값 이상일 경우
        return          # 탐색 중단
    for i in range(N):
        if harvest[i]:  # 이미 수확한 사과라면 continue
            continue
        y2, x2 = apple[i]
        distance = abs(y1 - y2) + abs(x1 - x2)
        harvest[i] = 1  # 사과의 수확을 기록
        robot(y2, x2, n + 1, s + distance)  # 재귀
        harvest[i] = 0  # 재귀를 빠져 나온 후 확인용 배열을 복구


T = int(input())
for case_num in range(1, 1 + T):
    N = int(input())
    apple = []
    harvest = [0] * N   # 백트래킹을 위한 확인 배열
    for _ in range(N):
        r, c = map(int, input().split())
        apple.append((r, c))
    sy, sx = 0, 0
    result = 2201   # 한번의 이동거리가 최대 200을 넘을 수 없으며, 이동횟수는 최대 11번
    robot(sy, sx)
    print(f'#{case_num} {result}')
