import sys
input = sys.stdin.readline

import collections
deque = collections.deque

N = int(input())
queue = deque()

for _ in range(N):
    cmd = input().strip().split()

    if cmd[0] == 'push':
        queue.append(cmd[1])
    elif cmd[0] == 'pop':
        if queue:
            print(queue.pop())
        else:
            print(-1)
    elif cmd[0] == 'size':
        print(len(queue))
    elif cmd[0] == 'empty':
        if queue:
            print(0)
        else:
            print(1)
    elif cmd[0] == 'top':
        if queue:
            print(queue[-1])
        else:
            print(-1)