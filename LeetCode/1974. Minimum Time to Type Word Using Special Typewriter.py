# https://leetcode.com/problems/minimum-time-to-type-word-using-special-typewriter/description/
# 알파뱃의 거리 => 아스키 코드로 직접 빼기 or 역방향으로 계산하기 (총 개수는 26개, 반대로 돌면 26에서 그 거리만큼 빼주면 됨)

class Solution:
    def minTimeToType(self, word: str) -> int:
        ans = len(word)
        prev = 'a'
        
        for ch in word:
            diff = abs(ord(ch) - ord(prev))
            ans += min(diff, 26 - diff)

            prev = ch

        return ans
