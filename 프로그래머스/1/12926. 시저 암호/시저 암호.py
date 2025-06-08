def solution(s, n):
    answer = ''
    
    for str in s:
        if str == " ":
            answer += " "
        else:
            if str.isupper() and (ord(str) + n) > 90:
                answer += chr(64 + (ord(str) + n) % 90)
            elif str.islower() and (ord(str) + n) > 122:
                answer += chr(96 + (ord(str) + n) % 122)
            else:
                answer += chr(ord(str) + n)
                
    return answer