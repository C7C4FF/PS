# https://leetcode.com/problems/reverse-bits/?envType=daily-question&envId=2026-02-16

class Solution:
    def reverseBits(self, n: int) -> int:
        binary = bin(n)[2:]
        space = 32 - len(binary)

        rv = '0' * space + binary

        return int(rv[::-1], 2)
