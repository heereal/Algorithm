arr = list(map(int, input().split()))
normal = [1, 1, 2, 2, 2, 8]
for i in range(6):
    print(normal[i] - arr[i], end=" ")