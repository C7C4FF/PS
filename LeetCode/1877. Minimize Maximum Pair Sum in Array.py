# https://leetcode.com/problems/minimize-maximum-pair-sum-in-array/?envType=daily-question&envId=2026-01-24

class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)
        pairs = []
        
        for i in range(n//2):
            pairs.append(nums[i]+nums[-i-1])
        
        return max(pairs)
            
