# https://leetcode.com/problems/two-furthest-houses-with-different-colors/description/?envType=daily-question&envId=2026-04-20
# 0번째 집과 가장 멀리 떨어진 집을 뒤에서부터 찾기, 마지막 집과 가장 멀리 떨어진 집을 앞에서부터 찾기

class Solution:
    def maxDistance(self, colors: List[int]) -> int:
        ans = 0
        n = len(colors)

        for i in range(n-1, 0, -1):
            if colors[0] != colors[i]:
                ans = max(ans, i)

        for i in range(n-1):
            if colors[0] != colors[i]:
                ans = max(ans, n-1-i)
        
        return ans
    
