n, x = map(int, input().split())
intList = list(map(int, input().split()))
for a in intList:
    if a < x:
        print(a, end=" ")