x, y, n = map(int, input().split())

for i in range(1, n + 1):
    res = ''
    if i % x == 0:
        res += 'Fizz'
    if i % y == 0:
        res += 'Buzz'   
    print(res or i)