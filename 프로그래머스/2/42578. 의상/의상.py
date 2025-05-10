def solution(clothes):
    dict = {}
    for name, type in clothes:
        if type not in dict:
            dict[type] = [name]
        else:
            dict[type] += [name]
        
    answer = 1
    for _, value in dict.items():
        answer *= (len(value) + 1)
            
    return answer - 1