t = int(input())

for i in range(1, t + 1):
    n = int(input())
    a = input()
    b = input()
    answer = 0

    for j in range(n):
        if a[j] != b[j]:
            answer += 1
    
    print(f'Case {i}: {answer}')