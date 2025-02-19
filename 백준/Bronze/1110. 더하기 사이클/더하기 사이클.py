N = int(input())

def cal(num, cnt):
    str_num = str(num)

    if N == num and cnt != 0:
        return cnt

    elif num < 10:
        num = int(str(str_num) + str(str_num)) 
        return cal(num, cnt+1)

    else:
        li = [int(i) for i in str_num]
        plus = sum(li)
        num = int(str(li[-1]) + str(plus)[-1])
        return cal(num, cnt+1)

print(cal(N, 0))