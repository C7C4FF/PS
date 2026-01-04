# https://leetcode.com/problems/number-of-ways-to-paint-n-3-grid/description/?envType=daily-question&envId=2026-01-03

# 앞과 뒤가 똑같음 1번: ABA, ACA, BAB, BCB, CAC, CBC
# 세개가 전부 다름 2번: ABC, ACB, BAC, BCA, CAB, CBA
# 처음이 1번, ABA 라고 가정하면, 그 아래에는 1번이 BAB, BCB, CAC 3개, 2번은 BAC, CAB 2개가 올 수 있음
# 처음이 2번, ABC 라고 가정하면, 그 아래에는 1번 (BAB, BCB) 2번 (BCA, CAB) 2개가 올 수 있음

class Solution:
    def numOfWays(self, n: int) -> int:
        MOD = 10**9 + 7
        type1, type2 = 6, 6

        for i in range(2, n+1):
            next1 = type1 * 3 + type2 * 2
            next2 = type1 * 2 + type2 * 2
            type1, type2 = next1, next2
        
        return (type1+type2) % MOD
