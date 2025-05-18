def solution(s):
    s = s.replace(",{", "")
    arr = s[2:-2].split("}")
    arr.sort(key=len)
    arr = map(int, ",".join(arr).split(","))
    
    answer = []
    for num in arr:
        if num not in answer:
            answer.append(num)
    
    return answer