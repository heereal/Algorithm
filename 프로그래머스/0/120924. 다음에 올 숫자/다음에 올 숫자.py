def solution(common):
    is_plus = False
    diff = common[1] - common[0]
    
    if common[-1] == common[0] + (diff * (len(common) - 1)):
        is_plus = True
    else:
        diff = common[1] // common[0]
    
    return common[-1] + diff if is_plus else common[-1] * diff