# https://leetcode.com/problems/maximum-element-after-decreasing-and-rearranging/?envType=daily-question&envId=2026-06-28
# 그리디 ..~ 

class Solution:
    def maximumElementAfterDecrementingAndRearranging(self, arr: List[int]) -> int:
        arr.sort()

        ans = 1

        for i in range(1, len(arr)):
            if arr[i] >= ans + 1:
                ans += 1
        
        return ans
