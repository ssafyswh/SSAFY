T = int(input())
for case_num in range(1, 1 + T):
    N, M = map(int, input().split())
    nums = list(map(int, input().split()))[::-1]    # 배열을 스택으로 사용하기 위해 역순으로 재배치
    result = 0
    while nums:     # 배열 내 모든 원소를 체크할때 까지
        is_increasing = True    # 증가패턴을 유지하고 있는가
        now = None
        for _ in range(M):      # 각 윈도우 단위의 원소를 확인
            if not nums:        # 윈도우가 가득 차지 않은 경우 break 후 증가패턴 확인
                break
            if now is None:
                now = nums.pop()
                continue
            if now >= nums[-1]:     # 증가패턴이 유지중인 지 체크
                is_increasing = False
            now = nums.pop()        # 확인한 원소는 제거
        if is_increasing:
            result += 1
    print(f'#{case_num} {result}')
