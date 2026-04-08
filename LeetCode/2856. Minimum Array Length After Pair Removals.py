# https://leetcode.com/problems/minimum-array-length-after-pair-removals/description/
# 중앙에서부터 하나씩 움직여가며 찾기
# nums[l] 보다 nums[(n+1)//2] 이 크다면 왼쪽에 있는 모든 요소들은 조건을 성립함

class Solution:
    def minLengthAfterRemovals(self, nums: List[int]) -> int:
        n = len(nums)
        ans = n

        l, r = 0, (n+1)//2 # 홀수일 때 중복 계산하지 않기 위함

        while r < n:
            if nums[l] < nums[r]:
                ans -= 2
                l += 1
                r += 1
            else:
                r += 1
        
        return ans

        
