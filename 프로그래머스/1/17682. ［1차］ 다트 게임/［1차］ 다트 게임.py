def solution(dartResult):
    answer = [0, 0, 0]
    i = 0 # 문자열 위치
    cnt = -1 # 몇 번째 기회인지
    
    while i < len(dartResult):
        s = dartResult[i]
        if s.isdigit():
            if (s + dartResult[i+1]).isdigit():
                s += dartResult[i+1]
                i += 1
            cnt += 1
            answer[cnt] = int(s)
        elif s == 'D':
            answer[cnt] **= 2 
        elif s == 'T':
            answer[cnt] **= 3
        elif s == "*":
            answer[cnt-1] *= 2
            answer[cnt] *= 2
        elif s == "#": 
            answer[cnt] *= -1
        i += 1
                
    return sum(answer)