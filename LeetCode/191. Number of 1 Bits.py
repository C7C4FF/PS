# https://leetcode.com/problems/number-of-1-bits/
class Solution:
    def hammingWeight(self, n: int) -> int:
        return bin(n)[2:].count('1')

'''
# n을 오른쪽으로 한칸씩 미루면서 끝의 값이 1인지 확인

class Solution:
    def hammingWeight(self, n: int) -> int:
        hw = 0
        while n:
            hw += n & 1
            n = n >> 1
        return hw

'''
