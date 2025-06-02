def solution(str1, str2):
    arr1 = []
    arr2 = []
    
    for i in range(len(str1)-1):
        str = str1[i:i+2].lower()
        if str.isalpha():
            arr1.append(str)
    
    for i in range(len(str2)-1):
        str = str2[i:i+2].lower()
        if str.isalpha():
            arr2.append(str)
    
    set1 = set(arr1)
    set2 = set(arr2)
    
    intersection = set1 & set2
    union = set1 | set2
    
    inter_len = 0
    union_len = 0
    
    for str in intersection:
        inter_len += min(arr1.count(str), arr2.count(str))
    
    for str in union:
        union_len += max(arr1.count(str), arr2.count(str))
    
    if not inter_len and not union_len:
        return 65536
    else:
        return int((inter_len / union_len) * 65536)