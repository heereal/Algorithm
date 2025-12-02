from collections import deque

n = int(input())
s = list(input())
C, P = deque([]), deque([])

for i in range(n):
    if s[i] == 'P':
        if len(C) > 0:
            j = C.popleft()
            s[i], s[j] = 'C', 'P'
        else:
            P.append(i)
    elif s[i] == 'C':
        if len(P) > 0:
            j = P.popleft()
            s[i], s[j] = 'P', 'C'
        else:
            C.append(i)

print("".join(s))