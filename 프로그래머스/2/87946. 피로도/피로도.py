import itertools

def solution(k, dungeons):
    permutation = itertools.permutations(dungeons)
    answer = 0
    
    for p in permutation:
        current = k
        cnt = 0
        
        for min, minus in p:
            if current >= min:
                current -= minus
                cnt += 1
            else:
                current -= minus
                
        answer = max(answer, cnt)   
    
    return answer