from collections import defaultdict

def solution(id_list, report, k):
    dict = defaultdict(int)
    
    for r in set(report):
        a, b = r.split()
        dict[b] += 1
 
    answer = [0] * len(id_list)
    
    for r in set(report):
        a, b = r.split()
        if dict[b] >= k:
            i = id_list.index(a)
            answer[i] += 1
    
    return answer