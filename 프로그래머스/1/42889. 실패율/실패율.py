def solution(N, stages):
    ratio = [[0, i] for i in range(N + 1)]
    stages.sort()
    
    for i in range(1, N + 1):
        if i in stages:
            cnt = len(stages) - stages.index(i)
            fail = stages.count(i)
            ratio[i][0] = fail / cnt
            
    ratio = sorted(ratio[1:], key=lambda x: (-x[0], x[1]))
    answer = [x[1] for x in ratio]
    
    return answer