# https://leetcode.com/problems/find-the-length-of-the-longest-common-prefix/?envType=daily-question&envId=2026-05-21
# arr1 에서 가능한 prefix 를 전부 집합에 넣고, arr2 에서 가장 긴 경우를 찾기

class Solution:
    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:
        prefixs = set()
        for num in arr1:
            temp = ''
            for n in str(num):
                temp += n
                prefixs.add(temp)
        
        ans = 0
        for num in arr2:
            prefix = ''
            for n in str(num):
                prefix += n
                if prefix in prefixs:
                    ans = max(ans, len(prefix)
                else:
                    break

        return ans


'''
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
'''
