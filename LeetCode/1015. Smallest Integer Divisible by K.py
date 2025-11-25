# https://leetcode.com/problems/smallest-integer-divisible-by-k/description/?envType=daily-question&envId=2025-11-25
# 2진수가 아님...
# 1, 11, 111, 1 + 111 * 10, 1 + (1 + 111 * 10) * 10 ...
# (다음 1로 이루어진 수) = 1 + (이전의 1로 이루어진 수) * 10
# 2와 5로는 나눠질 수 없음

class Solution:
    def smallestRepunitDivByK(self, k: int) -> int:
        start = 1
        cnt = 1

        if k % 2 == 0 or k % 5 == 0:
            return -1
        
        while start % k != 0:
            start = 1 + start * 10
            cnt += 1

        return cnt
