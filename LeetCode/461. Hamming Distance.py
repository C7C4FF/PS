# https://leetcode.com/problems/hamming-distance/description/
# 둘을 xor 하고, 1의 개수를 세면 몇개가 다른지 구할 수 있음

class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        result = x ^ y

        return result.bit_count()
