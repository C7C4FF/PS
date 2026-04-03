# https://leetcode.com/problems/longest-palindrome-by-concatenating-two-letter-words/description/
# 두번 이상 등장하면 palindrome 성립 -> ans += 4
# 마지막에 똑같은 문자가 있다면 +2 해주고 break

class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
        ans = 0
        seen = defaultdict(int)

        for word in words:
            target = word[::-1]

            if seen[target] > 0:
                ans += 4
                seen[target] -= 1
            else:
                seen[word] += 1

        for word, cnt in seen.items():
            if word[0] == word[1] and cnt > 0:
                ans += 2
                break
        
        return ans
        

            
