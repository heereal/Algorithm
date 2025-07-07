def solution(skill, skill_trees):
    answer = 0
    skill = list(skill)
    
    for tree in skill_trees:
        check = [1] * len(skill)
        
        for s in tree:
            if s in skill:
                i = skill.index(s)
                if sum(check[:i]) >= 1:
                    break
                else:
                    check[i] = 0
        else:
            answer += 1
            
    return answer