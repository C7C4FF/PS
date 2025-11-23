# https://leetcode.com/problems/count-subarrays-with-score-less-than-k/description/

class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        n = len(nums)
        ans = 0

        l, r = 0, 0
        temp = 0

        for r in range(n):
            temp += nums[r]
            while l <= r and temp * (r - l + 1) >= k:
                temp -= nums[l]
                l += 1
            ans += (r - l + 1)


        return ans
