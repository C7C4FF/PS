# https://leetcode.com/problems/number-of-subarrays-with-lcm-equal-to-k/description/
# 최대 공배수가 k 가 되기 위해서는 subarray 의 모든 숫자가 k의 약수로 이루어져야 함
# lcm(x, y, z) = lcm(lcm(x, y), z) .. > subarray 를 하나씩 늘릴 때마다 lcm을 갱신해주기

class Solution:
    def subarrayLCM(self, nums: List[int], k: int) -> int:
        ans = 0

        for i in range(len(nums)):
            n = nums[i]

            for j in range(i, len(nums)):
                next_n = nums[j]
                n = lcm(n, next_n)
                
                if n > k:
                    break
                
                if n == k:
                    ans += 1
                
        
        return ans
