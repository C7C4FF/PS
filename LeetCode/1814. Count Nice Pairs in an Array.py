# https://leetcode.com/problems/count-nice-pairs-in-an-array/
# nums[i] - rev(nums[i]) == nums[j] - rev(nums[j])

class Solution:
    def countNicePairs(self, nums: List[int]) -> int:
        pair = {}
        nice = 0

        for i in range(len(nums)):
            diff = nums[i] - int(str(nums[i])[::-1])

            nice += pair.get(diff, 0)
            pair[diff] = pair.get(diff, 0) + 1
        
        return nice % (1000000000 + 7)
