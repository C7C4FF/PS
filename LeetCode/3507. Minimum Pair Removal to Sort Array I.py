# https://leetcode.com/problems/minimum-pair-removal-to-sort-array-i/?envType=daily-question&envId=2026-01-22
# sort() != nums 조건으로 넣는 건 불가능..

class Solution:
    def minimumPairRemoval(self, nums: List[int]) -> int:
        ans = 0

        while any(nums[i] < nums[i-1] for i in range(1, len(nums))):
            pairs = []

            for i in range(len(nums)-1):
                heapq.heappush(pairs, (nums[i] + nums[i+1], i))

            ans += 1
            pair_sum, pair_index = heapq.heappop(pairs)
            nums[pair_index:pair_index+2] = [pair_sum]
            
        return ans

        
