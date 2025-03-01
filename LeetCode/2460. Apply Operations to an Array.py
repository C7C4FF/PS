# https://leetcode.com/problems/apply-operations-to-an-array/?envType=daily-question&envId=2025-03-01

class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        for i in range(len(nums)-1):
            if nums[i] == nums[i+1]:
                nums[i] *= 2
                nums[i+1] = 0

        answer = []
        cnt = 0

        for e in nums:
            if e != 0:
                answer.append(e)
            else:
                cnt += 1

        answer += [0 for _ in range(cnt)] 
        
        return answer
