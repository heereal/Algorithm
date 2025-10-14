def solution(survey, choices):
    scores = [0, 3, 2, 1, 0, 1, 2, 3]
    dict = {'R': 0, 'T': 0, 'C': 0, 'F': 0, 'J': 0, 'M': 0, 'A': 0, 'N': 0}
    answer = ''
    
    for i in range(len(survey)):
        if choices[i] > 4:
            dict[survey[i][1]] += scores[choices[i]]
        elif choices[i] < 4:
            dict[survey[i][0]] += scores[choices[i]]
    
    for a, b in [('R', 'T'), ('C', 'F'), ('J', 'M'), ('A', 'N')]:
        if dict[b] > dict[a]:
            answer += b
        else:
            answer += a
        
    return answer