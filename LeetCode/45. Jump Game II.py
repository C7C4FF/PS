# https://leetcode.com/problems/jump-game-ii/?envType=study-plan-v2&envId=top-interview-150

class Solution:
    def jump(self, nums: List[int]) -> int:
        ans = 0

        n = len(nums)
        if n <= 1:
            return 0

        l, r = 0, 0
        pos = nums[0]

        while r < n-1:
            ans += 1
            
            for i in range(l, r+1):
                pos = max(pos, i + nums[i])

            l = r+1
            r = pos

                
        return ans
                
            
