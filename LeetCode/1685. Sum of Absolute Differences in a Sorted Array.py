# https://leetcode.com/problems/sum-of-absolute-differences-in-a-sorted-array/description/

# (nums[i] - nums[0]) + (nums[i] - nums[1]) + ... + (nums[i] - nums[i-1]) + (nums[i+1] - nums[i]) + (nums[i+2] - nums[i]) + ... + (nums[n-1] - nums[i])
# => (nums[i] * i - (nums[0] + nums[1] + ... + nums[i-1])) + ((nums[i+1] + nums[i+2] + ... + nums[n-1]) - nums[i] * (n-i-1))
# => prefix[n-1] - nums[i] * n - 2*(prefix[i] - nums[i] * (i+1))

class Solution:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = []
        
        prefix = []
        temp = 0
        for num in nums:
            temp += num
            prefix.append(temp)

        for i in range(n):
            ans.append(prefix[n-1] - nums[i] * n - 2*(prefix[i] - nums[i] * (i+1)))
        
        return ans

        
                
