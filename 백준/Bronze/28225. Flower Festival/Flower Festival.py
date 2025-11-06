n, f = map(int, input().split())
arr = []

for _ in range(n):
    x, v = map(int, input().split())
    time = (f - x) / v
    arr.append(time)

print(arr.index(min(arr)) + 1)