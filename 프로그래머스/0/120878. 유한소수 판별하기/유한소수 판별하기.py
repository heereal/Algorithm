def gcd(a, b):
    while b > 0:
        a, b = b, a % b
    return a

def solution(a, b):
    gcd_value = gcd(a, b)
    denominator = b // gcd_value
    
    primes = [2, 5]
    cnt = 2
    
    while denominator > 1:
        if denominator % cnt == 0:
            denominator //= cnt
            if cnt not in primes or cnt > 5:
                return 2
        else:
            cnt += 1

    return 1 