# https://leetcode.com/problems/how-many-numbers-are-smaller-than-the-current-number/description/

class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        nums = [(idx, value) for idx, value in enumerate(nums)]
        nums.sort(key=lambda x:x[1])
        ans = [(nums[0][0], 0)]

        smaller = 0
        for i in range(1, len(nums)):
            if nums[i-1][1] == nums[i][1]:
                ans.append((nums[i][0], smaller))
            else:
                ans.append((nums[i][0], i))
                smaller = i
        
        ans.sort()
        ans = [v for _, v in ans]
            
        return ans
