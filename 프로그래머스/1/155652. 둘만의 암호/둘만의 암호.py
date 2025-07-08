def solution(s, skip, index):
    answer = ''
    alpha = [chr(i) for i in range(97, 123)]
    
    for str in skip:
        alpha.remove(str)
    
    for str in s:
        i = (alpha.index(str) + index) % len(alpha)
        answer += alpha[i]
        
    return answer