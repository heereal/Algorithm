n = int(input())

for i in range(1, n + 1):
    arr = reversed(input().split())
    s = " ".join(arr)
    print(f'Case #{i}: {s}')
