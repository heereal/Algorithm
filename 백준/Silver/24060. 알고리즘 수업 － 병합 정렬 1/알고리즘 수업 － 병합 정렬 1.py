N, K = map(int, input().split())
nums = list(map(int, input().split()))

def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    
    mid = (len(arr) + 1) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    return merge(left, right)

def merge(left, right):
    global cnt, res
    merged = []
    l = r = 0

    while l < len(left) and r < len(right):
        if left[l] > right[r]:
            merged.append(right[r])
            res.append(right[r])
            r += 1
        else:
            merged.append(left[l])
            res.append(left[l])
            l += 1

    while l < len(left):
        merged.append(left[l])
        res.append(left[l])
        l += 1
    
    while r < len(right):
        merged.append(right[r])
        res.append(right[r])
        r += 1

    return merged

res = []
merge_sort(nums)

if len(res) >= K:
    print(res[K-1])
else:
    print(-1)