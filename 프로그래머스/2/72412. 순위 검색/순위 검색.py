from itertools import combinations

def solution(info, query):
    answer = []
    info_hash = {}
    
    # info 전처리
    for i in info:
        splited_info = i.split()
        score = splited_info.pop()
        
        # “-(조건 무시)”를 처리하기 위한 전처리 단계
        for j in range(5):
            combi = combinations(range(4), j)
            
            for com in combi:
                key = splited_info[:]
                
                for el in com:
                    key[el] = '-'
                
                key = ' '.join(key)
                if key in info_hash:
                    info_hash[key].append(int(score))
                else:
                    info_hash[key] = [int(score)]
    
    # 점수 리스트 정렬
    for key in info_hash:
        info_hash[key].sort()
    
    # query 처리
    for q in query:
        # 조건에 해당하는 점수 찾기
        splited_q = q.replace('and ', '').split()
        target_score = int(splited_q.pop())
        target_key = ' '.join(splited_q)
        
        if target_key not in info_hash:
            answer.append(0)
            continue
            
        score_list = info_hash[target_key]
        
        # upper bound 이진 탐색
        start, end = 0, len(score_list)
        mid = (start + end) // 2
        
        while start < end:
            mid = (start + end) // 2
            mid_score = score_list[mid]
            
            if target_score > mid_score:
                start = mid + 1
            else:
                end = mid
        
        answer.append(len(score_list) - start)
        

    return answer