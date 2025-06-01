def solution(topping):
    first = {topping[0]: 1}
    second = {}
    answer = 0
    
    for n in topping[1:]:
        if n in second:
            second[n] += 1
        else:
            second[n] = 1
    
    for i in range(1, len(topping)):
        n = topping[i]
        
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