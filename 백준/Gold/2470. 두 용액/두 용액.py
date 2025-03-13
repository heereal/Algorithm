N = int(input())
nums = sorted(list(map(int, input().split())))

left, right = 0, N-1
min = abs(nums[left] + nums[right])
result = [nums[left], nums[right]]

while left < right:
    sum = nums[left] + nums[right]
    
    if abs(sum) < min:
        min = abs(sum)
        result = [nums[left], nums[right]]

        if min == 0:
            break
        
    if sum > 0:
        right -= 1
    else:
        left += 1

print(result[0], result[1])