# https://leetcode.com/problems/check-if-a-string-contains-all-binary-codes-of-size-k/?envType=daily-question&envId=2026-02-23

class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        bit = ['0', '1']
        lst = set("".join(i) for i in product(bit, repeat=k))
        seen = set()

        for i in range(len(s)-k+1):
            seen.add(s[i:i+k])

        if lst == seen:
            return True
        else:
            return False
        
