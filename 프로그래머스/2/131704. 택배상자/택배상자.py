def solution(order):
    stack = []
    answer = 0
    
    for i, box in enumerate(order):
        stack.append(i + 1)
        
        while stack and stack[-1] == order[answer]:
            stack.pop()
            answer += 1        
        
    return answer