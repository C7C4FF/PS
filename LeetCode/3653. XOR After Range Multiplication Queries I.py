# https://leetcode.com/problems/xor-after-range-multiplication-queries-i/description/?envType=daily-question&envId=2026-04-08

class Solution:
    def xorAfterQueries(self, nums: List[int], queries: List[List[int]]) -> int:
        MOD = 10**9 + 7
        for l, r, k, v in queries:
            while l <= r:
                if l <= r:
                    nums[l] = (nums[l] * v) % MOD
                    l += k
        
        # ans = reduce(xor, nums)
        ans = nums[0]
        for i in range(1, len(nums)):
            ans = ans ^ nums[i]
        
        return ans
