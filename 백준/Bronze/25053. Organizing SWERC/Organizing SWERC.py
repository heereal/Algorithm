import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n = int(input())
    arr = [0] + ([-1] * 10)

    for _ in range(n):
        b, d = map(int, input().split())
        arr[d] = max(arr[d], b)
    
    if -1 in arr:
        print('MOREPROBLEMS')
    else:
        print(sum(arr))