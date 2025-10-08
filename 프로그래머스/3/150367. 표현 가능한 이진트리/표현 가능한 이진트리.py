def check(bin_num):
    mid = len(bin_num) // 2
    
    if mid == 0:
        return True
    elif bin_num[mid] == "0" and "1" in bin_num:
        return False
    else:
        return check(bin_num[:mid]) and check(bin_num[mid + 1:])

def solution(numbers):
    answer = []
    
    for num in numbers:
        bin_num, height = bin(num)[2:], 0
        
        while 2 ** height <= len(bin_num):
            height += 1
            
        bin_num = bin_num.zfill(2 ** height - 1)
        
        if check(bin_num):
            answer.append(1)
        else:
            answer.append(0)
        
    return answer