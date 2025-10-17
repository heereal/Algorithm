from itertools import combinations

n = int(input())

for i in range(1, n + 1):
    c = int(input())
    l = int(input())
    p = list(map(int, input().split()))

    combination = combinations(p, 2)
    
    for com in combination:
        if sum(com) == c:
            a = p.index(com[0]) + 1
            b = p[a:].index(com[1]) + 1 + a
            print(f'Case #{i}: {a} {b}')
            break