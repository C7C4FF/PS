# 시침은 1분에 0.5도, 1초에 1/120
# 분침은 1분에 6도, 1초에 1/10
# 초침은 1분에 360도, 1초에 6

import datetime

def solution(h1, m1, s1, h2, m2, s2):
    answer = 0
    
    time1 = datetime.datetime(2024, 11, 18, h1, m1, s1)
    time2 = datetime.datetime(2024, 11, 18, h2, m2, s2)
    time_gap = time2 - time1
    total_seconds = time_gap.seconds
    
    hourhand = h1 * 30 + (1/2 * m1) + (1/120 * s1)
    minutehand = m1 * 6 + (1/10 * s1)
    secondhand = s1 * 6

    if secondhand == hourhand or secondhand == minutehand:
        answer += 1
        
    for _ in range(total_seconds):
        after_sec_hourhand = hourhand + (1 / 120)
        after_sec_minutehand = minutehand + (1 / 10)
        after_sec_secondhand = secondhand + 6
        
        if secondhand < hourhand and after_sec_secondhand > after_sec_hourhand:
            if minutehand < hourhand and after_sec_minutehand > after_sec_hourhand:
                answer -= 1
            answer += 1
        if secondhand < minutehand and after_sec_secondhand > after_sec_minutehand:
            answer += 1
        
        
        hourhand = after_sec_hourhand
        minutehand = after_sec_minutehand
        secondhand = after_sec_secondhand
        
        if hourhand >= 360:
            hourhand -= 360
        if minutehand >= 360:
            minutehand -= 360
        if secondhand >= 360:
            secondhand -= 360
    
    if m2 == 0 and s2 == 0:
        answer += 1
        
    return answer
