def solution(number, limit, power):
    answer = 0
    powers = []
    
    for i in range(1, number + 1):
        divisors = set([1, i])
        for j in range(1, int(i**0.5) + 1):
            if i % j == 0:
                divisors.add(j)   
                divisors.add(i // j)
        powers.append(len(divisors))
    
    for p in powers:
        if p <= limit:
            answer += p
        else:
            answer += power
    
    return answer