def solution(record):
    answer = []
    dict = {}
    
    for r in record:
        arr = r.split()
        if arr[0] == 'Enter' or arr[0] == 'Change':
            dict[arr[1]] = arr[2]
    
    for r in record:
        arr = r.split()
        if arr[0] == 'Enter':
            answer.append(f'{dict[arr[1]]}님이 들어왔습니다.')
        elif arr[0] == 'Leave':
            answer.append(f'{dict[arr[1]]}님이 나갔습니다.')
    
    return answer