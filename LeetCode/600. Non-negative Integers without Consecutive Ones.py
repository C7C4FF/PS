# https://leetcode.com/problems/non-negative-integers-without-consecutive-ones/

class Solution:
    def findIntegers(self, n: int) -> int:
        bin_n = bin(n)[2:]
        length = len(bin_n)

        # dp[i][tight][prev_bit] = dp[자릿수][인접한 1 여부][이전 비트]
        dp = [[[0] * 2 for _ in range(2)] for _ in range(length + 1)]

        # 맨 마지막에 도달했다면 조건을 만족한 것이기에 1로 초기화
        for tight in range(2):
            for prev_bit in range(2):
                dp[length][tight][prev_bit] = 1

        # 역순으로 bottom-up 
        for i in range(length-1, -1, -1):
            for tight in range(2):
                for prev_bit in range(2):
                    # 원본과 똑같이 진행되고 있다면, 원본 비트를 사용해야 함
                    if tight:
                        selectable = int(bin_n[i])
                    else:
                        selectable = 1

                    total = 0
                    for curr in range(selectable + 1):
                        if prev_bit == 1 and curr == 1:
                            continue

                        if tight and curr == selectable:
                            next_tight = 1
                        else:
                            next_tight = 0

                        total += dp[i+1][next_tight][curr]

                    dp[i][tight][prev_bit] = total

        return dp[0][1][0]

        
