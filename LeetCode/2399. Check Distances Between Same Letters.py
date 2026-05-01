# https://leetcode.com/problems/check-distances-between-same-letters/description/

# ord('a') = 97
# 주어진 거리가 0에 s에 해당 글자가 없다면 건너뛰고 있으면 확인하기

class Solution:
    def checkDistances(self, s: str, distance: List[int]) -> bool:
        table = defaultdict(list)

        for i in range(len(s)):
            table[s[i]].append(i)

        for i in range(len(distance)):
            gap = distance[i]
            ch = chr(97+i)

            if gap == 0 and not table[ch]:
                continue

            if table[ch]:
                if gap != (table[ch][1] - table[ch][0] - 1):
                    return False

        return True

            

