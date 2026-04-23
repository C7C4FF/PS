# https://leetcode.com/problems/check-if-there-is-a-valid-partition-for-the-array/description/
# 같은 원소 2개, 같은 원소 3개, 1씩 늘어나는 원소 3개

class Solution:
    def validPartition(self, nums: List[int]) -> bool:
        n = len(nums)
        
        dp = [False] * (n+1)
        dp[0] = True

        for i in range(1, n+1):
            if dp[i] == True:
                continue

            if i >= 2 and dp[i-2]:
                if nums[i-2] == nums[i-1]:
                    dp[i] = True
            
            if i >= 3 and dp[i-3]:
                if nums[i-3] == nums[i-2] == nums[i-1]:
                    dp[i] = True
                
                if nums[i-3] == nums[i-2] - 1 and nums[i-2] == nums[i-1] - 1:
                    dp[i] = True
                
        return dp[n]
