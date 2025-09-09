def solution(m, n, board):
    board = [list(str) for str in board]
    res = [[0] * n for _ in range(m)]
    
    answer = 0
    count = 1
    
    while True:
        count += 1
        new_answer = answer
        
        if count % 2 != 0:
            res = [[0] * n for _ in range(m)]
            
            for i in range(m-1):
                for j in range(n-1):
                    if board[i][j] == '/':
                        continue
                        
                    if board[i][j] == board[i][j+1] == board[i+1][j] == board[i+1][j+1]:
                        res[i][j:j+2], res[i+1][j:j+2] = [1, 1], [1, 1]
            
            for i in range(m):
                for j in range(n):
                    if res[i][j]:
                        new_answer += 1
                        board[i][j] = "/"
                        
            if answer == new_answer:
                break
            else:
                answer = new_answer

        else:
            for i in range(m-1, 0, -1):
                for j in range(n):
                    if board[i][j] == "/":
                        for z in range(i-1, -1, -1):
                            if board[z][j] != "/":
                                board[i][j], board[z][j] = board[z][j], board[i][j]
                                break
            
    return answer