def solution(msg):
    words = list('_ABCDEFGHIJKLMNOPQRSTUVWXYZ')
    answer = []
    
    while msg:
        i = 1
        
        while True:
            i += 1
            if i > len(msg): 
                break
            if msg[:i] not in words:
                break

        answer.append(words.index(msg[:i-1]))
        words.append(msg[:i])
        msg = msg[i-1:]
        
    return answer