n = int(input())
flights = [int(input()) for _ in range(n)]

res = min(flights) - (max(flights) // 2)
if res < 0:
    print(0)
else:
    print(res)