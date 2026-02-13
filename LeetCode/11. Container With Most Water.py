# https://leetcode.com/problems/container-with-most-water/
# 이중 포문 > O(n^2) TLE
# 양쪽 끝에서 시작하고, 짧은 기둥 쪽부터 하나씩 움직여서 최댓값 구하기

class Solution:
    def maxArea(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        ans = 0

        while l < r:
            h = min(height[l], height[r])
            container = h * (r - l)

            ans = max(ans, container)

            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
        
        return ans
