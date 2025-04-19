import copy

def solution(el):
    length = len(el)
    el_sum = copy.deepcopy(el)
    
    answer = set(el)
    answer.add(sum(el))
    
    for i in range(1, length-1):
        for j in range(length):
            el_sum[j] += el[(i+j) % length]
            answer.add(el_sum[j])
    
    return len(answer)