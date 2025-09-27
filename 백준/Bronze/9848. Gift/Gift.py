n, k = map(int, input().split())
prev = 0
answer = 0

for _ in range(n):
    next = int(input())
    if next <= prev - k:
        answer += 1
    prev = next

print(answer)