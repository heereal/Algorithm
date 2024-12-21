M, N = map(int, input().split())
board = []
min = 64

black_first = 'BWBWBWBWWBWBWBWBBWBWBWBWWBWBWBWBBWBWBWBWWBWBWBWBBWBWBWBWWBWBWBWB'
white_first = 'WBWBWBWBBWBWBWBWWBWBWBWBBWBWBWBWWBWBWBWBBWBWBWBWWBWBWBWBBWBWBWBW'

for _ in range(M):
    board.append(input())

for i in range(M-7):
    for j in range(N-7):
        chessboard = [str[j:j+8] for str in board[i:i+8]]
        for chess in [black_first, white_first]:
            differ = 0
            for k in range(64):
                if ''.join(chessboard)[k] != chess[k]:
                    differ += 1
            if differ < min:
                min = differ

print(min)