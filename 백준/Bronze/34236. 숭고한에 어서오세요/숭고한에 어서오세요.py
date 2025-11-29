n = int(input())
arr = list(map(int, input().split()))
answer = arr[-1] + (arr[1] - arr[0])
print(answer)