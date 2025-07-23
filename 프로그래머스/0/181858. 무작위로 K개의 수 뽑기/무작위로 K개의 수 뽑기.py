def solution(arr, k):
    answer = []
    
    for n in arr:
        if len(answer) == k:
            break
        if n not in answer:
            answer.append(n)
    
    if len(answer) < k:
        answer += [-1] * (k - len(answer))
        
    return answer