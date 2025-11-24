def solution(board, moves):
    n = len(board)
    answer = 0
    
    stack = [[] for _ in range(n + 1)]
    basket = []
    board.reverse()
    
    for i in range(n):
        for j in range(n):
            if board[j][i]:
                stack[i + 1].append(board[j][i])
        
    for i in moves:
        if stack[i]:
            next = stack[i].pop()
            
            if not basket:
                basket.append(next)
            elif basket[-1] == next:
                answer += 2
                basket.pop()
            else:
                basket.append(next)
        
    return answer