# https://leetcode.com/problems/maximum-count-of-positive-integer-and-negative-integer/?envType=daily-question&envId=2025-03-12

# 0의 인덱스 i를 찾아서 i+1 = negative, 1의 인덱스 j를 찾아서 len(nums) - j ...
# 0과 1이 무조건 있는 건 아님... -> 0보다 크거나 같은 수, 1보다 크거나 같은 수로 이진탐색해도 될듯

# 양수면 positive count +1, 음수면 negative count +1

class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        p_cnt = 0
        n_cnt = 0

        for n in nums:
            if n > 0:
                p_cnt += 1
            elif n < 0:
                n_cnt += 1
        
        return max(p_cnt, n_cnt)
