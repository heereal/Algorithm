n = int(input())

a = 2
while True:
    if n % a != 0:
        print(a, end=" ")
        break
    else:
        a += 1

b = n - 1
while True:
    if n % b != 0:
        print(b)
        break
    else:
        b -= 1