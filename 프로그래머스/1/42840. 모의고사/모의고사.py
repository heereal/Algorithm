def solution(answers):
    first = [1, 2, 3, 4, 5]
    second = [2, 1, 2, 3, 2, 4, 2, 5]
    third = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    
    cnt = [0, 0, 0, 0]
    answer = []
    
    for i in range(len(answers)):
        if answers[i] == first[i % len(first)]:
            cnt[1] += 1
        if answers[i] == second[i % len(second)]:
            cnt[2] += 1
        if answers[i] == third[i % len(third)]:
            cnt[3] += 1
            
    for i in range(1, 4):
        if cnt[i] >= max(cnt):
            answer.append(i)
            
    return answer