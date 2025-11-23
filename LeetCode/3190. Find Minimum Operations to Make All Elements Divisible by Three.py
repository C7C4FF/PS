# https://leetcode.com/problems/find-minimum-operations-to-make-all-elements-divisible-by-three/submissions/?envType=daily-question&envId=2025-11-22

class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        dividable = 0
        for num in nums:
            if num % 3 == 0:
                dividable += 1

        return len(nums) - dividable 
