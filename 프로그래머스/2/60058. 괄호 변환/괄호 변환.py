from collections import deque

def reverse_str(u):
    res = ""
    for s in u:
        if s == "(":
            res += ")"
        else:
            res += "("

    return res

def is_valid(u):
    stack = []
    
    for s in u:
        if s == '(':
            stack.append(s)
        elif not stack:
            return False
        else:
            stack.pop()
        
    if stack:
        return False
    else:
        return True

def solution(p):
    if not p:
        return ""
    
    queue = deque(p)
    s, e = 0, 0
    u = ""

    while queue:
        cur = queue.popleft()
        u += cur
        
        if cur == "(":
            s += 1
        else:
            e += 1
            
        if s > 0 and e > 0 and s == e:
            break
    
    v = solution("".join(queue))
   
    if is_valid(u):
        return u + v
    else:
        return "(" + v + ")" + reverse_str(u[1:-1])