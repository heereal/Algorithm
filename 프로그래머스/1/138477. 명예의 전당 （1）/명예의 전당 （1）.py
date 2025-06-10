def solution(k, score):
    answer = []
    highest = []
        
    for s in score:
        highest.append(s)
        if len(highest) > k:
            highest.remove(min(highest))
        answer.append(min(highest))
        
    return answer