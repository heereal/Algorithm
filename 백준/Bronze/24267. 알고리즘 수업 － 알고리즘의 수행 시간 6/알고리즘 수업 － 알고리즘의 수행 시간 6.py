N = int(input())
cnt_list = []
cnt = 0

for i in range(1, N-1):
    cnt += i
    cnt_list.append(cnt)

print(sum(cnt_list))
print(3)