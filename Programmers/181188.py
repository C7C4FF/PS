def solution(targets):
    answer = 0
    cur = 0
    
    targets.sort(key=lambda x : x[1])
    
    for i in range(len(targets)):
        if cur > targets[i][0]:
            continue
        cur = targets[i][1]
        answer += 1
    
    return answer
