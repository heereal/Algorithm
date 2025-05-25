def solution(s):
    arr = [-1] * 26
    answer = []
    
    for i in range(len(s)):
        j = ord(s[i]) - 97
        
        if arr[j] == -1:
            answer.append(-1)
            arr[j] = i
        else:
            answer.append(i - arr[j])
            arr[j] = i
        
    return answer