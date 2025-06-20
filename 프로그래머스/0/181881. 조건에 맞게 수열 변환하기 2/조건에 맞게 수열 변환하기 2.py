def solution(arr):
    answer = 0
    prev = arr[:]
    new = arr[:]
    
    while True:
        for i, num in enumerate(prev):
            if num >= 50 and num % 2 == 0:
                num //= 2
            elif num < 50 and num % 2 != 0:
                num = (num * 2) + 1
            new[i] = num
            
        if prev == new:
            break
        else:
            prev = new[:]
            answer += 1
            
    return answer