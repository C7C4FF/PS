# https://leetcode.com/problems/weighted-word-mapping/?envType=daily-question&envId=2026-06-13

class Solution:
    def mapWordWeights(self, words: List[str], weights: List[int]) -> str:
        ans = ''
        for word in words:
            weight = 0
            for ch in word:
                weight += weights[ord(ch) - ord('a')]
            
            weight %= 26
            ans += chr(ord('z') - weight)

        return ans
