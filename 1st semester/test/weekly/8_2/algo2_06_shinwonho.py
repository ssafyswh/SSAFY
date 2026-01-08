T = int(input())
delta = [[0, 1], [-1, 0], [0, -1], [1, 0]]  # 인접구역을 확인하기 위한 방향 설정
for case_num in range(1, 1 + T):
    N, M = list(map(int, input().split()))
    rain = [list(map(int, input().split())) for _ in range(N)]
    count = 0   # 테스트 케이스 별 안전구역의 개수를 저장하기 위한 변수
    for y in range(1, N - 1):
        for x in range(1, M - 1):   # 가장자리는 안전구역에서 제외되므로 반복구간에서 제외한다.
            for direct in delta:
                if rain[y][x] <= rain[y + direct[0]][x + direct[1]]:
                    break   # 인접구역중 하나라도 안전구역 조건을 만족하지 않는다면 break
            else:
                count += 1  # 모든 인접구역들에 대해 조건을 만족했다면 안전구역 카운트를 올린다.
    print(f'#{case_num} {count}')