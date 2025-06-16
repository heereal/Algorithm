def solution(k, m, score):
    score.sort()
    min_list = score[len(score) % m::m]   
    return sum(min_list) * m