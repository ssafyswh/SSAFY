# import sys
# sys.stdin = open('algo1_sample_in.txt')

T = int(input())
for case_num in range(1, 1 + T):
    N, M = map(int, input().split())
    data = [list(map(int, input().split())) for _ in range(N)]
    filt = [list(map(int, input().split())) for _ in range(M)]
    # R: result 배열의 크기
    R = N - M + 1
    result = [[0] * R for _ in range(R)]
    # (y, x): result 가 저장될 인덱스
    for y in range(R):
        for x in range(R):
            # (fy, fx): 필터의 인덱스
            # (y + fy, x + fx): 데이터의 인덱스
            for fy in range(M):
                for fx in range(M):
                    result[y][x] += filt[fy][fx] * data[y + fy][x + fy]
    print(f'#{case_num}')
    for row in result:
        print(*row)
