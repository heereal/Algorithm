def solution(board):
    m, n = len(board), len(board[0])
    moves = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
    answer = 0
    
    for i in range(m):
        for j in range(n):
            if board[i][j] == 1:
                for dx, dy in moves:
                    nx, ny = i + dx, j + dy
                    if 0 <= nx < m and 0 <= ny < n and board[nx][ny] != 1:
                        board[nx][ny] = -1
    
    for line in board:
        answer += line.count(0)
                
    return answer