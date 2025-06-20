def solution(numlist, n):
    arr = []
    
    for num in numlist:
        arr.append((abs(num - n), num))
        
    sorted_arr = sorted(arr, key=lambda x: (x[0], -x[1]))
    return [x[1] for x in sorted_arr]