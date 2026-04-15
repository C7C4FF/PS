# https://leetcode.com/problems/k-radius-subarray-averages/description/
# 내림할 때는 math.floor 대신 // 사용하기

class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        ans = [-1] * n
        length = k * 2 + 1

        if length > n:
            return ans
        
        sum_window = sum(nums[:length])
        ans[k] = sum_window // length

        for i in range(k+1, n-k):
            sum_window = sum_window + nums[i+k] - nums[i-k-1]
            ans[i] = sum_window // length

        return ans

'''
class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        ans = [-1] * n
        length = k * 2 + 1

        prefix = [0] * (n+1)
        temp = 0

        for i in range(n):
            prefix[i+1] = prefix[i] + nums[i]

        for i in range(k, n-k):
            ans[i] = math.floor((prefix[i+k+1] - prefix[i-k]) / length)

        return ans
'''
