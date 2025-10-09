from itertools import combinations

def solution(orders, course):
    answer = []
    
    for n in course:
        result = {}
        
        for order in orders:
            for new_order in combinations(order, n):
                new_order = "".join(sorted(new_order))
                
                if new_order in result:
                    result[new_order] += 1
                else:
                    result[new_order] = 1

        if result:
            max_order = max(result.values())
            if max_order >= 2:
                for order in result:
                    if result[order] == max_order:
                        answer.append(order)                  
    
    return sorted(answer)