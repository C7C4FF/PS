# https://school.programmers.co.kr/learn/courses/30/lessons/17683

# 동일한 부분이 여러 개 있을 때 확인을 맨 앞의 것만 확인하면 안 됨
# 정규 표현식으로 확인, (?!#) 을 통해 뒤에 #이 없는 경우만 확인하기
# melody를 반복할 때 필요한 만큼만 구하기. 
# answer.sort(key=lambda x: (-x[1], x[2])) 을 통해 duration이 큰 순, start가 작은 순으로 정렬

# B#, C#, D#, F#, G#, A# ... 등 #이 붙은 것들을 다른 알파벳으로 치환해서 하는 방법도 좋을듯...

import re

def solution(m, musicinfos):
    answer = []

    for music in musicinfos:
        start, end, title, melody = music.split(",")

        start = int(start[:2]) * 60 + int(start[3:])
        end = int(end[:2]) * 60 + int(end[3:])
        
        duration = end - start
        melody_stack = []
        
        # #이 올라간 것을 정확하게 반복하기 위해 리스트로 만들어주기
        for tone in melody:
            if tone == "#":
                melody_stack[-1] += tone
            else:
                melody_stack.append(tone)
        
        temp = (melody_stack * (duration // len(melody_stack))) + melody_stack[:duration % len(melody_stack)]
        temp = ''.join(temp)
        
        if re.search(rf'{re.escape(m)}(?!#)', temp):
            answer.append([title, duration, start])
        
        # if m in temp:
        #     chk_sharp = temp.find(m) + len(m)
        #     if chk_sharp < len(temp):
        #         if temp[chk_sharp] == "#":
        #             pass
        #         else:
        #             answer.append([title, duration, start])
        #     else:
        #         answer.append([title, duration, start])
    
    if answer:
        answer.sort(key=lambda x: (-x[1], x[2]))
        return answer[0][0]
    else:
        return "(None)"
        
    
