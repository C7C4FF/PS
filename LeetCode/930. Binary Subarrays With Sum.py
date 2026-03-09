# https://leetcode.com/problems/binary-subarrays-with-sum/description/

# 0이 이어지면 current_sum 이 정체되서 계속해서 발생할 수 있음 > dict.get 으로 가져오기...

class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        ans = 0
        current_sum = 0
        prefix = {0: 1}
        
        for n in nums:
            current_sum += n
            
            if current_sum - goal in prefix:
                ans += prefix[current_sum - goal]

            prefix[current_sum] = prefix.get(current_sum, 0) + 1

        return ans
        
