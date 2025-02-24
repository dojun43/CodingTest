def check(user_id, banned_id):
    if len(user_id) != len(banned_id):
        return False
    for i in range(len(banned_id)):
        if banned_id[i] == "*":
            continue
        if user_id[i] != banned_id[i]:
            return False
    return True

def solution(user_id, banned_id):
    def dfs(i):
        global chk, rs
        
        if i == len(banned_id):
            rs.append(''.join(sorted(chk)))
            return
        
        for each_user_id in user_id:
            if each_user_id not in chk and check(each_user_id, banned_id[i]) == True:
                chk.append(each_user_id)
                dfs(i+1)
                chk.pop()
            
        
    global chk, rs
    
    chk = []
    rs = []

    dfs(0)
    answer = len(set(rs))

    return answer