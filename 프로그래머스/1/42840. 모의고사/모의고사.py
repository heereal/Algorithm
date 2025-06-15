def solution(answers):
    first = [1, 2, 3, 4, 5]
    second = [2, 1, 2, 3, 2, 4, 2, 5]
    third = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    
    score = [0, 0, 0]
    answer = []
    
    for i in range(len(answers)):
        if answers[i] == first[i % len(first)]:
            score[0] += 1
        if answers[i] == second[i % len(second)]:
            score[1] += 1
        if answers[i] == third[i % len(third)]:
            score[2] += 1
            
    for i, s in enumerate(score):
        if s >= max(score):
            answer.append(i+1)
            
    return answer