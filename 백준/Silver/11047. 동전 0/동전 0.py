n, k = map(int, input().split())
coins = [int(input()) for _ in range(n)]
cnt = 0

for coin in sorted(coins, reverse=True):
    if coin <= k:
        cnt += (k // coin)
        k = k % coin
        
    if k == 0:
        break

print(cnt)