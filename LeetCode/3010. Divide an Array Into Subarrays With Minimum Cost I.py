# https://leetcode.com/problems/divide-an-array-into-subarrays-with-minimum-cost-i/?envType=daily-question&envId=2026-02-01
# nums 를 3개로 나누기 > nums[0] 는 고정
# 그 뒤로는 가장 작은 원소 2개를 구하면 됨 > 첫번째 값을 뺸 리스트를 정렬 후 가장 작은 원소 2개를 더하기

class Solution:
    def minimumCost(self, nums: List[int]) -> int:
        ans = nums[0]

        nums = nums[1:]
        nums.sort()
        
        return ans + nums[0] + nums[1]
