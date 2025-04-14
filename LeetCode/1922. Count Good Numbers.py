# https://leetcode.com/problems/count-good-numbers/?envType=daily-question&envId=2025-04-13
# 짝수 인덱스에는 0, 2, 4, 6, 8 짝수 5개만 가능
# 홀수 인덱스에는 2, 3, 5, 7 소수 4개만 가능

# n자리 수에서 짝수는 (n+1) // 2 개, 홀수는 n//2 개 존재
# 짝수 인덱스의 가능한 경우의 수 * 홀수 인덱스 가능한 경우의 수

class Solution:
    def countGoodNumbers(self, n: int) -> int:
        mod = 10**9 + 7

        return (pow(5, (n+1)//2, mod) * pow(4, n//2, mod)) % mod
