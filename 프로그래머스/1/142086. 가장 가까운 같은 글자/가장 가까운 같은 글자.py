def solution(s):
    dict = {}
    answer = []
    
    for i in range(len(s)):
        if s[i] in dict:
            answer.append(i - dict[s[i]])
        else:
            answer.append(-1)
            
        dict[s[i]] = i
        
    return answer