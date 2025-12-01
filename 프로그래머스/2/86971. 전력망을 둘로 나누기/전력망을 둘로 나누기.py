from copy import deepcopy

def count(node, temp, connected):
    connected.append(node)
    
    for cur in temp[node]:
        if cur not in connected:
            count(cur, temp, connected)
    
    return connected

def solution(n, wires):
    tree = [[] for _ in range(n + 1)]
    answer = 100
    
    for v1, v2 in wires:
        tree[v1].append(v2)
        tree[v2].append(v1)
    
    for v1, v2 in wires:
        temp = deepcopy(tree)
        temp[v1].remove(v2)
        temp[v2].remove(v1)
        
        A = count(v1, temp, [])
        B = count(v2, temp, [])
        
        answer = min(answer, abs(len(A) - len(B)))
        
    return answer