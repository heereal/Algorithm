def solution(babbling):
    words = ['aya', 'ye', 'woo', 'ma']
    answer = 0
    
    for b in babbling:
        for word in words:
            if word * 2 in b:
                break
            else:
                b = b.replace(word, ' ')
                
        if b.isspace():
            answer += 1
        
    return answer