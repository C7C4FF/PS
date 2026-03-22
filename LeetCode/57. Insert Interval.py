# https://leetcode.com/problems/insert-interval/

class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        ans = []
        n = len(intervals)
        x, y = newInterval[0], newInterval[1]

        merged_s, merged_e = x, y
        flag = False

        for i in range(n):
            s, e = intervals[i]
            
            # newInterval이 앞에 있어서 겹치지 않을 때
            if y < s:
                if not flag:
                    ans.append([merged_s, merged_e])
                    flag = True
                ans.append(intervals[i])
            
            # 뒤에 있어서 겹치지 않을 때
            elif e < x:
                ans.append(intervals[i])

            # 겹칠 때
            else:
                merged_s = min(merged_s, s)
                merged_e = max(merged_e, e)

        # intervals 을 다 돌았는데 삽입하지 못했을 때
        if not flag:
            ans.append([merged_s, merged_e]) 
        

        return ans
