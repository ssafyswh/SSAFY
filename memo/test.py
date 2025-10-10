import sys
sys.stdin = open('input.txt')
# sys.stdout = open('output.txt', 'w', encoding='UTF-8')

import sys
from collections import deque


def find_start():
    for y in range(N):
        for x in range(N):
            if sea[y][x] == 9:
                return y, x
            
            
def find_fish():
    cnt = 0
    for y in range(N):
        for x in range(N):
            if sea[y][x] < size:
                return True
    return False


def catch_fish():
    global size, count
    sy, sx = find_start()
    q = deque([(0, sy, sx)])
    while q:
        time, ny, nx = q.popleft()
        for d1, d2 in delta:
            dy, dx = ny + d1, nx + d2
            if not (0 <= dy < N and 0 <= dx < N):
                continue
            if sea[dy][dx] > size:
                continue
            if 1 <= sea[dy][dx] < size:
                sea[dy][dx] = 0
                count -= 1
                if not count:
                    size += 1
                    count = size
            q.append((time + 1, dy, dx))
    
    
def solve():
    while True:
        if not find_fish():
            break
        
    
delta = [(0, 1), (1, 0), (0, -1), (-1, 0)]

N = int(input())
size, count = 2, 2
sea = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
        