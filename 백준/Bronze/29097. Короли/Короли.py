arr = list(map(int, input().split()))
names = ['Joffrey',  'Robb',  'Stannis']
answer = ''

total = []
for i in range(3):
    total.append(arr[i] * arr[i+3])

max_strength = max(total)
for i in range(3):
    if total[i] == max_strength:
        answer += names[i] + ' '

print(answer)