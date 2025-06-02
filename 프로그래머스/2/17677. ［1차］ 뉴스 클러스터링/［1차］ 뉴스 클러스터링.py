from collections import Counter

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
    
    dic1 = Counter(arr1)
    dic2 = Counter(arr2)
    
    intersection = (dic1 & dic2).values()
    union = (dic1 | dic2).values()
    
    inter_len = sum(intersection)
    union_len = sum(union)
    
    if not inter_len and not union_len:
        return 65536
    else:
        return int((inter_len / union_len) * 65536)