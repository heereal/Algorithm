res = {'A': 0, 'B': 0}

while True:
    arr = input().split()
    n = int(arr[0])
    
    if n == 1:
        res[arr[1]] = int(arr[2])
    elif n == 2:
        print(res[arr[1]])
    elif n == 3:
        res[arr[1]] += res[arr[2]]
    elif n == 4:
        res[arr[1]] *= res[arr[2]]
    elif n == 5:
        res[arr[1]] -= res[arr[2]]
    elif n == 6:
        res[arr[1]] //= res[arr[2]]
    elif n == 7:
        break