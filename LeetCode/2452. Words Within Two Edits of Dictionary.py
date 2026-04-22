# https://leetcode.com/problems/words-within-two-edits-of-dictionary/description/?envType=daily-question&envId=2026-04-22

class Solution:
    def twoEditWords(self, queries: List[str], dictionary: List[str]) -> List[str]:
        n = len(queries[0])
        ans = []

        for query in queries:
            for word in dictionary:
                diff = 0
                for i in range(n):
                    if query[i] != word[i]:
                        diff += 1
                    
                    if diff > 2:
                        break
                
                if diff <= 2:
                    ans.append(query)
                    break

        return ans
