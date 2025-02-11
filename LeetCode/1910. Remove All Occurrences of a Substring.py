# https://leetcode.com/problems/remove-all-occurrences-of-a-substring/?envType=daily-question&envId=2025-02-11
# re.search로 해당 패턴을 찾고 있으면 해당 부분을 제거
# sub로 한번에 지우는 것이 아니라 한 번에 하나씩을 지우도록 진행

class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        pattern = part
        
        pos = re.search(pattern, s)

        while pos:
            start, end = pos.start(), pos.end()
            s = s[:start] + s[end:]

            pos = re.search(pattern, s)
            
        return s
