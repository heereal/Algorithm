n = int(input())
days = [0] * 32

for _ in range(n):
    start, end = map(int, input().split())

    for i in range(start, end):
        days[i] += 1

k = int(input())

if max(days) > k:
    print(0)
else:
    print(1)