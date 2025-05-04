def solution(s):
    close = [")", "}", "]"]
    whole = ["()", "{}", "[]"]
    answer = 0
    
    for i in range(len(s)):
        if s[i] in close:
            continue
        
        stack = [s[i]]
        for j in range(1, len(s)):
            k = (i+j) % len(s)
            
            if s[k] in close and stack:
                if stack[-1] + s[k] == whole[close.index(s[k])]:
                    stack.pop()
            else:
                stack.append(s[k])
            
        if not stack:
            answer += 1
            
    return answer