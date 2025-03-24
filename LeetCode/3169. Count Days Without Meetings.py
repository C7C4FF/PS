# https://leetcode.com/problems/count-days-without-meetings/?envType=daily-question&envId=2025-03-24
# editorial #2

class Solution:
    def countDays(self, days: int, meetings: List[List[int]]) -> int:
        meetings.sort()
        free = 0
        latest_end = 0

        for s, e in meetings:
            # 이전 회의들의 마지막 종료일 latest_end 바로 다음 날보다 뒤에 있다면
            if s > latest_end + 1:
                # 시작하는 날까지 쉬는 날짜 더해주기
                free += s - latest_end - 1
            
            # 가장 늦은 날짜 최신화
            latest_end = max(latest_end, e)
        
        free += days - latest_end

        return free


'''
# 차이배열도 MLE .. 음 .. 단순히 days를 돌면 안 됨

# MLE 563/578

class Solution:
    def countDays(self, days: int, meetings: List[List[int]]) -> int:
        day = [False] + [True] * days

        for start, end in meetings:
            meet = [False] * (end - start + 1)
            day[start:end+1] = meet

        return day.count(True)
'''
