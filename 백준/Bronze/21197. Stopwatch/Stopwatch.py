n = int(input())

if n % 2 != 0:
    print('still running')
else:
    arr = [int(input()) for _ in range(n)]
    seconds = 0

    for i in range(1, n, 2):
        seconds += arr[i] - arr[i-1]

    print(seconds)