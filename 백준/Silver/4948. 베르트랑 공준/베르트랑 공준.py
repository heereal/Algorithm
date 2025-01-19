max = 123456*2
nums = {i : True for i in range(2, max+1)}

for i in range(2, int(max**0.5)+1):
    cnt = 2
    while i*cnt <= max:
        if nums[i*cnt]:
            nums[i*cnt] = False
        cnt += 1

while True:
    num = int(input())

    if num == 0:
        break
    else:
        cnt = 0
        for i in range(num+1, (num*2)+1):
            if nums[i]:
                cnt += 1
    print(cnt)
