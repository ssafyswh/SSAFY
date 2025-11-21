import sys
sys.stdin = open('input.txt')
# sys.stdout = open('output.txt', 'w', encoding='UTF-8')

import sys
input = sys.stdin.readline

d, keyword = input().split()
words = []
for _ in range(int(d)):
    words.append(input().strip())

dictionary = {}

for word in words:
    dictionary[word] = []
    length = len(word)
    for nxt_word in words:
        if len(nxt_word) != length + 1:
            continue
