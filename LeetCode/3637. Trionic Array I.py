# https://leetcode.com/problems/trionic-array-i/?envType=daily-question&envId=2026-02-03

class Solution:
    def isTrionic(self, nums: List[int]) -> bool:
        asc, desc, chk = 1, 0, 0

        if nums[0] > nums[1]:
            return False

        for i in range(1, len(nums)):
            if nums[i] > nums[i-1] and asc >= 1:
                pass
            elif nums[i] > nums[i-1] and asc == 0:
                asc += 1
                desc = 0
                chk += 1
            elif nums[i] < nums[i-1] and desc == 0:
                desc += 1
                asc = 0
                chk += 1
            elif nums[i] < nums[i-1] and desc >= 1:
                pass
            else:
                return False
        
        if asc == 1 and desc == 0 and chk == 2:
            return True
        else:
            return False
