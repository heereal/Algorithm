def solution(sides):
    answer = 0
    answer += max(sides) - (max(sides) - min(sides))
    answer += sum(sides)- max(sides) - 1
    return answer