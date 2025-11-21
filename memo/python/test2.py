import sys
sys.stdin = open('input.txt')
# sys.stdout = open('output.txt', 'w', encoding='UTF-8')


import sys
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        if self.head is None:
            self.head = Node(data)
        else:
            node = self.head
            while node.next is not None:
                node = node.next
            node.next = Node(data)

    def insert(self, i, data):
        node = self.head
        for _ in range(i - 1):
            node = node.next
        new_node = Node(data)
        new_node.next = node.next
        node.next = new_node


for case_num in range(1, 11):
    N = int(input())
    codes = list(map(int, input().split()))
    nxt_codes = list(range(1, N))
    nxt_codes.append(-1)

    M = int(input())



    print(f'#{case_num}')




