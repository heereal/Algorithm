from itertools import permutations

def solution(dots):
    permutation = permutations([0, 1, 2, 3], 2)
    a, b = 0, 0
    
    for p1 in permutation: 
        n1, m1 = p1
        n2, m2 = [x for x in [0, 1, 2, 3] if x not in p1]
        
        a = (dots[n1][0] - dots[m1][0]) / (dots[n1][1] - dots[m1][1])
        b = (dots[n2][0] - dots[m2][0]) / (dots[n2][1] - dots[m2][1])
        
        if a == b:
            return 1
                
    return 0