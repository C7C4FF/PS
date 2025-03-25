# https://leetcode.com/problems/merge-intervals/
# 어제 문제와 마찬가지로 정렬 먼저 해주기
# s >= latest_end + 1 조건에 부합한다면 merge를 끝내고 ans 리스트에 삽입
# s < latest_end + 1 상태는 latest_start, s, latest_end, e 의 순서기 때문에 겹침 -> latest_end 를 e로 바꾸기
# 마지막에 latest_start, latest_end 넣어주기.

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()

        ans = []
        latest_start = intervals[0][0]
        latest_end = intervals[0][1]
        
        for s, e in intervals:
            if s >= latest_end + 1:
                ans.append([latest_start, latest_end])
                latest_start = s
            
            latest_end = max(latest_end, e)
        
        ans.append([latest_start, latest_end])

        return ans
