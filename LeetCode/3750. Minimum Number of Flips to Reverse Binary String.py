# https://leetcode.com/problems/minimum-number-of-flips-to-reverse-binary-string/

class Solution:
    def minimumFlips(self, n: int) -> int:
        binary = bin(n)[2:]
        reversed_binary = binary[::-1]

        complement = int(binary, 2) ^ int(reversed_binary, 2)

        if complement == 0:
            return 0
        else:
            return bin(complement)[2:].count("1")
