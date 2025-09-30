T = int(input())
for case_num in range(1, T + 1):
    N, M, K = list(map(int, input().split()))
    space = [input() for _ in range(N)]
    y_result, x_result = -1, -1 # 탐색 실패시 출력할 기본값
    for n in range((N - M + 1) ** 2):   # 가능한 탐색의 영역 개수만큼 반복
        x_start = n % (N - M + 1)   # 탐색 시작 좌표를 이미 주어진 변수들에 의해 계산
        y_start = n // (N - M + 1)
        count = 0   # 한번의 탐색 과정에서 '*'의 개수를 저장할 변수
        for y in range(y_start, y_start + M):
            for x in range(x_start, x_start + M):
                if space[y][x] == '*':
                    count += 1
        if count == K:
            x_result = x_start
            y_result = y_start
            break   # 조건을 만족하는 영역이 한개 이하이므로, 탐색 성공시 반복 종료
    print(f'#{case_num} {y_result} {x_result}')
