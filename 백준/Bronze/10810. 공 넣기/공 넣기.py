N, M = map(int, input().split())
baskets = [0 for _ in range(N)]
for _ in range(M):
    i, j, k = map(int, input().split())
    baskets[i-1:j] = [k for _ in range(j-i+1)]

for n in baskets:
    print(n, end=" ")