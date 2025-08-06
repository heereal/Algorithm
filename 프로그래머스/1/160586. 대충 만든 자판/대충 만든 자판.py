def solution(keymap, targets):
    answer = []
    dict = {}
    
    for key in keymap:
        for i, k in enumerate(key):
            if k not in dict:
                dict[k] = i + 1
            elif dict[k] > i + 1:
                dict[k] = i + 1
                
    for target in targets:
        cnt = 0
        for s in target:
            if s in dict:
                cnt += dict[s]
            else:
                cnt = -1
                break
        answer.append(cnt)
            
    return answer