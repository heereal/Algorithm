def convert_number(n, base):
    num = "0123456789ABCDEF" # 16진수까지
    q, r = divmod(n, base) # 몫, 나머지
    
    if q == 0:
        return num[r]
    else:
        return convert_number(q, base) + num[r]
    
def solution(n, t, m, p):
    answer = ""
    num = 0
    
    while True:
        answer += convert_number(num, n)
        num += 1
        
        if len(answer) >= t * m:
            return answer[p-1:t*m:m]