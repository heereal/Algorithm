def solution(users, emoticons):
    answer = [0, 0]
    arr = []
    
    def dfs(rates, i):
        if i == len(emoticons):
            arr.append(rates[:])
            return
        
        for rate in [10, 20, 30, 40]:
            rates[i] = rate
            dfs(rates, i + 1)
            
    dfs([0] * len(emoticons), 0)
    
    for rates in arr:
        temp = [0, 0]

        for i in range(len(users)):
            user_price = 0
            
            for j in range(len(emoticons)):
                if rates[j] >= users[i][0]:
                    user_price += emoticons[j] * ((100 - rates[j]) / 100)

                    if user_price >= users[i][1]:
                        temp[0] += 1
                        user_price = 0
                        break
                        
            temp[1] += int(user_price)
        
        if temp[0] > answer[0]:
            answer = [temp[0], temp[1]]
        elif temp[0] == answer[0] and temp[1] > answer[1]:
            answer[1] = temp[1]             
            
    return answer