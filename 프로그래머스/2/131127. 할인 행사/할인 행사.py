def solution(want, number, discount):
    answer = 0
    
    for i in range(10):
        if discount[i] in want:
            index = want.index(discount[i])
            number[index] -= 1
    
    if all(x <= 0 for x in number):
            answer += 1
    
    for i in range(10, len(discount)):
        if discount[i] in want:
            index = want.index(discount[i])
            number[index] -= 1
        
        if discount[i-10] in want:
            index = want.index(discount[i-10])
            number[index] += 1
        
        if all(x <= 0 for x in number):
            answer += 1
            
    return answer