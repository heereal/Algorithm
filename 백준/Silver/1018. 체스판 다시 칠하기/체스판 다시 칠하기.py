M, N = map(int, input().split())
board = []
count = []

for _ in range(M):
    board.append(input())

for i in range(M-7):
    for j in range(N-7):
        black_first = 0
        white_first = 0

        for a in range(i, i+8):
            for b in range(j, j+8):
                if (a+b) % 2 == 0:
                    if board[a][b] != 'W':
                        black_first += 1
                    elif board[a][b] != 'B':
                        white_first += 1
                else:
                    if board[a][b] != 'B':
                        black_first += 1
                    elif board[a][b] != 'W':
                        white_first += 1
        count.append(min(black_first, white_first))

print(min(count))