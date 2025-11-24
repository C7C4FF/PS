# https://leetcode.com/problems/binary-prefix-divisible-by-5/description/
# 2진수 수들을 str 형태로 저장하고, 하나씩 10진수로 바꾸면서 검증

class Solution:
    def prefixesDivBy5(self, nums: List[int]) -> List[bool]:
        prefix = []
        binary = ""
        for n in nums:
            binary += str(n)
            prefix.append(binary)

        ans = [True if int(x, 2) % 5 == 0 else False for x in prefix]
        
        return ans
