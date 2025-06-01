from collections import Counter

def solution(topping):
    first = {}
    second = Counter(topping)
    answer = 0
    
    for n in topping:
        if n in first:
            first[n] += 1
        else:
            first[n] = 1
            
        if second[n] == 1:
            second.pop(n)
        else:
            second[n] -= 1
        
        if len(first) == len(second):
            answer += 1
            
    return answer