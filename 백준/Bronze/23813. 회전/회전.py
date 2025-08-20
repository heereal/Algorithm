from collections import deque

n = input()
queue = deque(n)
answer = 0

for _ in range(len(n)):
    queue.rotate(1)
    answer += int("".join(queue))

print(answer)