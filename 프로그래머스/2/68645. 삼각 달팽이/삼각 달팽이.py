def solution(n):
    snail = [[0] * i for i in range(1, n + 1)]
    moves = [(1, 0), (0, 1), (-1, -1)]
    
    turns = [0]
    for i in range(n, 0, -1):
        turns.append(turns[-1] + i)
    
    r, c, j = -1, 0, 0
    for i in range(1, n + 1):
        dr, dc = moves[j]
        
        for num in range(turns[i - 1] + 1, turns[i] + 1):  
            r += dr
            c += dc
            snail[r][c] = num
            
        j = (j + 1) % 3
    
    answer = []
    for arr in snail:
        answer += arr
        
    return answer