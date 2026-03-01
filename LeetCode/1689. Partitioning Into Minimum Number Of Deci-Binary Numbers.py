# https://leetcode.com/problems/partitioning-into-minimum-number-of-deci-binary-numbers/?envType=daily-question&envId=2026-03-01

# n 중 가장 큰 수만큼 1이 들어가야 함..

class Solution:
    def minPartitions(self, n: str) -> int:
        n = sorted(n)
        
        return int(n[-1])
