# https://leetcode.com/problems/max-consecutive-ones/

class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_length, length = 0, 0

        for n in nums:
            if n == 1:
                length += 1
                max_length = max(max_length, length)
            else:
                length = 0
        
        return max_length
