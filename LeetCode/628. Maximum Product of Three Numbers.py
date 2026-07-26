# https://leetcode.com/problems/maximum-product-of-three-numbers/?envType=daily-question&envId=2026-07-26
# 가장 큰 수 3개 혹은 가장 작은 수 2개 (음수) 와 가장 큰 수

class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        nums.sort()
        return max(nums[-1] * nums[-2] * nums[-3], nums[0] * nums[1] * nums[-1])
        
