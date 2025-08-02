def convert_number(n, base):
    q, r = divmod(n, base)
    
    if q == 0:
        return str(r)
    else:
        return convert_number(q, base) + str(r)

def is_prime_number(n):
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

def solution(n, k):
    answer = 0
    arr = convert_number(n, k).split("0")
    
    for s in arr:
        if s and s != "1":
            if is_prime_number(int(s)):
                answer += 1

    return answer