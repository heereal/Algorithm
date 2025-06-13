def solution(a, b):
    days = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    week = ["FRI", "SAT", "SUN", "MON", "TUE", "WED", "THU"]
    total_days = sum(days[:a-1]) + b - 1
    
    return week[total_days % 7]