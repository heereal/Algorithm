N = int(input())
paper = [[0]*100 for _ in range(100)]

for _ in range(N):
    X, Y = map(int, input().split())

    for i in range(X, X+10):
        for j in range(Y, Y+10):
            paper[i][j] = 1

cnt = 0
for arr in paper:
    cnt += arr.count(1)

print(cnt)