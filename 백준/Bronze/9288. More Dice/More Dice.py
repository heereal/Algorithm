t = int(input())
arr = []

for i in range(1, 7):
    for j in range(i, 7):
        arr.append((i, j))

for i in range(t):
    n = int(input())
    print(f'Case {i+1}:')

    for a, b in arr:
        if a + b == n:
            print(f'({a},{b})')
