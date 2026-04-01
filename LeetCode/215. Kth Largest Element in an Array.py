# https://leetcode.com/problems/kth-largest-element-in-an-array/description/

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heapq.heapify(nums)

        return heapq.nlargest(k, nums)[-1]

'''
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        max_heap = []

        for n in nums:
            heapq.heappush(max_heap, -n)

        while k > 0:
            ans = -heapq.heappop(max_heap)
            k -= 1

        return ans
'''
