N, M = map(int, input().split())
baskets = [0 for _ in range(N)]
for i in range(N):
    baskets[i] = i + 1

for _ in range(M):
    i, j = map(int, input().split())
    a = baskets[i-1]
    b = baskets[j-1]
    baskets[i-1] = b
    baskets[j-1] = a

for n in baskets:
    print(str(n), end=" ")
