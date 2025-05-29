def solution(rank, attendance):
    answer = []
    
    for i, attend in enumerate(attendance):
        if attend:
            answer.append((rank[i], i))
    
    a, b, c = sorted(answer)[:3]
    return (a[1] * 10000) + (b[1] * 100) + c[1]