from collections import Counter

def solution(X, Y):
    x = Counter(X)
    y = Counter(Y)
    dic = x & y
    
    if not dic:
        return "-1"
    
    answer = ""
    
    for i in range(9, -1, -1):
        i = str(i)
        if i in dic:
            answer += i * dic[i]
    
    if answer[0] == "0":
        return "0"
    else:
        return answer