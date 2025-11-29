# https://leetcode.com/problems/minimum-operations-to-make-array-sum-divisible-by-k/?envType=daily-question&envId=2025-11-29

class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        total = sum(nums)

        return total % k
