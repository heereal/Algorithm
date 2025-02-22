N = int(input())
cnt = min(99, N)

for i in range(100, N+1):
    num = list(map(int, str(i)))

    if num[0] - num[1] == num[1] - num[2]:
        cnt += 1

print(cnt)