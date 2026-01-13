# https://leetcode.com/problems/longest-common-prefix/
# 정렬하고, 둘 중 작은 길이만큼 반복해서 prefix 찾기

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        n = len(strs)
        strs.sort()
        ans = ""

        if strs[0] == "":
            return ans

        length = min(len(strs[0]), len(strs[-1]))
        
        for i in range(length):
            if strs[0][i] == strs[-1][i]:
                ans += strs[0][i]
            else:
                break
        
        return ans

        
