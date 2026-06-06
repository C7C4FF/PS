# https://leetcode.com/problems/left-and-right-sum-differences/description/?envType=daily-question&envId=2026-06-06

class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        ans = []
        for i in range(len(nums)):
            left, right = sum(nums[:i]), sum(nums[i+1:])
            ans.append(abs(left - right))

        return ans
