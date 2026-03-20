# https://leetcode.com/problems/summary-ranges/description/

class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        ans = []

        if len(nums) == 1:
            return [str(nums[0])]

        start = 0
        for i in range(1, len(nums)):
            this = nums[i]
            if nums[i] - nums[i-1] != 1:
                # 도중에 이어지지 않는다면
                if i - start == 1:
                    # 바로 이어지지 않았을 경우
                    ans.append(f'{nums[start]}')
                else:
                    # 2번 이상 이어졌을 경우
                    ans.append(f'{nums[start]}->{nums[i-1]}')
                start = i
            
            if i == (len(nums)-1):
                # 마지막 체크
                if start == i:
                    ans.append(f'{nums[start]}')
                else:
                    ans.append(f'{nums[start]}->{nums[i]}')

        
        return ans
                
