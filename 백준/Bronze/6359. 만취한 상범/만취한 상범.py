t = int(input())

for _ in range(t):
    n = int(input())
    arr = [1] * n

    for i in range(2, n+1):
        j = i
        while j <= n:
            if arr[j-1] == 1:
                arr[j-1] = 0
            else:
                arr[j-1] = 1
            j += i
    
    print(sum(arr))
