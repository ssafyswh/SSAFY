# im_1445482
# 1445482
import sys
sys.stdin = open("input.txt")

T = int(input())
for case_num in range(1, T + 1):
    N, M, K = list(map(int, input().split()))
    result = 0
    count = K
    correct = M
    incorrect = N - M
    double = (M - (K - 1) * incorrect) // K
    if M < K:
        result = M
        print(f'#{case_num} {result}')
        continue
    for _ in range(N):
        if correct > 0:
            if count > 1:
                result += 1
                count -= 1
                correct -= 1
                continue
            if count == 1 and double > 0:
                result += 1
                correct -= 1
                result *= 2
                double -= 1
            count = K
        else:
            break
    print(f'#{case_num} {result}')


