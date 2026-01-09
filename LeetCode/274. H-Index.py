# https://leetcode.com/problems/h-index/description/?envType=study-plan-v2&envId=top-interview-150
# h 번 이상 인용된 논문이 h 편 이상, 가장 큰 h 찾기 > h 는 1부터 len(citations) 만큼 가능함

class Solution:
    def hIndex(self, citations: List[int]) -> int:
        ans = 0

        for h in range(1, len(citations)+1):
            cnt = sum(x >= h for x in citations)
            if cnt >= h:
                ans = max(ans, h)
        
        return ans

        
            
