def solution(n):
    answer = 1
    
    for i in range(2, n + 1):
        answer += 1
        
        while True:
            if answer % 3 == 0 or "3" in str(answer):
                answer += 1
            else:
                break
                
    return answer