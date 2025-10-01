from collections import deque

n = int(input())
tree = list(map(int, input().split()))
r = int(input())

queue = deque([r])

while queue:
    cur = queue.popleft()
    tree[cur] = -2

    for i in range(n):
        if tree[i] == cur:
            queue.append(i)

answer = 0

for i in range(n):
    if tree[i] != -2 and i not in tree:
        answer += 1

print(answer)