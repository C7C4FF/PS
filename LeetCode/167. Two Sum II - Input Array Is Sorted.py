# https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/?envType=study-plan-v2&envId=top-interview-150

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r = 0, len(numbers) - 1

        while l < r:
            lr_sum = numbers[l] + numbers[r]

            if lr_sum > target:
                r -= 1
            elif lr_sum < target:
                l += 1
            
            if lr_sum == target:
                return [l+1, r+1]
            
            
