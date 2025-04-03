# https://leetcode.com/problems/maximum-value-of-an-ordered-triplet-i/description/?envType=daily-question&envId=2025-04-02
# 어제 푼 문제가 데일리 문제가 되다

# 2873 은 3 <= nums.length <= 100 이었는데, 2874는 3 <= nums.length <= 10^5 ,,,
# 요 문제가 O(n) 시간복잡도를 요구하는 듯..

class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        largest_value = 0
        diff = 0
        ans = 0

        for i in range(len(nums)):
            ans = max(ans, diff * nums[i])
            largest_value = max(largest_value, nums[i])
            diff = max(diff, largest_value - nums[i])
            
        return ans if ans >= 0 else 0
