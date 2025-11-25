# https://leetcode.com/problems/1-bit-and-2-bit-characters
# 마지막은 항상 0 , 0 앞의 1에서부터 1이 홀짝인지 세기

class Solution:
    def isOneBitCharacter(self, bits: List[int]) -> bool:
        i = len(bits) - 2
        cnt = 0

        while i >= 0 and bits[i] == 1:
            cnt += 1
            i -= 1
        
        return cnt % 2 == 0
