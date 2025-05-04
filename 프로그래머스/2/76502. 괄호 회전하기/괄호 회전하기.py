from collections import deque

def check(s):
    while True:
        if "()" in s:
            s = s.replace("()", "")
        elif "{}" in s:
            s = s.replace("{}", "")
        elif "[]" in s:
            s = s.replace("[]", "")
        else:
            if s:
                return False
            else:
                return True

def solution(s):
    answer = 0
    queue = deque(s)
    
    for i in range(len(s)):
        if check("".join(queue)):
            answer += 1
        queue.rotate(-1)
            
    return answer