n, r = map(int, input().split())
returns = list(map(int, input().split()))
answer = []

if n == r:
    print('*')
else:
    for i in range(1, n + 1):
        if i not in returns:
            answer.append(i)
            print(i, end=" ")
        if len(answer) == n - r:
            break