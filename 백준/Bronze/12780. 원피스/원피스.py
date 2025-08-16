h = input()
n = input()
answer = 0

for i in range(len(h) - len(n) + 1):
    if h[i:i+len(n)] == n:
        answer += 1

print(answer)