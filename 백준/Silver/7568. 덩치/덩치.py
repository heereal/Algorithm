N = int(input())
li = []

for _ in range(N):
    X, Y = map(int, input().split())
    li.append([X, Y])

for X, Y in li:
    rank = 1

    for P, Q in li:
        if X < P and Y < Q:
            rank += 1

    print(rank, end=" ")