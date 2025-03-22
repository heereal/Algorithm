def solution(s):
    stack = []
    
    if s[0] == ")":
        return False

    for p in list(s):
        if p == "(":
            stack.append(p)
        elif p == ")" and stack:
            stack.pop()
    
    return False if len(stack) else True