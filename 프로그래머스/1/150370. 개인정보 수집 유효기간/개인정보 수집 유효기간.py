def solution(today, terms, privacies):
    dic = {}
    dates = []
    
    for term in terms:
        type, month = term.split()
        dic[type] = int(month)
    
    for i, p in enumerate(privacies):
        date, type = p.split()
        y, m, d = map(int, date.split('.'))
        
        days = (y * 28 * 12) + ((m + dic[type]) * 28) + d
        dates.append((days, i + 1))
    
    y, m, d = map(int, today.split('.'))
    t_days = (y * 28 * 12) + (m * 28) + d
    answer = []

    for days, i in dates:
        if t_days >= days:
            answer.append(i)

    return answer