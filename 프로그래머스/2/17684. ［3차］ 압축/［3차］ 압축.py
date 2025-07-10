def solution(msg):
    words = [0, "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
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