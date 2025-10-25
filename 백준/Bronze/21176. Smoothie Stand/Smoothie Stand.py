import sys
input = sys.stdin.readline

k, r = map(int, input().split())
total = list(map(int, input().split()))
answer = []

for _ in range(r):
    arr = list(map(int, input().split()))
    cur = arr[:k]
    price = arr[k]

    cnt = 0
    while True:
        cnt += 1
        finished = False
        
        for i in range(k):
            if cur[i] * cnt > total[i]:
                finished = True
                break

        if finished:
            cnt -= 1
            break

    answer.append(price * cnt)

print(max(answer))