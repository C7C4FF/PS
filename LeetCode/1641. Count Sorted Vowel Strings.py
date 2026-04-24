# https://leetcode.com/problems/count-sorted-vowel-strings/description/

# 5개로 n개를 뽑는 중복 조합. -> 5Hn = (5+n-1) C n = (4+n)Cn = (4+n)C4

# 조합 combinations, 중복 조합 combinations_with_replacement
# 순열 permutations, 중복 순열 product

class Solution:
    def countVowelStrings(self, n: int) -> int:

        return math.comb(4+n, 4)

        # vowels = ['a', 'e', 'i', 'o', 'u']
        # 
        # return len(list(combinations_with_replacement(vowels, n)))
