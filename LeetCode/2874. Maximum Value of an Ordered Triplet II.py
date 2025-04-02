# https://leetcode.com/problems/maximum-value-of-an-ordered-triplet-ii/
# 요 문제가 O(n) 시간복잡도를 요구하는 듯..

class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        largest_value = 0
        diff = 0
        ans = 0

        for i in range(len(nums)):
            ans = max(ans, diff * nums[i])
            largest_value = max(largest_value, nums[i])
            diff = max(diff, largest_value - nums[i])
            
        return ans if ans >= 0 else 0
