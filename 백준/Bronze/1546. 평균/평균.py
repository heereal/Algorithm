N = int(input())
arr = list(map(int, input().split()))
M = max(arr)
total = 0

for score in arr:
    total += score/M*100

print(total/N)