t = int(input())

for i in range(1, t + 1):
    n, k = map(int, input().split())
    mine = input()
    arr = [[] for _ in range(k)]

    for _ in range(n):
        data = input()
        for j in range(k):
            arr[j] += data[j]
    
    answer = 0
    for j in range(k):
        if mine[j] not in arr[j]:
            answer += 1
    
    print(f'Data Set {i}:\n{answer}/{k}\n')