# 1 -> 2 -> 4 -> 6 -> 

class Solution:
    def peopleAwareOfSecret(self, n: int, delay: int, forget: int) -> int:
        MOD = 10**9 + 7
        new = [0] * (n + 1)  # new[day]: day에 새로 비밀을 알게 된 사람 수
        new[1] = 1

        sharers = 0  
        know = 1     

        for day in range(2, n + 1):
            if day - delay >= 1:
                sharers = (sharers + new[day - delay]) % MOD
            
            if day - forget >= 1:
                sharers = (sharers - new[day - forget]) % MOD

            new[day] = sharers % MOD

            know = (know + new[day]) % MOD
            if day - forget >= 1:
                know = (know - new[day - forget]) % MOD

        return know % MOD
