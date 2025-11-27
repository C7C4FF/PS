# https://leetcode.com/problems/maximum-subarray-sum-with-length-divisible-by-k/?envType=daily-question&envId=2025-11-27
# 길이가 k로 나눠지는 subarray 중 가장 큰 합인 것 고르기

class Solution:
    def maxSubarraySum(self, nums: List[int], k: int) -> int:
        

'''
# MLE

class Solution:
    def maxSubarraySum(self, nums: List[int], k: int) -> int:
        n = len(nums)
        lst = []

        for size in range(k, n + 1, k):
            window = sum(nums[0:size])
            heapq.heappush(lst, -window)

            for i in range(size, n):
                window += nums[i]
                window -= nums[i - size]
                heapq.heappush(lst, -window)

        return -heapq.heappop(lst)

'''
