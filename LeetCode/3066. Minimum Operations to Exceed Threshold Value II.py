# https://leetcode.com/problems/minimum-operations-to-exceed-threshold-value-ii/?envType=daily-question&envId=2025-02-13
# min(a, b) * 2 + max(a, b) 지만, 최소힙이니 2a + b 해주기
# nsmallest(2, nums) 으로 계산해도 될 듯함...


class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        heapq.heapify(nums)
        cnt = 0

        while nums[0] < k:
            a, b = heapq.heappop(nums), heapq.heappop(nums)
            heapq.heappush(nums, a*2+b)
            cnt += 1

        return cnt
