# https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/?envType=study-plan-v2&envId=top-interview-150
# re.match() 는 맨 처음만 비교, search는 전체에서 찾음

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        word = re.compile(needle)
        result = word.search(haystack)
        
        if result:
            return result.start()
        else:
            return -1

'''
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        try:
            return haystack.index(needle)
        except:
            return -1

'''
