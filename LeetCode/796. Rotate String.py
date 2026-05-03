# https://leetcode.com/problems/rotate-string/?envType=daily-question&envId=2026-05-03
# 문자열 이어 붙이기....
# 2개를 이어 붙이고 그 안에 있는지 확인할 수도 있음

class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        if len(s) != len(goal):
            return False

        return goal in s+s

'''

class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        n = len(s)
        for i in range(n):
            s = s[1:] + s[0]
            if s == goal:
                return True

        return False

'''
