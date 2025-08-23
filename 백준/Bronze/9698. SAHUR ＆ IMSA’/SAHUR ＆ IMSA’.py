n = int(input())

for i in range(1, n + 1):
    h, m = map(int, input().split())

    if m < 45:
        h -= 1
        m += 15
    else:
        m -= 45
        
    if h < 0:
        h = 23
    
    print(f'Case #{i}: {h} {m}')