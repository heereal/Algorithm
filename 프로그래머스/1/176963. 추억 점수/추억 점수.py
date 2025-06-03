def solution(name, yearning, photo):
    answer = []
    
    for group in photo:
        score = 0
        for v in group:
            if v in name:
                score += yearning[name.index(v)]
        answer.append(score)
                
    return answer