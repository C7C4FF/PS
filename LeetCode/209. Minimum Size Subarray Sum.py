# https://leetcode.com/problems/minimum-size-subarray-sum/description/
# 슬라이딩 윈도우로 오른쪽으로 계속 밀면서 확인. 크면 왼쪽 값을 줄이기

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        ans = 10**9
        current_sum = 0
        n = len(nums)
        l = 0

        for r in range(n):
            current_sum += nums[r]

            while current_sum >= target:
                ans = min(ans, r - l + 1)
                current_sum -= nums[l]
                l += 1
        
        return ans if ans != 10**9 else 0
