import sys
sys.stdin = open('input.txt')
# sys.stdout = open('output.txt', 'w', encoding='UTF-8')


import sys

s, n = map(int, input().split())
nums = str(n)
lcd = [[' '] * ((s + 2) * len(nums) + (len(nums) - 1)) for _ in range(2 * s + 3)]
panel = [
    {2, 3, 5, 6, 7, 8, 9, 0},
    {4, 5, 6, 8, 9, 0},
    {1, 2, 3, 4, 7, 8, 9, 0},
    {2, 3, 4, 5, 6, 8, 9},
    {2, 6, 8, 0},
    {1, 3, 4, 5, 6, 7, 8, 9, 0},
    {2, 3, 5, 6, 8, 9, 0}
]
for i in range(len(nums)):
    start_x = (s + 3) * i
    num = int(nums[i])
    if num in panel[0]:
        for x in range(start_x + 1, start_x + s + 1):
            lcd[0][x] = '-'
    if num in panel[1]:
        for y in range(1, s + 1):
            lcd[y][start_x] = '|'
    if num in panel[2]:
        for y in range(1, s + 1):
            lcd[y][start_x + s + 1] = '|'
    if num in panel[3]:
        for x in range(start_x + 1, start_x + s + 1):
            lcd[s + 1][x] = '-'
    if num in panel[4]:
        for y in range(s + 2, 2 * s + 2):
            lcd[y][start_x] = '|'
    if num in panel[5]:
        for y in range(s + 2, 2 * s + 2):
            lcd[y][start_x + s + 1] = '|'
    if num in panel[6]:
        for x in range(start_x + 1, start_x + s + 1):
            lcd[2 * s + 2][x] = '-'
for row in lcd:
    print(''.join(row))

