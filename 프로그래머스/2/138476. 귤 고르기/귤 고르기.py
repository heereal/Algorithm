from collections import Counter

def solution(k, tangerine):
    answer = 0
    counts = Counter(tangerine)
    
    for v in sorted(counts.values(), reverse=True):
        k -= v
        answer += 1
        if k <= 0:
            break
    
    return answer