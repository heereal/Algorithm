import sys
input = sys.stdin.readline

from collections import deque

N = int(input())
d = deque()

for i in range(N):
    x = input().split()
    
    if x[0] == '1':
        d.insert(0, x[1])
    elif x[0] == '2':
        d.append(x[1])
    elif x[0] == '3':
        if d:
            print(d.popleft())
        else:
            print(-1)
    elif x[0] == '4':
        if d:
            print(d.pop())
        else:
            print(-1)
    elif x[0] == '5':
        print(len(d))
    elif x[0] == '6':
        if d:
            print(0)
        else:
            print(1)
    elif x[0] == '7':
        if d:
            print(d[0])
        else:
            print(-1)
    elif x[0] == '8':
        if d:
            print(d[-1])
        else:
            print(-1)