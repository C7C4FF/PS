# https://leetcode.com/problems/shortest-distance-to-target-string-in-a-circular-array/description/?envType=daily-question&envId=2026-04-15
# 정방향, 역방향으로 동시에 확인하기. index가 아니라 카운터로 생각하기
# 원형 리스트는 리스트를 복제해서 풀면 쉬움

class Solution:
    def closestTarget(self, words: List[str], target: str, startIndex: int) -> int:
        try:
            idx = words.index(target)
        except ValueError:
            return -1

        ans = float('inf')
        n = len(words)
        lst = words + words
        
        i = 0
        while i < n:
            if lst[startIndex+i] == target or lst[startIndex-i] == target:
                ans = min(ans, i)
            i += 1

        return ans
