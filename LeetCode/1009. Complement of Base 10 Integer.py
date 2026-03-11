# https://leetcode.com/problems/complement-of-base-10-integer/description/?envType=daily-question&envId=2026-03-11

class Solution:
    def bitwiseComplement(self, n: int) -> int:
        ans = ""
        binary = bin(n)[2:]

        for bit in binary:
            ans += "0" if bit == "1" else "1"
        
        return int(ans, 2)
