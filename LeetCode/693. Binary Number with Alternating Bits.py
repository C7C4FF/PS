# https://leetcode.com/problems/binary-number-with-alternating-bits/?envType=daily-question&envId=2026-02-18

class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        binary = bin(n)[2:]
        stack = [binary[0]]

        if n == 1:
            return True
        
        for i in range(1, len(binary)):
            if binary[i] == stack[-1]:
                return False
            else:
                stack.pop()
                stack.append(binary[i])
        
        return True
