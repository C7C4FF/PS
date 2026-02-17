# https://leetcode.com/problems/binary-watch/?envType=daily-question&envId=2026-02-17
# 하드코딩으로는 놓치는 게 너무 많음..

class Solution:
    def readBinaryWatch(self, turnedOn: int) -> List[str]:
        ans = []
        hours = {0: ['0'],}
        minutes = {0: ['00'],}
        
        h_bit = [8, 4, 2, 1]
        m_bit = [32, 16, 8, 4, 2, 1]

        for i in range(1, 4):
            result = [f"{sum(combo)}" for combo in combinations(h_bit, i) if sum(combo) < 12]
            hours[i] = result

        for i in range(1, 6):
            result = [f"{sum(combo):02d}" for combo in combinations(m_bit, i) if sum(combo) < 60]
            minutes[i] = result

        if turnedOn > 8:
            return ans

        for h in range(turnedOn+1):
            m = turnedOn - h
            if h in hours and m in minutes:
                for possible_h, possible_m in product(hours[h], minutes[m]):
                    ans.append(f"{possible_h}:{possible_m}")
        
        return ans

'''
# 다른 솔루션... 
class Solution:
    def readBinaryWatch(self, turnedOn: int) -> List[str]:
        res = []
        for h in range(12):
            for m in range(60):
                if (bin(h).count('1') + bin(m).count('1')) == turnedOn:
                    res.append(f"{h}:{m:02d}")
        return res
'''
