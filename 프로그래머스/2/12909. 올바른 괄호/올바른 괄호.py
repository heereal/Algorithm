def solution(s):
    stack = []

    for p in list(s):
        if p == "(":
            stack.append(p)
        else:
            try:
                stack.pop()
            except IndexError:
                return False
    
    return len(stack) == 0