lion_cnt = 0

for _ in range(9):
    vote = input()
    if vote == 'Lion':
        lion_cnt += 1

if lion_cnt >= 5:
    print('Lion')
else:
    print('Tiger')