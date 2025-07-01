def solution(a, b, c, d):
    arr = [a, b, c, d]
    cnt = [0] * 7
    
    for n in arr:
        cnt[n] += 1

    if 4 in cnt:
        return a * 1111
    
    elif 3 in cnt:
        p = cnt.index(3)
        q = cnt.index(1)
        return ((10 * p) + q) ** 2
    
    elif 2 in cnt and 1 not in cnt:
        p = cnt.index(2)
        q = cnt.index(2, p+1)
        return (p + q) * abs(p - q)
    
    elif 2 in cnt and 1 in cnt:
        q = cnt.index(1)
        r = cnt.index(1, q+1)
        return q * r
    
    else:
        return min(arr)