import sys
from collections import deque
input = sys.stdin.readline

t = int(input())
input()

for _ in range(t):
    n, e = map(int, input().split())
    queue = deque([i for i in range(1, n + 1)])

    for i in range(e):
        p = int(input())
        queue.remove(p)
        queue.appendleft(p)
    
    print(queue.pop())
    input()