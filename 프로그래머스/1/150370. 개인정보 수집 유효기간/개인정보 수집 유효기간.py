def solution(today, terms, privacies):
    dic = {}
    answer = []
    
    for term in terms:
        type, month = term.split()
        dic[type] = int(month)
        
    y, m, d = map(int, today.split('.'))
    t_days = (y * 28 * 12) + (m * 28) + d
    
    for i, p in enumerate(privacies):
        date, type = p.split()
        y, m, d = map(int, date.split('.'))
        days = (y * 28 * 12) + ((m + dic[type]) * 28) + d
        
        if t_days >= days:
            answer.append(i + 1)

    return answer