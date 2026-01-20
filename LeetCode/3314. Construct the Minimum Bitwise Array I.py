# https://leetcode.com/problems/construct-the-minimum-bitwise-array-i/?envType=daily-question&envId=2026-01-20

# 길이 n의 배열이 주어졌을 때, 각 인덱스 i에 대해서 ans[i] OR ans[i+1] == nums[i] 가 되도록 하는
# ans 배열을 새로 만들기 + ans의 값을 최소화하라
# 조건에 맞는 ans[i] 값을 찾을 수 없으면 -1로 두기

class Solution:
    def minBitwiseArray(self, nums: List[int]) -> List[int]:
        ans = []

        def or_bitwise(num: int) -> int:
            n = 0
            while n < num:
                if n | (n+1) == num:
                    return n
                n += 1
            return -1


        for n in nums:
            ans.append(or_bitwise(n))
        
        return ans
        
