class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        out = []
        p = 1

        # 왼쪽의 수를 곱함
        # [1, 1, 2, 6]
        for i in range(0, len(nums)):
            out.append(p)
            p = p * nums[i]
            
        
        p = 1

        # [24, 12, 4, 1]
        # [24 x 1, 12 x 1, 4 x 2, 1 x 6]
        for i in range(len(nums) - 1, -1, -1):    
            out[i] = out[i] * p
            p = p * nums[i]
            

        return out
