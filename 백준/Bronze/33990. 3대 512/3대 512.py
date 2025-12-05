n = int(input())
res = []

for _ in range(n):
    total = sum(map(int, input().split()))
    if total >= 512:
        res.append(total)

if res:
    print(min(res))
else:
    print(-1)