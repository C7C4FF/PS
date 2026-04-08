# https://leetcode.com/problems/find-the-length-of-the-longest-common-prefix/description/

class Solution:
    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:
        ans = 0
        arr1, arr2 = set(arr1), set(arr2)

        prefix = defaultdict(int)
        for num in arr1:
            possible = ''
            for n in str(num):
                possible += n
                prefix[possible] += 1
        
        for num in arr2:
            possible = ''
            for n in str(num):
                possible += n
                if prefix[possible] > 0:
                    ans = max(ans, len(possible))

        return ans
