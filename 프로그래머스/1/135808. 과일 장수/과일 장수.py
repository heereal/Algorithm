def solution(k, m, score):
    answer = 0
    score.sort(reverse=True)
    
    for i in range(len(score) // m):
        box = score[i*m:(i*m + m)]
        answer += min(box) * m
        
    return answer