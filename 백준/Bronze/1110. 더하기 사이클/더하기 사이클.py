N = int(input())
num = N
cnt = 0

while True:
    a = num // 10
    b = num % 10
    c = (a + b) % 10

    num = int(str(b) + str(c))
    cnt += 1

    if N == num:
        print(cnt)
        break