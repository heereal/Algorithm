import sys
input = sys.stdin.readline

t = int(input())
cases = ['TTT', 'TTH', 'THT', 'THH', 'HTT', 'HTH', 'HHT', 'HHH']

for _ in range(t):
    answer = [0] * 8
    case = input()

    for i in range(38):
        idx = cases.index(case[i:i+3])
        answer[idx] += 1
    
    print(*answer)