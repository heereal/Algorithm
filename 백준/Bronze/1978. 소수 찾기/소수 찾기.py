N = int(input())
num_list = list(map(int, input().split()))
cnt = len(num_list)

for i in num_list:
    if i == 1:
        cnt -= 1
        
    for j in range(2, i):
        if i%j == 0:
            cnt -= 1
            break

print(cnt)