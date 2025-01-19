import math

cases = []

while True:
    num = int(input())

    if num == 0:
        break
    else:
        cases.append(num)

sorted_cases = sorted(cases)

min = sorted_cases[0] + 1
max = sorted_cases[len(cases) - 1] * 2

nums = {i : True for i in range(min, max + 1)}

for i in range(2, int(max**0.5) + 1):
    total = i * math.ceil(min/i) * 2

    while total <= max:
        if nums[total]:
            nums[total] = False
        total += i

for num in cases:
    cnt = 0

    for i in range(num + 1, num*2 + 1):
        if nums[i]:
            cnt += 1
            
    print(cnt)