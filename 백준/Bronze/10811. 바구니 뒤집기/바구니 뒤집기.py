N, M = map(int, input().split())
baskets = [i for i in range(1, N+1)]

for _ in range(M):
    i, j = map(int, input().split())
    temp = baskets[i-1:j]
    temp.reverse()
    baskets[i-1:j] = temp

for n in baskets:
    print(n, end=" ")