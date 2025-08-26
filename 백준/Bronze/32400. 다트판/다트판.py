arr = list(map(int, input().split()))
i = arr.index(20)

a = (arr[i-1] + arr[i] + arr[(i+1) % 20]) / 3
b = sum(arr) / 20

if a > b:
    print('Alice')
elif a == b:
    print('Tie')
else:
    print('Bob')