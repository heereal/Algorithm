N, K = map(int, input().split())
num_list = []

for i in range(1, N+1):
    if N % i == 0:
        num_list.append(i)

if len(num_list) >= K:
    print(num_list[K-1])
else:
    print(0)