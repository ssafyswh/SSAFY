import sys
sys.stdin = open('input.txt')
# sys.stdout = open('output.txt', 'w', encoding='UTF-8')

import sys

T = int(input())
for _ in range(T):
    n, k, t, m = map(int, sys.stdin.readline().split())
    