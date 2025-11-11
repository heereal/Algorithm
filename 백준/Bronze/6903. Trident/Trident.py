t = int(input())
s = int(input())
h = int(input())

for _ in range(t):
    res = '*' + (" " * s) + '*' + (" " * s) + '*'
    print('*' + (" " * s) + '*' + (" " * s) + '*')

print('*' * ((s * 2) + 3))

for _ in range(h):
    print(" " * (s + 1) + '*')