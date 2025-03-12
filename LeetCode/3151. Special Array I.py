# https://leetcode.com/problems/special-array-i/?envType=daily-question&envId=2025-02-01
# nums[i] % 2 로 홀수짝수 체크

class Solution:
    def isArraySpecial(self, nums: List[int]) -> bool:
        if len(nums) == 1:
            return True
        
        parity = nums[0] % 2
        for i in range(1, len(nums)):
            check = nums[i] % 2
            if parity == check:
                return False
            else:
                parity = check
        
        return True
            
