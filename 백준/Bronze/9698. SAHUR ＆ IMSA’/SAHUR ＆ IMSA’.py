n = int(input())

for i in range(1, n + 1):
    h, m = map(int, input().split())

    if m - 45 < 0:
        h -= 1
        if h < 0:
            h = 23
            
    if m - 45 < 0:
        m = 60 - abs(m - 45)
    else:
        m -= 45
    
    print(f'Case #{i}: {h} {m}')