import sys
sys.stdin = open('input.txt')
# sys.stdout = open('output.txt', 'w', encoding='UTF-8')


import sys

result = int(int(input()) ** 0.5)
print(f'The largest square has side length {result}.')