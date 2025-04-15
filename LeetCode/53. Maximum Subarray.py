# https://leetcode.com/problems/maximum-subarray/

# Kadane’s Algorithm
# 현재까지의 최댓값 or 지금 값 중 큰 값 고르기
# 부분합이 가장 큰 것을 고를 수 있음 

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        current_sum = nums[0]
        max_sum = nums[0]

        for num in nums[1:]:
            current_sum = max(num, current_sum + num) 
            max_sum = max(max_sum, current_sum)

        return max_sum
