# https://leetcode.com/problems/zero-array-transformation-i/
# Difference Array. 차이 배열... increment 면 l += i, r -= i .. decrement면 l -= i, r += i
# 그 후 누적합으로 처리...

class Solution:
    def isZeroArray(self, nums: List[int], queries: List[List[int]]) -> bool:
        # 마지막 요소에서 r+1 을 위해 길이를 하나 늘림.
        diff = [0 for _ in range(len(nums)+1)]

        # 차이 배열 만들기
        for l, r in queries:
            diff[l] -= 1
            diff[r+1] += 1
        
        for i in range(len(nums)):
            if i == 0:
                nums[i] += diff[i]
            else:
                diff[i] += diff[i-1]
                nums[i] += diff[i]
            
        if all(i <= 0 for i in nums):
            return True
        else:
            return False
