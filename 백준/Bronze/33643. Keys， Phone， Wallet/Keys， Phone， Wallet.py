n = int(input())
all_itmes = ['keys', 'phone', 'wallet']

for _ in range(n):
    item = input()
    if item in all_itmes:
        all_itmes.remove(item)

if all_itmes:
    for item in all_itmes:
        print(item)
else:
    print('ready')