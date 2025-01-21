import sys
input = sys.stdin.readline

N = int(input())
stack = []

for i in range(N):
    command = input().strip()
    
    if len(command) > 1:
        stack.append(command[2:])

    elif command == '2':
        print(stack.pop()) if stack else print(-1)

    elif command == '3':
        print(len(stack))

    elif command == '4':
        print(0) if stack else print(1)

    elif command == '5':
        print(stack[len(stack)-1]) if stack else print(-1)