n = int(input())
arr = list(map(int, input().split()))

answer = []
temp = 0

for i in arr:
    if i == 1:
        temp += 1
    elif temp != 0:
        answer.append(temp)
        temp = 0

answer.append(temp)
print(max(answer))