import sys
input = sys.stdin.readline

N = int(input())
dancing_men = set(['ChongChong'])

for i in range(N):
    A, B = input().strip().split()

    if A in dancing_men:
        dancing_men.add(B)
    elif B in dancing_men:
        dancing_men.add(A)

print(len(dancing_men))