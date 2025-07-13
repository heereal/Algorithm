def solution(dartResult):
    dartResult = dartResult.replace('10', 'k')
    point = [10 if i == 'k' else i for i in dartResult]
    answer = [0, 0, 0]
    
    i = -1
    SDT = [-1, 'S', 'D', 'T']
    
    for s in point:
        if s in SDT:
            answer[i] **= SDT.index(s)
        elif s == '*':
            answer[i] *= 2
            answer[i-1] *= 2
        elif s == '#':
            answer[i] *= -1
        else:
            i += 1
            answer[i] = int(s)
    
    return sum(answer)