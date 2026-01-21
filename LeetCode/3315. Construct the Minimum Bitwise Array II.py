# https://leetcode.com/problems/construct-the-minimum-bitwise-array-ii/?envType=daily-question&envId=2026-01-21
# 뒤에서부터 연속된 1의 갯수 세기 -> (num - 2^(ones-1)) 만들기
# 가장 왼쪽 1만 0으로 바꾸고 나머지를 유지하는 게 최소값이 됨

class Solution:
    def minBitwiseArray(self, nums: List[int]) -> List[int]:
        ans = []

        def or_bitwise(num: int) -> int:
            if num % 2 == 0:
                return -1  # n|(n+1)은 항상 홀수

            ones = 0
            x = num
            while x & 1:
                ones += 1
                x >>= 1

            return num - (1 << (ones - 1))


        for n in nums:
            ans.append(or_bitwise(n))
        
        return ans
        
