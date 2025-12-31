# https://leetcode.com/problems/maximum-product-subarray/description/
# nums가 음수만 있을 수도 있으니 ans 선언 조심하기

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        ans = max(nums)

        cur_max = 1
        cur_min = 1

        for num in nums:
            x = cur_max * num
            y = cur_min * num

            cur_max = max(num, x, y)
            cur_min = min(num, x, y)
            
            ans = max(ans, cur_max)

        return ans  
