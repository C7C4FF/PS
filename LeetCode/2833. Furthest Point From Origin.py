# https://leetcode.com/problems/furthest-point-from-origin/description/?envType=daily-question&envId=2026-04-24
# 더 큰 쪽으로 _ 을 몰아주기

class Solution:
    def furthestDistanceFromOrigin(self, moves: str) -> int:
        cnt = Counter(moves)

        return abs(cnt['L'] - cnt['R']) + cnt['_']
