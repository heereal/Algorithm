from collections import defaultdict

def solution(id_list, report, k):
    dict = defaultdict(set)
    
    for r in report:
        a, b = r.split()
        dict[b].add(a)
       
    answer = [0] * len(id_list)
    
    for a in dict:
        if len(dict[a]) >= k:
            for b in dict[a]:
                i = id_list.index(b)
                answer[i] += 1
    
    return answer