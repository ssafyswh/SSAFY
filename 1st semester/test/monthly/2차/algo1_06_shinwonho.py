import sys
sys.stdin = open('input.txt')

T = int(input())
for case_num in range(1, 1 + T):
    case = list(input().split('.'))     # '.'으로 구분된 문자들을 분리하여 리스트로 변환
    for i in range(len(case)):
        case[i] = case[i][::-1]     # 각 단어들을 역순으로 재배치
    print(f'#{case_num} {".".join(case)}')       # 단어들을 다시 '.'으로 연결하여 출력
