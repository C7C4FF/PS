def change_to_sec(mmss):
    return int(mmss[:2]) * 60 + int(mmss[-2:])

def solution(video_len, pos, op_start, op_end, commands):
    answer = ''
    
    total = change_to_sec(video_len)
    op_s = change_to_sec(op_start)
    op_e = change_to_sec(op_end)
    cur = change_to_sec(pos)
    
    if cur > op_s and cur < op_e:
        cur = op_e
    
    for command in commands:
        if command == "prev":
            cur -= 10
            if cur < 0:
                cur = 0
            if cur >= op_s and cur <= op_e:
                cur = op_e
        else:
            cur += 10
            if cur >= op_s and cur <= op_e:
                cur = op_e
            if cur > total:
                cur = total
    
    if cur//60 <= 9:
        answer = "0" + str(cur//60)
    else:
        answer += str(cur//60)
        
    answer += ":"
    
    if cur%60 <= 9:
        answer += "0" + str(cur%60)
    else:
        answer += str(cur%60)
        
    return answer
