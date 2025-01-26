N = int(input())
line = list(map(int, input().split()))

stack = []
target = 1

for student in line:
    stack.append(student)

    while stack and stack[-1] == target:
        stack.pop()
        target += 1

if stack:
    print('Sad')
else:
    print('Nice')