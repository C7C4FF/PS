# https://leetcode.com/problems/count-equal-and-divisible-pairs-in-an-array/description/?envType=daily-question&envId=2025-04-17

class Solution:
    def countPairs(self, nums: List[int], k: int) -> int:
        n = len(nums)
        ans = 0

        for i in range(n):
            for j in range(i+1, n):
                if nums[i] == nums[j]:
                    if (i * j) % k == 0:
                        ans += 1

        return ans
