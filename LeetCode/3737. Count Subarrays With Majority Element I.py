# https://leetcode.com/problems/count-subarrays-with-majority-element-i/?envType=daily-question&envId=2026-06-25
# 쌩짜 bf는 TLE > 누적합으로 계산

class Solution:
    def countMajoritySubarrays(self, nums: List[int], target: int) -> int:
        ans = 0
        n = len(nums)

        for i in range(n):
            cnt = 0

            for j in range(i, n):
                if nums[j] == target:
                    cnt += 1
                else:
                    cnt -= 1

                if cnt > 0:
                    ans += 1

        return ans
        
