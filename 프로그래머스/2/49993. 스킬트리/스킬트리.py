def solution(skill, skill_trees):
    answer = 0
    skill = list(skill)
    
    for tree in skill_trees:
        check = [1] * len(skill)
        is_possible = True
        
        for s in tree:
            if s in skill:
                i = skill.index(s)
                if sum(check[:i]) >= 1:
                    is_possible = False
                    break
                else:
                    check[i] = 0

        if is_possible:
            answer += 1
            
    return answer