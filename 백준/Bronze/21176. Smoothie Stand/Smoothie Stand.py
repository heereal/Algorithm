import sys
input = sys.stdin.readline

k, r = map(int, input().split())
total = list(map(int, input().split()))
answer = 0

for _ in range(r):
    arr = list(map(int, input().split()))
    cur = arr[:k]
    price = arr[k]

    cnt = int(1e9)
    for i in range(k):
        if cur[i] > 0:
            cnt = min(cnt, total[i] // cur[i])

    answer = max(answer, price * cnt)

print(answer)