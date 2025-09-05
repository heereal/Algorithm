n = int(input())
arr = list(map(int, input().split()))

current = 0
answer = 0

for i in arr:
    if i:
        current += 1
    else:
        current -= 1
    answer += current

print(answer)