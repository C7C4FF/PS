# https://leetcode.com/problems/check-if-strings-can-be-made-equal-with-operations-i/description/?envType=daily-question&envId=2026-03-29

# 2개 떨어진 거리에서 왔다갔다 가능 > 총 합은 모두 짝수여야 함

class Solution:
    def canBeEqual(self, s1: str, s2: str) -> bool:
        ch = defaultdict(list)
        ch2 = defaultdict(list)

        for i in range(len(s1)):
            ch[s1[i]] += [i]
            ch2[s2[i]] += [i]

        for k in ch:
            if not ch2[k]:
                return False
            if (sum(ch[k]) + sum(ch2[k])) % 2 != 0:
                return False
        
        return True
