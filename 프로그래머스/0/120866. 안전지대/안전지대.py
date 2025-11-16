def solution(board):
    m, n = len(board), len(board[0])
    danger = set()
    
    for i in range(m):
        for j in range(n):
            if board[i][j] == 1:
                danger.update((i + dx, j + dy) for dx in [-1, 0, 1] for dy in [-1, 0, 1])
                
    return n * n - sum(0 <= x < m and 0 <= y < n for x, y in danger)