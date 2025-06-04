def solution(word):
    vowels = "AEIOU"
    words = []
    
    def dfs(cnt, w):
        if cnt == 5:
            return
        
        for i in range(5):
            words.append(w + vowels[i])
            dfs(cnt + 1, w + vowels[i])
    
    dfs(0, "")
    
    return words.index(word) + 1