N, K = map(int, input().split())
arr = list(map(int, input().split()))

flag = False
cnt = 0

for i in range(N):
    for j in range(N-i-1):
        if arr[j] > arr[j+1]:
            arr[j], arr[j+1] = arr[j+1], arr[j]

            cnt += 1
            if cnt == K:
                flag = True
                print(arr[j], arr[j+1])
    if flag:
        break

if cnt < K:
    print(-1)