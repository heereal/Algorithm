money = int(input())
n = len(str(money))
cnt = 0

while True:
    money *= 2
    if len(str(money)) > n:
        print(cnt)
        break
    cnt += 1