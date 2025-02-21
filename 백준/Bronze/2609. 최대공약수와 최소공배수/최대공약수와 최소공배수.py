A, B = map(int, input().split())

def gcd(a, b):
    c = a % b

    if c != 0:
        return gcd(b, c)
    else:
        return b


print(gcd(A, B)) # 최대공약수

big = max(A, B)
small = min(A, B)
cnt = 1

while True:
    if (big * cnt) % small == 0:
        print(big * cnt) # 최대공약수
        break
    else:
        cnt += 1
