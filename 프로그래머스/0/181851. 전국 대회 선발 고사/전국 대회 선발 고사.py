def solution(rank, attendance):
    answer = []
    cnt = 0
    
    for i, attend in zip(sorted(rank), attendance):
        j = rank.index(i)
        if attendance[j]:
            answer.append(j)
            cnt += 1
        if cnt == 3:
            break
    
    a, b, c = answer
    return (a * 10000) + (b * 100) + c