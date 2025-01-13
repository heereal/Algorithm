a, b = map(int, input().split())
aa, bb = a, b

while b > 0:
    a, b = b, a % b

print(aa*bb//a)