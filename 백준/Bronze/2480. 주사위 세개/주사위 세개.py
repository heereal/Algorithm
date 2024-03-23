first, second, third = map(int, input().split())
[a, b, c] = sorted([first, second, third])

if a == b and b == c:
   print(10000 + (a * 1000))
elif a == b or b == c:
    print(1000 + (b * 100))
else:
    print(c * 100)