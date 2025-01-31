from collections import deque

N = int(input())
deq = deque(enumerate(map(int, input().split())))
result = []

while deq:
    idx, cmd = deq.popleft()
    result.append(idx+1)

    if cmd >= 0:
        deq.rotate(-(cmd-1))
    else:
        deq.rotate(-cmd)

print(" ".join(map(str, result)))