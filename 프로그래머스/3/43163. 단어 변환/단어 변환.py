def solution(begin, target, words):
    answer = int(1e9)
    visited = [False] * len(words)
    
    def check_word(word, current):
        cnt = 0
        
        for i in range(len(word)):
            if word[i] != current[i]:
                cnt += 1
                
        return True if cnt == 1 else False
    
    def dfs(cnt, current):
        nonlocal answer
        
        if current == target:
            answer = min(answer, cnt)
            return
        
        for i in range(len(words)):
            if not visited[i] and check_word(words[i], current):
                visited[i] = True
                dfs(cnt+1, words[i])
                visited[i] = False
                
    dfs(0, begin)
    
    return answer if answer != int(1e9) else 0