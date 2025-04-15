# https://leetcode.com/problems/maximum-absolute-sum-of-any-subarray/?envType=daily-question&envId=2025-02-26

# 부분합이 가장 큰 kadane's algorithm과, 부분합이 가장 작은 반대 kadane's algorithm 을 구하고
# 부분합이 가장 작은 것은 절댓값을 씌워 최댓값 반환

class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        current_sum = nums[0]
        max_sum = nums[0]
        
        curr_min_sum = nums[0]
        min_sum = nums[0]

        for num in nums[1:]:
            current_sum = max(num, current_sum + num) 
            max_sum = max(max_sum, current_sum)

            curr_min_sum = min(num, curr_min_sum + num)
            min_sum = min(curr_min_sum, min_sum)

        return max(abs(min_sum), max_sum)
