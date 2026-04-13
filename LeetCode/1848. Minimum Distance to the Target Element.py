# https://leetcode.com/problems/minimum-distance-to-the-target-element/description/?envType=daily-question&envId=2026-04-13

class Solution:
    def getMinDistance(self, nums: List[int], target: int, start: int) -> int:
        ans = float('inf')

        for i in range(len(nums)):
            if nums[i] == target:
                ans = min(ans, abs(i-start))

        return ans
