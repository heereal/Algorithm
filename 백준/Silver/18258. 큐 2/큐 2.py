import sys
from collections import deque

input = sys.stdin.readline

N = int(input())
queue = deque()

for _ in range(N):
    order = input().strip()

    if 'push' in order:
        X = order.split()[1]
        queue.append(int(X))
    elif order == 'pop':
        if queue:
            print(queue.popleft())
        else:
            print(-1)
    elif order == 'size':
        print(len(queue))
    elif order == 'empty':
        if queue:
            print(0)
        else:
            print(1)
    elif order == 'front':
        if queue:
            print(queue[0])
        else:
            print(-1)
    elif order == 'back':
        if queue:
            print(queue[-1])
        else:
            print(-1)