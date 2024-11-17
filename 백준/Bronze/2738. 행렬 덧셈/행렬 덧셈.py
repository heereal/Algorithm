N, M = map(int, input().split())
num_list = []

for _ in range(N):
    temp = list(map(int, input().split()))
    num_list.append(temp)

for i in range(N):
    temp = list(map(int, input().split()))
    for j in range(M):
        result = num_list[i][j] + temp[j]
        print(result, end=" ")
    print()