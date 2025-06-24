def solution(numbers):
    stack = []
    answer = [-1] * len(numbers)
    
    for i, n in enumerate(numbers):
        while stack and numbers[stack[-1]] < n:
            answer[stack.pop()] = n
        stack.append(i)
        
    return answer