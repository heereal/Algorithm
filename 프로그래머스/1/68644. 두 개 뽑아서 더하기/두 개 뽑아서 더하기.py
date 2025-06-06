def solution(numbers):
    n = len(numbers)
    answer = set()
    
    for i in range(n):
        for j in range(i + 1, n):
            answer.add(numbers[i] + numbers[j])
            
    return sorted(list(answer))