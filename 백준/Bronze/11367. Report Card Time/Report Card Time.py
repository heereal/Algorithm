n = int(input())

for _ in range(n):
    name, score = input().split()
    score = int(score)

    if score >= 97:
        print(name, 'A+')
    elif score >= 90:
        print(name, 'A')
    elif score >= 87:
        print(name, 'B+')
    elif score >= 80:
        print(name, 'B')
    elif score >= 77:
        print(name, 'C+')
    elif score >= 70:
        print(name, 'C')
    elif score >= 67:
        print(name, 'D+')
    elif score >= 60:
        print(name, 'D')
    else:
        print(name, 'F')