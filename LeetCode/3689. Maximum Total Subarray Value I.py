# https://leetcode.com/problems/maximum-total-subarray-value-i/description/?envType=daily-question&envId=2026-06-09
# ... ?? can be chosen more than once. = 그냥 곱해주기

class Solution:
    def maxTotalValue(self, nums: List[int], k: int) -> int:
        max_v, min_v = max(nums), min(nums)

        return (max_v - min_v) * k
