n = int(input())

total = []
score = [[] for _ in range(3)]

for _ in range(n):
    a, b, c = map(int, input().split())
    total.append([a, b, c])
    score[0].append(a)
    score[1].append(b)
    score[2].append(c)

for i in range(n):
    answer = 0
    if score[0].count(total[i][0]) == 1:
        answer += total[i][0]
    if score[1].count(total[i][1]) == 1:
        answer += total[i][1]
    if score[2].count(total[i][2]) == 1:
        answer += total[i][2]
    print(answer)
