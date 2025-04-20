def solution(el):
    n = len(el)
    answer = set()
    
    for i in range(n):
        ssum = el[i]
        answer.add(ssum)
        
        for j in range(i+1, i+n):
            ssum += el[j % n]
            answer.add(ssum)
            
    return len(answer)