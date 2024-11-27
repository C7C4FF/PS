# https://school.programmers.co.kr/learn/courses/30/lessons/176962 

# 과제를 우선적으로 처리하고, 남은 시간이 있으면 못 푼 과제를 스택에서 빼와서 해결하기

def solution(plans):
    answer = []
    
    planning = []
    unsolved = []
    
    for subject, start_time, time in plans:
        start_time = int(start_time[:2]) * 60 + int(start_time[3:])
        planning.append([subject, int(start_time), int(time)])
    
    # 시작하는 시간으로 정렬하기
    planning.sort(key=lambda x: x[1])
    
    while planning or unsolved:
        if len(planning) >= 2:
            this_subject, first_start, this_time = planning.pop(0)
            next_subject, next_start, next_time = planning.pop(0)
            
            now = first_start + this_time
            gap = next_start - first_start
            
            if first_start + this_time > next_start:
                unsolved.append([this_subject, this_time - gap])
                
            else:
                answer.append(this_subject)
                if unsolved:
                    remain_subject, time = unsolved.pop()
                    
                    if now + time > next_start:
                        gap = next_start - now
                        unsolved.append([remain_subject, time - gap])
                        
                    else:
                        answer.append(remain_subject)
                        now += time
                        while now < next_start and len(unsolved) >= 1:
                            remain_subject, time = unsolved.pop()

                            if now + time > next_start:
                                gap = next_start - now
                                unsolved.append([remain_subject, time - gap])
                                now += time
                            else:
                                answer.append(remain_subject)
                                now += time
                                
            
            planning.insert(0, [next_subject, next_start, next_time])
            
        elif len(planning) == 1:
            this_subject, first_start, this_time = planning.pop(0)
            answer.append(this_subject)
            
        else:
            pass
        
        if len(planning) == 0 and len(unsolved) > 0:
            answer.append(unsolved.pop()[0])

    
    return answer
