# https://leetcode.com/problems/minimum-removals-to-balance-array/?envType=daily-question&envId=2026-02-06
# 원소가 1개만 남아도 밸런스함, 최솟값 * k >= 최댓값
# 단순히 최솟값, 최댓값을 제거하는 건 최적해 보장할 수 없음
# 총 길이 - ans => balanced 길이

class Solution:
    def minRemoval(self, nums: List[int], k: int) -> int:
        ans = 0

        if len(nums) == 1:
            return ans
        
        nums.sort()

        l = 0
        for r in range(len(nums)):
            while nums[r] > nums[l] * k:
                l += 1
            ans = max(ans, r - l + 1)

        return len(nums) - ans
