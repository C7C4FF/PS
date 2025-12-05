class Solution:
    def countPartitions(self, nums: List[int]) -> int:
        ans = 0
        n = len(nums)
        for i in range(n-1):
            left = nums[:i+1]
            right = nums[i+1:]

            l_sum = sum(left)
            r_sum = sum(right)
            diff = l_sum - r_sum

            if diff % 2 == 0:
                ans += 1
        
        return ans
