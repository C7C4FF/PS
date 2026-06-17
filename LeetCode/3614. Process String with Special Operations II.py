# https://leetcode.com/problems/process-string-with-special-operations-ii/?envType=daily-question&envId=2026-06-17
# editorial,,,
# 그냥 하면 MLE -> 최종 길이만 계산
# 역추적 -> 문자열을 뒤에서부터 거꾸로 순회하며 연산자를 역산하기

class Solution:
    def processStr(self, s: str, k: int) -> str:
        length = 0
        for c in s:
            if c == "*":
                if length:
                    length -= 1
            elif c == "#":
                length *= 2
            elif c == "%":
                pass
            else:
                length += 1
        
        if k + 1 > length:
            return "."
            
        for c in reversed(s):
            if c == "*":
                length += 1
            elif c == "#":
                if k + 1 > (length + 1) // 2:
                    k -= length // 2
                length = (length + 1) // 2
            elif c == "%":
                k = length - k - 1
            else:
                if k + 1 == length:
                    return c
                length -= 1
                
        return "."
