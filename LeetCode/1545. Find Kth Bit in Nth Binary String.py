# https://leetcode.com/problems/find-kth-bit-in-nth-binary-string/?envType=daily-question&envId=2026-03-03

class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        binary = "011"

        i = 3
        while i <= n:
            inverted = "".join([str(1-int(n)) for n in binary[::-1]])
            binary += "1" + inverted
            i += 1 
            
        return binary[k-1]
