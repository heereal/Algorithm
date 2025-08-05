def solution(s):
    x = s[0]
    cnt = [0, 0]
    answer = 0
    
    for a in s:
        if not x:
            x = a
            
        if a == x:
            cnt[0] += 1
        else:
            cnt[1] += 1
            
        if cnt[0] == cnt[1]:
            answer += 1
            x = ''
            cnt = [0, 0]
    
    if x:
        answer += 1
        
    return answer