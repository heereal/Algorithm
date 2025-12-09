p1, p2, p3 = sorted(list(map(int, input().split())), reverse=True)
c1, c2, c3 = map(int, input().split())

a = (p1 + p2 + p3) * (c1 * 0.01)
b = (p1 * (max(c2, c3) * 0.01)) + (p2 * (min(c2, c3) * 0.01))

if a > b:
    print(f'one {a:.2f}')
else:
    print(f'two {b:.2f}')