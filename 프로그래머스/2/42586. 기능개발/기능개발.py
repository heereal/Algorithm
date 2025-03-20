import math

def solution(P, S):
    P = [math.ceil((100 - a) / b) for a, b in zip(P, S)]
    result = []
    front = 0
    
    for i in range(len(P)):
        if P[i] > P[front]:
            result.append(i-front)
            front = i
    
    result.append(len(P) - front)
    return result
