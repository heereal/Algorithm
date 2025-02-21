A, B = map(int, input().split())

def gcd_func(a, b):
    c = a % b

    if c != 0:
        return gcd_func(b, c)
    else:
        return b

gcd = gcd_func(A, B)
lcm = (A * B) // gcd

print(gcd)
print(lcm)
