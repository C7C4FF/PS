# https://leetcode.com/problems/binary-number-with-alternating-bits/?envType=daily-question&envId=2026-02-18
# 1 101 10101 1010101 101010101 .. 1 5 21 85 | 1/3 * (4^n - 1)
# 10 1010 101010 10101010 | 2 10 42 170 | 2/3 * (4^n - 1)

# 101010 을 하나 옮기면 10101 이 됨. 이 둘을 xor 하면 모든 비트가 1이 됨
# t = n ^ (n >> 1) 이후 t & (t + 1) == 0 으로도 해결 가능

class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        target = 1

        while target <= n:
            val = (4**target - 1) / 3
            val2 = val * 2

            if val == n or val2 == n:
                return True

            if val > n:
                break
            target += 1
        
        return False

'''
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
'''
