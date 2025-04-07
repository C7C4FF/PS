# https://leetcode.com/problems/longest-increasing-subsequence/
# dp[i]는 i에서 끝나는 증가 부분 수열의 최대 길이
# nums[j] < nums[i] 만족할 때만 수열의 길이 증가

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        
        dp = [1] * n

        for i in range(n):
            for j in range(i):
                if nums[j] < nums[i]:
                    dp[i] = max(dp[i], dp[j]+1)

        return max(dp)
