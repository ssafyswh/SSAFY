import sys
sys.stdin = open('input.txt')
# sys.stdout = open('output.txt', 'w', encoding='UTF-8')


import sys
from math import factorial
N = int(input())
print(factorial(N) // (24 * factorial(N - 4)) if N > 3 else 0)