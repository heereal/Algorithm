def solution(new_id):
    possible = 'abcdefghijklmnopqrstuvwxyz0123456789-_.'
    
    # 1단계
    new_id = list(new_id.lower())
    
    # 2단계
    for i in range(len(new_id)):
        if new_id[i] not in possible:
            new_id[i] = ''
            
    new_id = ''.join(new_id)
    
    # 3단계
    while '..' in new_id:
        new_id = new_id.replace('..', '.')
    
    # 4단계
    new_id = new_id.strip('.')
        
    # 5단계
    if not new_id:
        new_id = 'a'
    
    # 6단계
    if len(new_id) >= 16:
        new_id = new_id[:15]
        
        if new_id[-1] == '.':
            new_id = new_id[:-1]
    
    # 7단계
    if len(new_id) <= 2:
        new_id += new_id[-1] * (3 - len(new_id))
        
    return new_id