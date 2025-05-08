def solution(arr1, arr2):
    answer = []
    
    for i in range(len(arr1)):
        arr = arr1[i]
        res = []
        for j in range(len(arr2[0])):
            temp = 0
            for k in range(len(arr1[0])):
                temp += arr[k] * arr2[k][j]
            res.append(temp)   
        answer.append(res)
            
    return answer