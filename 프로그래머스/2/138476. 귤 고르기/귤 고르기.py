def solution(k, tangerine):
    counts = [0] * (max(tangerine) + 1)
    
    for t in tangerine:
        counts[t] += 1
        
    counts.sort(reverse=True)
    
    total = 0
    i = 0
    
    while total < k:
        total += counts[i]
        i += 1
    
    return i